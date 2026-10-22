"""
Module: analytics.py
Provides analytical and reporting capabilities for the EduTrack system.
"""

from typing import List, Dict
from models import Student

class PerformanceAnalytics:
    """Analyzes student attendance and academic performance metrics."""
    def __init__(self, students: List[Student]):
        self.students = students

    def get_class_average_attendance(self) -> float:
        """Calculates the overall class average attendance percentage."""
        if not self.students:
            return 0.0
        total_pct = sum(s.attendance.percentage for s in self.students)
        return round(total_pct / len(self.students), 2)

    def get_class_average_gpa(self) -> float:
        """Calculates the overall class average GPA."""
        if not self.students:
            return 0.0
        total_gpa = sum(s.gpa for s in self.students)
        return round(total_gpa / len(self.students), 2)

    def categorize_defaulters(self) -> Dict[str, List[Student]]:
        """Categorizes all students into their respective attendance brackets."""
        categories = {
            "Critical Defaulters": [],
            "Major Defaulters": [],
            "Moderate Defaulters": [],
            "Eligible": []
        }
        for s in self.students:
            pct = s.attendance.percentage
            if pct < 20.0:
                categories["Critical Defaulters"].append(s)
            elif 20.0 <= pct <= 50.0:
                categories["Major Defaulters"].append(s)
            elif 50.0 < pct < 75.0:
                categories["Moderate Defaulters"].append(s)
            else:
                categories["Eligible"].append(s)
        return categories

    def generate_summary_report(self) -> str:
        """Generates a structured text report of the analytics."""
        cats = self.categorize_defaulters()
        lines = [
            "=" * 72,
            "          EDUTRACK STUDENT PERFORMANCE & DEFAULTER REPORT          ",
            "=" * 72,
            f"Total Students Enrolled: {len(self.students)}",
            f"Class Average Attendance: {self.get_class_average_attendance()}%",
            f"Class Average GPA:        {self.get_class_average_gpa()} / 10.0",
            "-" * 72,
            f"Eligible Students (>= 75%):       {len(cats['Eligible'])}",
            f"Moderate Defaulters (50% - 75%):   {len(cats['Moderate Defaulters'])}",
            f"Major Defaulters (21% - 50%):      {len(cats['Major Defaulters'])}",
            f"Critical Defaulters (< 20%):       {len(cats['Critical Defaulters'])}",
            "=" * 72
        ]
        return "\n".join(lines)
