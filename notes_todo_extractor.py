# notes_todo_extractor.py

from pathlib import Path


def extract_todos_from_notes(notes_path: str, output_path: str) -> None:
    notes_file = Path(notes_path)

    if not notes_file.exists():
        print(" Notes file does not exist.")
        return

    todos = []

    with notes_file.open("r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            # Convention: any line starting with "- [ ]" or "-" is a todo
            if stripped.startswith("- [ ]") or stripped.startswith("- "):
                todos.append(stripped)

    if not todos:
        print("No to-do items found in the notes file.")
        return

    output_file = Path(output_path)
    with output_file.open("w", encoding="utf-8") as f:
        for todo in todos:
            f.write(todo + "\n")

    print(f"Extracted {len(todos)} to-do items to: {output_file}")
