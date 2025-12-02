# file_organizer.py

import os
import shutil
from pathlib import Path
from typing import Dict


EXTENSION_MAP: Dict[str, str] = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Text",
    ".csv": "Data",
    ".xlsx": "Data",
    ".py": "Code",
    ".ipynb": "Code",
    ".json": "Data",
}


def organize_folder(folder_path: str) -> None:
    base_path = Path(folder_path)

    if not base_path.exists() or not base_path.is_dir():
        print("The folder does not exist.")
        return

    print(f"Organizing files in: {base_path}")

    for item in base_path.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            target_folder_name = EXTENSION_MAP.get(ext, "Other")
            target_folder = base_path / target_folder_name
            target_folder.mkdir(exist_ok=True)

            target_path = target_folder / item.name
            try:
                shutil.move(str(item), str(target_path))
                print(f"Moved: {item.name} → {target_folder_name}/")
            except shutil.Error as e:
                print(f"Could not move {item.name}: {e}")

    print("Organizing complete.")
