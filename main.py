"""
main.py
-------
Aptura Tech Solution — Batch 3 Internship — Week 1
Task 1: Student Record System (Python, terminal-based)

A menu-driven, terminal-based Student Record System that lets a user
Add, View, Search, Update and Delete student records. Records are
persisted to a local JSON file (students.json) so data is not lost
when the program exits.

Run with:  python main.py
"""

import logging
import sys

from student import Student
from storage import load_students, save_students

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

MENU = """
==================================================
        APTURA TECH - STUDENT RECORD SYSTEM
==================================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
==================================================
"""


def get_non_empty_input(prompt: str) -> str:
    """Repeatedly ask for input until the user enters a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def get_int_input(prompt: str) -> int:
    """Repeatedly ask for input until the user enters a valid integer."""
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid whole number.")


def get_float_input(prompt: str) -> float:
    """Repeatedly ask for input until the user enters a valid number."""
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")


def add_student(students: dict) -> None:
    """Prompt the user for details and add a new student record."""
    roll_no = get_non_empty_input("Enter Roll No: ")
    if roll_no in students:
        print(f"A student with roll no '{roll_no}' already exists.")
        return

    name = get_non_empty_input("Enter Name: ")
    age = get_int_input("Enter Age: ")
    course = get_non_empty_input("Enter Course: ")
    marks = get_float_input("Enter Marks (0-100): ")

    students[roll_no] = Student(roll_no, name, age, course, marks)
    save_students(students)
    logger.info("Added student %s", roll_no)
    print(f"\nStudent '{name}' added successfully!\n")


def view_students(students: dict) -> None:
    """Display all student records in a formatted table."""
    if not students:
        print("\nNo student records found.\n")
        return

    print("\n" + "-" * 65)
    print(f"{'Roll No':<12} {'Name':<20} {'Age':<5} {'Course':<15} {'Marks':<6}")
    print("-" * 65)
    for student in students.values():
        print(student)
    print("-" * 65 + f"\nTotal Records: {len(students)}\n")


def search_student(students: dict) -> None:
    """Search for a student by roll number."""
    roll_no = get_non_empty_input("Enter Roll No to search: ")
    student = students.get(roll_no)
    if student:
        print("\nStudent Found:")
        print("-" * 65)
        print(f"{'Roll No':<12} {'Name':<20} {'Age':<5} {'Course':<15} {'Marks':<6}")
        print("-" * 65)
        print(student, "\n")
    else:
        print(f"\nNo student found with roll no '{roll_no}'.\n")


def update_student(students: dict) -> None:
    """Update an existing student's details. Press Enter to keep a field unchanged."""
    roll_no = get_non_empty_input("Enter Roll No to update: ")
    student = students.get(roll_no)
    if not student:
        print(f"\nNo student found with roll no '{roll_no}'.\n")
        return

    print("Leave a field blank to keep its current value.")
    name = input(f"Enter Name [{student.name}]: ").strip()
    age = input(f"Enter Age [{student.age}]: ").strip()
    course = input(f"Enter Course [{student.course}]: ").strip()
    marks = input(f"Enter Marks [{student.marks}]: ").strip()

    if name:
        student.name = name
    if age:
        try:
            student.age = int(age)
        except ValueError:
            print("Invalid age entered — keeping previous value.")
    if course:
        student.course = course
    if marks:
        try:
            student.marks = float(marks)
        except ValueError:
            print("Invalid marks entered — keeping previous value.")

    save_students(students)
    logger.info("Updated student %s", roll_no)
    print(f"\nStudent '{roll_no}' updated successfully!\n")


def delete_student(students: dict) -> None:
    """Delete a student record after confirmation."""
    roll_no = get_non_empty_input("Enter Roll No to delete: ")
    student = students.get(roll_no)
    if not student:
        print(f"\nNo student found with roll no '{roll_no}'.\n")
        return

    confirm = input(f"Are you sure you want to delete '{student.name}'? (y/n): ").strip().lower()
    if confirm == "y":
        del students[roll_no]
        save_students(students)
        logger.info("Deleted student %s", roll_no)
        print(f"\nStudent '{roll_no}' deleted successfully!\n")
    else:
        print("\nDeletion cancelled.\n")


def main() -> None:
    """Entry point: loads data, shows the menu loop, and handles user choices."""
    students = load_students()
    print("Welcome to the Aptura Tech Student Record System!")

    actions = {
        "1": add_student,
        "2": view_students,
        "3": search_student,
        "4": update_student,
        "5": delete_student,
    }

    while True:
        print(MENU)
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "6":
            print("\nThank you for using the Student Record System. Goodbye!")
            logger.info("Application closed by user.")
            sys.exit(0)

        action = actions.get(choice)
        if action:
            try:
                action(students)
            except Exception as exc:  # noqa: BLE001 - top-level safety net for a CLI app
                logger.exception("Unexpected error: %s", exc)
                print(f"\nAn unexpected error occurred: {exc}\n")
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.\n")


if __name__ == "__main__":
    main()
