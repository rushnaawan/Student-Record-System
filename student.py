"""
student.py
-----------
Defines the Student data model used by the Student Record System.

Following industry best practice, the data model is kept separate from
business logic (storage.py) and presentation logic (main.py). This makes
the code easier to test, maintain, and extend.
"""

from dataclasses import dataclass, field


@dataclass
class Student:
    """Represents a single student record.

    Attributes:
        roll_no: Unique identifier for the student (e.g. "AT-2026-001").
        name: Full name of the student.
        age: Age of the student in years.
        course: Course / program the student is enrolled in.
        marks: Marks / percentage obtained (0-100).
    """

    roll_no: str
    name: str
    age: int
    course: str
    marks: float = field(default=0.0)

    def to_dict(self) -> dict:
        """Convert the Student object into a JSON-serialisable dictionary."""
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,
        }

    @staticmethod
    def from_dict(data: dict) -> "Student":
        """Re-create a Student object from a dictionary (used when loading JSON)."""
        return Student(
            roll_no=data["roll_no"],
            name=data["name"],
            age=data["age"],
            course=data["course"],
            marks=data.get("marks", 0.0),
        )

    def __str__(self) -> str:
        return (
            f"{self.roll_no:<12} {self.name:<20} {self.age:<5} "
            f"{self.course:<15} {self.marks:<6}"
        )
