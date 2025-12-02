# main.py

from file_organizer import organize_folder
from notes_todo_extractor import extract_todos_from_notes
from time_tracker import time_tracker_menu
import os


def print_menu() -> None:
    print("\n=== Personal Productivity Automation Toolkit ===")
    print("1. Organize files in a folder")
    print("2. Extract to-do items from notes file")
    print("3. Time tracker")
    print("0. Exit")


def handle_organize_folder() -> None:
    """Handles the logic for organizing a folder."""
    folder_path = input("Enter folder path to organize: ").strip()
    if not os.path.isdir(folder_path):
        print(f"Error: Folder not found at '{folder_path}'")
        return
    try:
        organize_folder(folder_path)
        print("Folder organized successfully.")
    except Exception as e:
        print(f"An error occurred during folder organization: {e}")


def handle_extract_todos() -> None:
    """Handles the logic for extracting to-do items from a notes file."""
    notes_path = input("Enter path to notes .txt file: ").strip()
    if not os.path.isfile(notes_path):
        print(f"Error: Notes file not found at '{notes_path}'")
        return

    output_path = input(
        "Enter path to save extracted to-dos (e.g. todos.txt): "
    ).strip()

    try:
        extract_todos_from_notes(notes_path, output_path)
        print(f"To-dos extracted successfully to '{output_path}'.")
    except Exception as e:
        print(f"An error occurred during to-do extraction: {e}")


def main() -> None:
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            folder_path = input("Enter folder path to organize: ").strip()
            organize_folder(folder_path)
        elif choice == "2":
            notes_path = input("Enter path to notes .txt file: ").strip()
            output_path = input(
                "Enter path to save extracted to-dos (e.g. todos.txt): "
            ).strip()
            extract_todos_from_notes(notes_path, output_path)
        elif choice == "3":
            time_tracker_menu()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Its not a valid choice. Please try again.")


if __name__ == "__main__":
    main()
