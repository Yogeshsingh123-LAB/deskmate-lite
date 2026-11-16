"""Read files from the workspace without allowing path traversal."""

from pathlib import Path

from config.settings import WORKSPACE_DIR


def _workspace_path(path: str | Path) -> Path:
    candidate = Path(path)
    if not candidate.is_absolute():
        candidate = WORKSPACE_DIR / candidate
    candidate = candidate.resolve()
    workspace = WORKSPACE_DIR.resolve()
    if candidate != workspace and workspace not in candidate.parents:
        raise ValueError("path must be inside the workspace")
    return candidate


def read_file(path: str | Path, encoding: str = "utf-8") -> str:
    """Return the text in a workspace file."""

    file_path = _workspace_path(path)
    if not file_path.is_file():
        raise FileNotFoundError(file_path)
    return file_path.read_text(encoding=encoding)
