"""
storage.py
----------
Handles reading and writing student records to a JSON file on disk so that
data persists between program runs. Keeping storage logic in its own module
(instead of mixing it with the menu code) follows the single-responsibility
principle and makes it easy to swap JSON for a real database later.
"""

import json
import logging
import os
from typing import Dict

from student import Student

logger = logging.getLogger(__name__)

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")


def load_students(file_path: str = DATA_FILE) -> Dict[str, Student]:
    """Load students from the JSON data file.

    Returns an empty dictionary if the file does not exist yet or is empty,
    so the program can run correctly on first launch.
    """
    if not os.path.exists(file_path):
        logger.info("No existing data file found. Starting with an empty record set.")
        return {}

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        return {roll_no: Student.from_dict(data) for roll_no, data in raw_data.items()}
    except (json.JSONDecodeError, KeyError) as exc:
        logger.error("Data file is corrupted (%s). Starting with an empty record set.", exc)
        return {}


def save_students(students: Dict[str, Student], file_path: str = DATA_FILE) -> None:
    """Persist the current in-memory student records to the JSON data file."""
    try:
        serialisable = {roll_no: student.to_dict() for roll_no, student in students.items()}
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(serialisable, f, indent=4)
    except OSError as exc:
        logger.error("Could not save data to disk: %s", exc)
        raise
