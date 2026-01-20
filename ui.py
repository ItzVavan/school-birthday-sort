def print_student_title(title: str, students: list):
    """Печатает заголовок и форматированный список учеников"""
    if not students:
        print(f"{title} - нет учеников")
        return
    print(title)
    
    print("-" * len(title))
    
    for student in students:
        date_str = f"{student.day:02d}.{student.month:02d}.{student.year}"
        class_str = f"{student.grade_num}{student.grade_letter}"
        print(f"{student.surname} {student.name}, {date_str} - {class_str}")
    
    print()

