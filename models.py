def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month: int, year: int) -> int:
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year): return 29
    return days[month]

def is_valid_date(day: int, month: int, year: int) -> bool:
    return 1 <= month <= 12 and 1 <= day <= days_in_month(month, year)

def is_valid_grade(grade_num: int) -> bool:
    """Только 8-11 классы"""
    return 8 <= grade_num <= 11

def check_data_errors(students: list['Student']) -> list[str]:
    """Ошибки данных ['Иванов: дата 32.04.2005', 'Петров: класс 7']"""
    errors = []
    for s in students:
        if not is_valid_date(s.day, s.month, s.year):
            errors.append(f"{s.surname} дата {s.day:02d}.{s.month:02d}.{s.year}")
        if not is_valid_grade(s.grade_num):
            errors.append(f"{s.surname} класс {s.grade_num}")
    return errors

class Student:
    """Класс для представления ученика школы"""
    def __init__(self, surname, name, day, month, year, grade_num, grade_letter):
        self.surname = surname
        self.name = name
        self.day = day
        self.month = month
        self.year = year
        self.grade_num = grade_num
        self.grade_letter = grade_letter

STUDENTS = [
    Student("Иванов", "Пётр", 5, 12, 2008, 8, "А"),
    Student("Петров", "Алексей", 14, 1, 2008, 8, "А"),
    Student("Сидорова", "Мария", 23, 2, 2008, 8, "Б"),
    Student("Кузнецов", "Илья", 30, 3, 2008, 8, "Б"),
    Student("Алексеева", "Дарья", 11, 4, 2008, 8, "В"),
    Student("Борисов", "Никита", 2, 12, 2007, 9, "А"),
    Student("Громова", "Анна", 19, 1, 2007, 9, "А"),
    Student("Денисов", "Степан", 27, 2, 2007, 9, "Б"),
    Student("Егорова", "Ольга", 7, 3, 2007, 9, "Б"),
    Student("Жуков", "Роман", 15, 4, 2007, 9, "В"),
    Student("Зайцев", "Кирилл", 9, 12, 2006, 10, "А"),
    Student("Ильина", "Софья", 21, 1, 2006, 10, "А"),
    Student("Ковалёв", "Артур", 3, 2, 2006, 10, "Б"),
    Student("Леонова", "Елена", 18, 3, 2006, 10, "Б"),
    Student("Морозов", "Дмитрий", 26, 4, 2006, 10, "В"),
    Student("Николаева", "Вера", 1, 12, 2005, 11, "А"),
    Student("Орлов", "Павел", 12, 1, 2005, 11, "А"),
    Student("Павлова", "Полина", 20, 2, 2005, 11, "Б"),
    Student("Романов", "Егор", 28, 3, 2005, 11, "Б"),
    Student("Смирнова", "Алёна", 6, 4, 2005, 11, "В"),
    Student("Абрамов", "Владимир", 5, 12, 2008, 8, "А"),
    Student("Яковлева", "Лидия", 14, 5, 2007, 9, "А"),
    Student("Фёдоров", "Матвей", 23, 2, 2006, 10, "Б"),
    Student("Чернова", "Инга", 30, 3, 2005, 11, "В"),
    Student("Голубев", "Савелий", 11, 4, 2008, 8, "В"),
]
