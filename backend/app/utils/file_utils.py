import os
from pathlib import Path


def cleanup_files(
    *file_paths
):
    for path in file_paths:
        try:
            file_path = Path(path)

            if file_path.exists():
                file_path.unlink()
                print(f"Deleted: {file_path}")

        except Exception as e:
            print(f"Cleanup failed for {path}")