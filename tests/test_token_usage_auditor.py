from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "skills/token-usage-auditor/scripts/collect_token_usage.py"


class TokenUsageAuditorSmokeTest(unittest.TestCase):
    def test_collects_codex_and_claude_usage_without_prompt_content(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            project = root / "project"
            project.mkdir()
            codex_root = root / "codex"
            claude_root = root / "claude"
            codex_session = codex_root / "2026/05/04/rollout-test.jsonl"
            claude_session = claude_root / "-tmp-project/session.jsonl"
            codex_session.parent.mkdir(parents=True)
            claude_session.parent.mkdir(parents=True)

            codex_records = [
                {
                    "timestamp": "2026-05-04T10:00:00Z",
                    "type": "session_meta",
                    "payload": {
                        "id": "codex-session",
                        "timestamp": "2026-05-04T10:00:00Z",
                        "cwd": str(project),
                        "model_provider": "openai",
                    },
                },
                {
                    "timestamp": "2026-05-04T10:01:00Z",
                    "type": "event_msg",
                    "payload": {
                        "type": "token_count",
                        "info": {
                            "last_token_usage": {
                                "input_tokens": 100,
                                "cached_input_tokens": 40,
                                "output_tokens": 20,
                                "reasoning_output_tokens": 5,
                                "total_tokens": 120,
                            }
                        },
                    },
                },
            ]
            codex_session.write_text("\n".join(json.dumps(record) for record in codex_records), encoding="utf-8")

            claude_record = {
                "timestamp": "2026-05-04T11:00:00Z",
                "type": "assistant",
                "requestId": "req-1",
                "cwd": str(project),
                "sessionId": "claude-session",
                "gitBranch": "main",
                "message": {
                    "id": "msg-1",
                    "model": "claude-sonnet",
                    "usage": {
                        "input_tokens": 10,
                        "cache_creation_input_tokens": 100,
                        "cache_read_input_tokens": 30,
                        "output_tokens": 5,
                    },
                    "content": [{"type": "text", "text": "should not be copied"}],
                },
            }
            claude_session.write_text(
                "\n".join([json.dumps(claude_record), json.dumps(claude_record)]),
                encoding="utf-8",
            )

            proc = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--project-root",
                    str(project),
                    "--codex-root",
                    str(codex_root),
                    "--claude-root",
                    str(claude_root),
                    "--format",
                    "json",
                ],
                text=True,
                capture_output=True,
                check=True,
            )

            payload = json.loads(proc.stdout)
            by_agent = payload["summary_by_agent"]
            self.assertEqual(by_agent["codex"]["fresh_tokens"], 80)
            self.assertEqual(by_agent["codex"]["total_context_tokens"], 120)
            self.assertEqual(by_agent["claude-code"]["fresh_tokens"], 115)
            self.assertEqual(by_agent["claude-code"]["total_context_tokens"], 145)
            self.assertEqual(by_agent["claude-code"]["usage_events"], 1)
            self.assertNotIn("should not be copied", proc.stdout)


if __name__ == "__main__":
    unittest.main()
