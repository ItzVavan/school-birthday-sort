def filter_by_season(students: list, season: str) -> list:
    """Фильтр по сезону рождения"""
    season = season.lower()
    
    if season == "зима":
        months = {12, 1, 2}
    elif season == "весна":
        months = {3, 4, 5}
    elif season == "лето":
        months = {6, 7, 8}
    elif season == "осень":
        months = {9, 10, 11}
    else:
        months = set()
    
    return [student for student in students if student.month in months]

def filter_by_grade_num(students: list, grade_num: int) -> list:
    """Фильтр по номеру класса"""
    return [student for student in students if student.grade_num == grade_num]
