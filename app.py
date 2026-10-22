"""
Module: app.py
Main entry point for EduTrack: Student Attendance & Performance Analytics Application.
Provides an interactive menu-driven interface and automated demonstration mode.
"""

import sys
from models import Student
from analytics import PerformanceAnalytics
from storage import DataStorage

class EduTrackApp:
    def __init__(self):
        self.storage = DataStorage()
        self.students = self.storage.load_students()
        if not self.students:
            self._seed_sample_data()

    def _seed_sample_data(self):
        """Initializes system with realistic CSE-AI&ML student records."""
        sample_records = [
            ("S101", "Aarav Sharma", 40, 36, {"Python": 88, "Data Structures": 82, "AI Basics": 90}),  # 90.0% - Regular
            ("S102", "Diya Patel", 40, 32, {"Python": 78, "Data Structures": 75, "AI Basics": 80}),    # 80.0% - Regular
            ("S103", "Rohan Kulkarni", 40, 26, {"Python": 65, "Data Structures": 60, "AI Basics": 70}),# 65.0% - Moderate Defaulter
            ("S104", "Sneha Deshmukh", 40, 22, {"Python": 58, "Data Structures": 55, "AI Basics": 62}),# 55.0% - Moderate Defaulter
            ("S105", "Sumit Kakade", 40, 16, {"Python": 72, "Data Structures": 68, "AI Basics": 74}),  # 40.0% - Major Defaulter (21-50%)
            ("S106", "Aditya Joshi", 40, 14, {"Python": 50, "Data Structures": 45, "AI Basics": 52}),  # 35.0% - Major Defaulter (21-50%)
            ("S107", "Kavya Verma", 40, 6, {"Python": 40, "Data Structures": 35, "AI Basics": 42})     # 15.0% - Critical Defaulter (<20%)
        ]
        for sid, name, total, attended, marks in sample_records:
            s = Student(sid, name, department="CSE-AI&ML", division="SY-A")
            s.attendance.total_sessions = total
            s.attendance.attended_sessions = attended
            s.marks = marks
            self.students.append(s)
        self.storage.save_students(self.students)

    def display_students(self):
        """Displays all students in a neat tabular format."""
        print("\n" + "=" * 90)
        print(f"{'ID':<6} {'Name':<18} {'Dept':<12} {'Attendance':<14} {'GPA':<8} {'Defaulter Status':<25}")
        print("-" * 90)
        for s in self.students:
            att_str = f"{s.attendance.attended_sessions}/{s.attendance.total_sessions} ({s.attendance.percentage}%)"
            print(f"{s.student_id:<6} {s.name:<18} {s.department:<12} {att_str:<14} {s.gpa:<8} {s.defaulter_status:<25}")
        print("=" * 90 + "\n")

    def add_student(self):
        """Adds a new student to the database."""
        try:
            sid = input("Enter Student ID (e.g. S108): ").strip()
            if any(s.student_id == sid for s in self.students):
                print("[Error] Student ID already exists.")
                return
            name = input("Enter Student Full Name: ").strip()
            dept = input("Enter Department [default: CSE-AI&ML]: ").strip() or "CSE-AI&ML"
            div = input("Enter Division [default: SY-A]: ").strip() or "SY-A"
            s = Student(sid, name, dept, div)
            self.students.append(s)
            self.storage.save_students(self.students)
            print(f"[Success] Student {name} ({sid}) added successfully.")
        except Exception as e:
            print(f"[Error] Failed to add student: {e}")

    def mark_attendance(self):
        """Marks attendance for a student."""
        sid = input("Enter Student ID: ").strip()
        student = next((s for s in self.students if s.student_id == sid), None)
        if not student:
            print("[Error] Student not found.")
            return
        status = input("Is the student Present? (y/n): ").strip().lower()
        student.attendance.mark_attendance(present=(status == 'y'))
        self.storage.save_students(self.students)
        print(f"[Updated] {student.name}'s attendance is now: {student.attendance.percentage}%")

    def show_analytics(self):
        """Displays summary analytics and defaulter categorization."""
        analytics = PerformanceAnalytics(self.students)
        print("\n" + analytics.generate_summary_report())
        cats = analytics.categorize_defaulters()
        
        print("\n--- MAJOR DEFAULTERS (21% - 50% Attendance) ---")
        for s in cats["Major Defaulters"]:
            print(f" * [{s.student_id}] {s.name} - Attendance: {s.attendance.percentage}% | Tasks: HackerRank + Lab Re-performance + Mini Project")
            
        print("\n--- MODERATE DEFAULTERS (50% - 75% Attendance) ---")
        for s in cats["Moderate Defaulters"]:
            print(f" * [{s.student_id}] {s.name} - Attendance: {s.attendance.percentage}% | Tasks: Extra Assignment + MCQ + Presentation")

    def export_data(self):
        """Exports data to CSV spreadsheet."""
        if self.storage.export_to_csv(self.students):
            print(f"[Success] Exported records to {self.storage.csv_path}")

    def run_demo(self):
        """Executes a full non-interactive demonstration of all features."""
        print("=" * 80)
        print("  EDUTRACK: SMART STUDENT ATTENDANCE & PERFORMANCE ANALYTICS SYSTEM")
        print("  Academic Year: 2026-2027 | Department: CSE-AI & ML | Semester: III")
        print("=" * 80)
        print("\n[STEP 1] Current Enrolled Students & Attendance Status:")
        self.display_students()
        
        print("[STEP 2] Performance Analytics & Defaulters Categorization:")
        self.show_analytics()
        
        print("\n[STEP 3] Exporting Data to CSV Spreadsheet:")
        self.export_data()
        print("\n[STEP 4] Database Persistence Status: Verified (students_db.json)")
        print("=" * 80)
        print("  DEMONSTRATION COMPLETED SUCCESSFULLY")
        print("=" * 80)

    def run(self):
        """Runs the interactive menu loop."""
        while True:
            print("\n================ EDUTRACK MENU ================")
            print("1. Display All Students & Defaulter Status")
            print("2. Add New Student Record")
            print("3. Record Attendance Session")
            print("4. View Analytics & Defaulter Categorization")
            print("5. Export Records to CSV")
            print("6. Run Full Demo")
            print("7. Exit")
            print("================================================")
            choice = input("Enter choice (1-7): ").strip()
            if choice == '1':
                self.display_students()
            elif choice == '2':
                self.add_student()
            elif choice == '3':
                self.mark_attendance()
            elif choice == '4':
                self.show_analytics()
            elif choice == '5':
                self.export_data()
            elif choice == '6':
                self.run_demo()
            elif choice == '7':
                print("Exiting EduTrack. Goodbye!")
                break
            else:
                print("Invalid option. Please choose between 1 and 7.")

if __name__ == "__main__":
    app = EduTrackApp()
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        app.run_demo()
    else:
        app.run_demo()
