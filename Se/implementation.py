from typing import List

# --- SUBJECT CLASS ---
class Subject:
    def __init__(self, code: str, name: str):
        self.code: str = code
        self.name: str = name
        self.course_teacher: 'Teacher' = None  # Assigned teacher


# --- GRADE CLASS ---
class Grade:
    def __init__(self, subject: Subject, score: float):
        self.subject: Subject = subject
        self.score: float = score


# --- TEACHER CLASS ---
class Teacher:
    def __init__(self, teacher_id: int, name: str):
        self.teacher_id: int = teacher_id
        self.name: str = name
        self.taught_subjects: List[Subject] = []  # Subjects taught by the teacher

    def assign_subject(self, subject: Subject):
        """Assigns a subject to the teacher and updates the subject's teacher info."""
        if subject not in self.taught_subjects:
            self.taught_subjects.append(subject)
            subject.course_teacher = self


# --- STUDENT CLASS ---
class Student:
    def __init__(self, student_id: int, name: str):
        self.student_id: int = student_id
        self.name: str = name
        self.enrolled_subjects: List[Subject] = []  # Subjects the student is enrolled in
        self.grades: List[Grade] = []  # Grades received by the student (Composition)

    def enroll(self, subject: Subject):
        """Enrolls the student in a subject."""
        if subject not in self.enrolled_subjects:
            self.enrolled_subjects.append(subject)
            print(f"[Enrollment] {self.name} has successfully enrolled in the '{subject.name}' subject.")

    def add_grade(self, subject: Subject, score: float):
        """Adds a grade to the student only if they are enrolled in the subject."""
        if subject in self.enrolled_subjects:
            new_grade = Grade(subject, score)
            self.grades.append(new_grade)
            print(f"[Grade Entry] {self.name} -> '{subject.name}': {score}")
        else:
            print(f"[ERROR] A grade cannot be added because {self.name} is not enrolled in the '{subject.name}' subject!")

    def print_transcript(self):
        """Prints the student's transcript."""
        print(f"\n===== {self.name} (ID: {self.student_id}) TRANSCRIPT =====")
        if not self.grades:
            print("No grades have been entered yet.")
        for grade in self.grades:
            print(f"- Subject: {grade.subject.name} [{grade.subject.code}] | Grade: {grade.score}")
        print("============================================")


# --- EXAMPLE USAGE (Test) ---
if __name__ == "__main__":
    # Object creation
    teacher1 = Teacher(101, "Ahmet Yilmaz")
    subject1 = Subject("MAT101", "Mathematics")
    subject2 = Subject("PHY101", "Physics")
    student1 = Student(2021001, "Ali Demir")

    # Assigning subjects to the teacher
    teacher1.assign_subject(subject1)
    teacher1.assign_subject(subject2)

    # Student operations
    student1.enroll(subject1)  # Enrolls in Mathematics
    
    student1.add_grade(subject1, 85.5)  # Successful grade entry
    student1.add_grade(subject2, 90.0)  # Failed grade entry (Not enrolled in Physics)

    # Print transcript
    student1.print_transcript()