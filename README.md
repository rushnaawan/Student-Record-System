# Student Record System

**Aptura Tech Solution — Batch 3 Internship — Week 1 — Task 1**

A terminal-based (command-line) Student Record System built in Python. It lets you **Add**, **View**, **Search**, **Update**, and **Delete** student records, with all data automatically saved to a local JSON file so nothing is lost between runs.

## Features

- Menu-driven command-line interface
- Add new student records (Roll No, Name, Age, Course, Marks)
- View all students in a formatted table
- Search for a student by Roll No
- Update any field of an existing student (leave blank to keep old value)
- Delete a student record (with a confirmation prompt)
- Data persistence using JSON (`students.json`) — your records survive after closing the program
- Input validation (won't crash on empty fields or invalid numbers)
- Activity logging to `app.log` for traceability
- Clean, modular code structure following separation of concerns

## Project Structure

```
student_record_system/
├── main.py              # Entry point — menu loop & CLI logic
├── student.py           # Student data model (dataclass)
├── storage.py           # JSON load/save logic (persistence layer)
├── students.json         # Auto-created on first run — stores your data
├── app.log               # Auto-created — logs actions and errors
├── screenshots/          # Sample screenshots of the program running
├── README.md
└── report.docx           # Project report
```

## Requirements

- Python 3.8 or later (no external libraries required — uses only the standard library)

## How to Run

1. Make sure Python 3 is installed:
   ```bash
   python3 --version
   ```
2. Open a terminal in the project folder.
3. Run the program:
   ```bash
   python3 main.py
   ```
4. Use the on-screen menu (enter a number 1–6) to manage student records.

## Menu Options

| Option | Action |
|--------|--------|
| 1 | Add Student |
| 2 | View All Students |
| 3 | Search Student |
| 4 | Update Student |
| 5 | Delete Student |
| 6 | Exit |

## Design Notes / Best Practices Followed

- **Separation of concerns:** data model (`student.py`), storage (`storage.py`), and UI/menu logic (`main.py`) are kept in separate files.
- **Data persistence:** records are saved to `students.json` immediately after every add/update/delete, so the program can be closed and reopened without losing data.
- **Input validation:** the program keeps re-prompting instead of crashing when given empty or invalid input.
- **Error handling & logging:** unexpected errors are caught, logged to `app.log`, and shown to the user in a friendly way instead of crashing the program.
- **Type hints & docstrings:** used throughout for readability and maintainability.

## Screenshots

See the `screenshots/` folder for sample runs covering Add, View, Search, Update, and Delete operations.

## Author

Prepared as part of the Aptura Tech Solution Batch 3 Internship, Week 1, Python track.
