def insertion_sort(students, comparator):
    """Сортировка вставками по заданному компаратору для списка студентов"""
    
    for i in range(1, len(students)):
        key_student = students[i]
        j = i - 1
        
        while j >= 0 and comparator(students[j], key_student) > 0:
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = key_student

def compare_full(a, b):
    """Сравнение класс -> фамилия -> имя"""
    if a.grade_num != b.grade_num:
        return a.grade_num - b.grade_num
    
    if a.grade_letter != b.grade_letter:
        return ord(a.grade_letter) - ord(b.grade_letter)
    
    if a.surname != b.surname:
        return -1 if a.surname < b.surname else 1
    
    if a.name != b.name:
        return -1 if a.name < b.name else 1
    
    return 0

def compare_by_date(a, b):
    """Сравнение месяц -> день -> фамилия -> имя"""
    
    if a.month != b.month:
        return a.month - b.month
    
    if a.day != b.day:
        return a.day - b.day
    
    if a.surname != b.surname:
        return -1 if a.surname < b.surname else 1
    
    if a.name != b.name:
        return -1 if a.name < b.name else 1
    
    return 0
