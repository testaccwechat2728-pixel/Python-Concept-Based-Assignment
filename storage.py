"""
Module: storage.py
Handles persistent storage (JSON) and report exporting (CSV).
Includes robust exception handling for file I/O operations.
"""

import json
import csv
import os
from typing import List
from models import Student

class DataStorage:
    """Manages saving and loading student records to disk."""
    def __init__(self, json_path: str = "students_db.json", csv_path: str = "students_export.csv"):
        self.json_path = json_path
        self.csv_path = csv_path

    def save_students(self, students: List[Student]) -> bool:
        """Saves student records to a JSON database file."""
        try:
            data = [s.to_dict() for s in students]
            with open(self.json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            return True
        except IOError as e:
            print(f"[Storage Error] Failed to write to {self.json_path}: {e}")
            return False

    def load_students(self) -> List[Student]:
        """Loads student records from JSON database."""
        if not os.path.exists(self.json_path):
            return []
        try:
            with open(self.json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            students = []
            for item in data:
                s = Student(item["student_id"], item["name"], item.get("department", "CSE-AI&ML"), item.get("division", "SY-A"))
                att_data = item.get("attendance", {})
                s.attendance.total_sessions = att_data.get("total_sessions", 0)
                s.attendance.attended_sessions = att_data.get("attended_sessions", 0)
                s.marks = item.get("marks", {})
                students.append(s)
            return students
        except (IOError, json.JSONDecodeError) as e:
            print(f"[Storage Warning] Could not load database {self.json_path}: {e}")
            return []

    def export_to_csv(self, students: List[Student]) -> bool:
        """Exports student list to a CSV spreadsheet."""
        try:
            with open(self.csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                # Header row
                writer.writerow([
                    "Student ID", "Name", "Department", "Division",
                    "Total Sessions", "Attended Sessions", "Attendance %",
                    "GPA", "Defaulter Status"
                ])
                for s in students:
                    writer.writerow([
                        s.student_id,
                        s.name,
                        s.department,
                        s.division,
                        s.attendance.total_sessions,
                        s.attendance.attended_sessions,
                        f"{s.attendance.percentage}%",
                        s.gpa,
                        s.defaulter_status
                    ])
            return True
        except IOError as e:
            print(f"[Export Error] Failed to export to {self.csv_path}: {e}")
            return False
