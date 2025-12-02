# time_tracker.py

import csv
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("time_log.csv")


def _write_header_if_needed() -> None:
    if not LOG_FILE.exists():
        with LOG_FILE.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["task_name", "start_time", "end_time", "duration_minutes"])


def _log_task(task_name: str, start_time: datetime, end_time: datetime) -> None:
    _write_header_if_needed()
    duration = (end_time - start_time).total_seconds() / 60.0

    with LOG_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [task_name, start_time.isoformat(), end_time.isoformat(), f"{duration:.2f}"]
        )

    print(f"Logged task '{task_name}' for {duration:.2f} minutes.")


def start_task_session() -> None:
    task_name = input("Enter task name: ").strip()
    if not task_name:
        print("Task name cannot be empty.")
        return

    start_time = datetime.now()
    print(f"Started task '{task_name}' at {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    input("Press ENTER to stop the task...")

    end_time = datetime.now()
    print(f"Stopped at {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

    _log_task(task_name, start_time, end_time)


def view_time_logs() -> None:
    if not LOG_FILE.exists():
        print("ℹNo logs found yet.")
        return

    with LOG_FILE.open("r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if len(rows) <= 1:
        print("No tasks recorded yet.")
        return

    print("\n=== Time Log ===")
    for row in rows[1:]:
        task_name, start_time, end_time, duration = row
        print(f"- {task_name}: {duration} minutes (from {start_time} to {end_time})")


def time_tracker_menu() -> None:
    while True:
        print("\n=== Time Tracker ===")
        print("1. Start new task session")
        print("2. View time log")
        print("0. Back to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            start_task_session()
        elif choice == "2":
            view_time_logs()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
