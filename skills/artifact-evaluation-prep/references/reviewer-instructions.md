# Reviewer Instructions

Reviewer instructions should optimize for a tired evaluator with limited time.

## Required Shape

1. One-paragraph artifact purpose.
2. Hardware and time budget.
3. Setup commands.
4. Quick smoke test.
5. Core reproduction commands.
6. Expected outputs and comparison instructions.
7. Troubleshooting.
8. Optional extended runs.

## Command Rules

- Use commands from the repository root unless stated otherwise.
- Define environment variables before using them.
- Make output paths explicit.
- State approximate runtime for each command.
- State expected success text, metric, plot, or file.
- Provide a recovery path for common dependency, CUDA, data, and memory failures.

## Wording

Use direct, reviewer-facing language:

- "Run this command to reproduce Table 1, row 3."
- "This command should finish in about 12 minutes on one A100."
- "The expected output is `outputs/table1_main.csv`; values should match the paper within 0.2 due to seed variance."

Avoid:

- "Just run the script."
- "Results may vary" without a tolerance.
- "Download the data" without URL, license, size, and path.
