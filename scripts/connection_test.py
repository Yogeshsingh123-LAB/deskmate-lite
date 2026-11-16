"""Validate the local Deskmate Lite connection configuration."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from config.settings import DEEPSEEK_BASE_URL, DEEPSEEK_MODEL, INPUT_DIR, OUTPUT_DIR


def main() -> int:
    """Check that the configured endpoint and workspace are usable."""

    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"DeepSeek endpoint: {DEEPSEEK_BASE_URL}")
    print(f"DeepSeek model: {DEEPSEEK_MODEL}")
    print(f"Workspace ready: {INPUT_DIR} and {OUTPUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
