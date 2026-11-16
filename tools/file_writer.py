"""Write files to the workspace without allowing path traversal."""

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


def write_file(path: str | Path, content: str, encoding: str = "utf-8") -> Path:
    """Write text to a workspace file and return its resolved path."""

    file_path = _workspace_path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding=encoding)
    return file_path
