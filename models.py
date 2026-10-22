"""
Module: models.py
Defines the core data models for the EduTrack Student Management System:
- AttendanceRecord
- Student
"""

from datetime import datetime
from typing import Dict, List

class AttendanceRecord:
    """Represents attendance statistics for a single student."""
    def __init__(self, total_sessions: int = 0, attended_sessions: int = 0):
        if attended_sessions > total_sessions:
            raise ValueError("Attended sessions cannot exceed total sessions.")
        self.total_sessions = max(0, total_sessions)
        self.attended_sessions = max(0, attended_sessions)

    @property
    def percentage(self) -> float:
        """Calculates attendance percentage."""
        if self.total_sessions == 0:
            return 100.0
        return round((self.attended_sessions / self.total_sessions) * 100, 2)

    def mark_attendance(self, present: bool = True):
        """Records attendance for a new session."""
        self.total_sessions += 1
        if present:
            self.attended_sessions += 1

    def to_dict(self) -> dict:
        return {
            "total_sessions": self.total_sessions,
            "attended_sessions": self.attended_sessions,
            "percentage": self.percentage
        }


class Student:
    """Represents a student enrolled in the university."""
    def __init__(self, student_id: str, name: str, department: str = "CSE-AI&ML", division: str = "SY-A"):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.division = division
        self.attendance = AttendanceRecord()
        self.marks: Dict[str, float] = {}

    def add_subject_mark(self, subject: str, score: float):
        """Adds or updates score for an academic subject (0-100)."""
        if not (0 <= score <= 100):
            raise ValueError("Marks must be between 0 and 100.")
        self.marks[subject] = float(score)

    @property
    def gpa(self) -> float:
        """Computes current Grade Point Average on a 10.0 scale."""
        if not self.marks:
            return 0.0
        average_score = sum(self.marks.values()) / len(self.marks)
        return round(average_score / 10.0, 2)

    @property
    def defaulter_status(self) -> str:
        """
        Categorizes student status based on university guidelines:
        - Critical Defaulter: < 20%
        - Major Defaulter: 21% - 50%
        - Moderate Defaulter: 50% - 75%
        - Eligible: >= 75%
        """
        pct = self.attendance.percentage
        if pct < 20.0:
            return "Critical Defaulter (< 20%)"
        elif 20.0 <= pct <= 50.0:
            return "Major Defaulter (21% - 50%)"
        elif 50.0 < pct < 75.0:
            return "Moderate Defaulter (50% - 75%)"
        else:
            return "Eligible / Regular (>= 75%)"

    def to_dict(self) -> dict:
        return {
            "student_id": self.student_id,
            "name": self.name,
            "department": self.department,
            "division": self.division,
            "attendance": self.attendance.to_dict(),
            "marks": self.marks,
            "gpa": self.gpa,
            "defaulter_status": self.defaulter_status
        }
