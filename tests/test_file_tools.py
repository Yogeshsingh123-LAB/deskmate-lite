import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.file_reader import read_file
from tools.file_writer import write_file


class FileToolsTest(unittest.TestCase):
    def test_write_and_read_workspace_file(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / "workspace"
            with patch("tools.file_writer.WORKSPACE_DIR", workspace), patch(
                "tools.file_reader.WORKSPACE_DIR", workspace
            ):
                written = write_file("nested/note.txt", "hello")

                self.assertEqual(written, workspace / "nested/note.txt")
                self.assertEqual(read_file("nested/note.txt"), "hello")

    def test_file_tools_reject_paths_outside_workspace(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / "workspace"
            with patch("tools.file_writer.WORKSPACE_DIR", workspace), patch(
                "tools.file_reader.WORKSPACE_DIR", workspace
            ):
                with self.assertRaises(ValueError):
                    write_file("../outside.txt", "nope")
                with self.assertRaises(ValueError):
                    read_file("../outside.txt")


if __name__ == "__main__":
    unittest.main()
