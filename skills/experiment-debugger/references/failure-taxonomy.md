# Experiment Failure Taxonomy

## Failure Mode Classification

### 1. NaN / Gradient Instability

**Symptoms**: `loss = nan`, `loss = inf`, gradient norm spikes, `RuntimeError: Function X returned nan values`

**Primary causes** (in frequency order):
1. Log of zero or near-zero in loss (cross-entropy with logits vs softmax probabilities)
2. Division by zero (custom normalization, per-class metrics on empty classes)
3. FP16 underflow (values below ~6e-8 flush to zero in float16)
4. Exploding gradients (LR too high, missing gradient clipping)
5. Bad initialization (weights initialized with std >> 1)
6. Batch normalization with batch size 1 (zero variance → NaN statistics)
7. Attention on very long sequences with float16 softmax overflow

**Quick triage**: If NaN at step 0, it's data or initialization. If NaN after N steps, it's instability.

### 2. GPU OOM

**Symptoms**: `CUDA out of memory. Tried to allocate X GiB`, `RuntimeError: CUDA error: device-side assert triggered`

**Primary causes**:
1. Batch size too large
2. Memory leak: gradients or tensors retained in Python lists across steps
3. Sequence length too long (quadratic attention memory)
4. Gradient checkpointing not enabled when needed
5. Evaluation run without `torch.no_grad()` or `model.eval()`
6. Graph retained via `loss.item()` not called (detach from graph)
7. Multi-GPU: activation memory replicated on wrong device

**Quick triage**: Does OOM happen at step 1 (too-large allocation) or later (leak)?

### 3. Slow Training

**Symptoms**: GPU utilization < 70%, samples/sec far below expected, training ETA unrealistically long

**Primary causes**:
1. `num_workers=0` in DataLoader
2. Online preprocessing (augmentations, tokenization) on the critical path
3. Dataset on network filesystem (NFS, GPFS) without local caching
4. Small batch size with large model → GPU underutilized
5. `cudnn.benchmark=False` when input size is constant
6. Sync operations in training loop (explicit `.item()` calls per step)
7. Logging overhead (writing every step to disk/wandb/tensorboard)

**Quick triage**: Is GPU utilization low? Use `nvidia-smi dmon -s u` or check `run-status-monitor` GPU occupancy.

### 4. Slow Data Loading

**Symptoms**: GPU utilization spikes and drops rhythmically, profiler shows >30% in DataLoader

**Primary causes**:
1. Too few DataLoader workers for the I/O bandwidth
2. Random access to HDF5/LMDB files without sequential prefetch
3. Image decoding on CPU without hardware acceleration (use `torchvision.io` for JPEG)
4. Network filesystem latency per file open (use local SSD cache or LMDB)
5. `pin_memory=False` causing extra CPU→GPU copy overhead

### 5. Metric Errors

**Symptoms**: accuracy > 1.0, loss < 0, metric is NaN, metric is identical every epoch, metric jumps discontinuously

**Primary causes**:
1. Batch-mean vs dataset-mean confusion with unequal batch sizes
2. Logits passed to metric that expects probabilities (or vice versa)
3. Class label offset (0-indexed vs 1-indexed)
4. Padding tokens included in sequence metric computation
5. Metric accumulated per-step across batches and divided by step count (wrong for unequal batches)
6. Val/test loader using train-time augmentation or shuffle
7. Metric reset not called between epochs

### 6. Reproducibility Failure

**Symptoms**: Different loss curves or final metrics with identical config and seed

**Primary causes**:
1. Incomplete seed: missing `torch.cuda.manual_seed_all` or `np.random.seed`
2. Non-deterministic CUDA ops: `torch.backends.cudnn.deterministic = False`
3. DataLoader shuffle with `num_workers > 0` and no `worker_init_fn`
4. Different CUDA/cuDNN version between runs
5. Multi-GPU: non-deterministic all-reduce (use `NCCL_ALGO=Tree` for deterministic NCCL)
6. Checkpoint loaded from different step
7. External randomness (random data augmentation in a subprocess with different seed)

### 7. Crash / Process Exit

**Symptoms**: Process killed by OOM killer, SIGKILL, timeout, or host failure

**Primary causes**:
1. CPU RAM OOM (different from GPU OOM): data preprocessing exceeds host memory
2. Job time limit exceeded on SLURM/RunAI
3. Disk quota exceeded (checkpoints or logs fill the filesystem)
4. Network disconnection during DDP / NCCL communication
5. Hardware ECC error on GPU

**Quick triage**: Check `dmesg`, SLURM sacct exit code, or container log for OOM killer messages.

### 8. Silent Errors

**Symptoms**: Run completes, metrics look plausible, but results are wrong on inspection

**Primary causes**:
1. Eval loop uses train-mode dropout or BN (`model.train()` not switched to `model.eval()`)
2. Wrong checkpoint loaded at eval time
3. Wrong normalization constants applied to test data
4. Label smoothing or logit scaling applied at eval
5. A metric file was not cleared between runs and old results were reported

## Decision Tree

```
Training produces NaN?
  → Step 0: data/init bug → check loss fn, input range, weight init
  → Later: instability → check LR, gradient clipping, FP16 config

GPU OOM?
  → Step 1: too-large allocation → reduce batch size, check model size
  → Later: likely memory leak → profile retention of tensors

Training too slow?
  → GPU < 70%: data-bound → profile DataLoader, check num_workers, filesystem
  → GPU ~100% but slow: model-bound → check batch size, gradient checkpointing, mixed precision

Metric value impossible?
  → Verify on tiny synthetic example with known expected value

Run not reproducible?
  → Check full seed coverage → check cudnn.deterministic → check num_workers + worker_init_fn

Process crashes?
  → Check exit code and system log → check CPU RAM, disk quota, job time limit
```
