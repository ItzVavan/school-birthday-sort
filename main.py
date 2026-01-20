from filters import filter_by_grade_num, filter_by_season
from models import STUDENTS, check_data_errors
from sorting import compare_by_date, compare_full, insertion_sort
from ui import print_student_title

def check_dates():
    clear_screen()
    errors = check_data_errors(STUDENTS)
    if not errors:
        print("Все даты корректны!")
    else:
        print("Ошибки в следущих датах")
        for err in errors:
            print(f"- {err}")
    print(f"Всего ошибок {len(errors)}")
    wait_till_enter()

def wait_till_enter():
    while True:
        input("Нажмите Enter для продолжения")
        break

def clear_screen():
    print("\033c", end="")

def input_int(prompt: str, min_value: int = None, max_value: int = None) -> int:
    """Безопасный ввод числа с проверкой диапазона"""
    while True:
        raw = input(prompt)

        try:
            value = int(raw)
        except ValueError:
            print("Ошибка! Введите число")
            continue

        if min_value is not None and value < min_value:
            print(f"Минимальное значение {min_value}")
            continue

        if max_value is not None and value > max_value:
            print(f"Максимальное значение {max_value}")
            continue

        return value

def input_season() -> str:
    seasons = {"1": "зима", "2": "весна", "3": "лето", "4": "осень"}
    print("1. Зима")
    print("2. Весна")
    print("3. Лето")
    print("4. Осень")
    
    while True:
        choice = input("Выбор: ").strip()
        if choice in seasons:
            return seasons[choice]
        print("Неверный выбор!")

def show_full_list(students: list):
    """Полный список, отсортированный по классу/фамилии"""
    clear_screen()
    
    copy_list = students.copy()
    insertion_sort(copy_list, compare_full)
    
    print_student_title("Полный список учеников", copy_list)
    
    wait_till_enter()

def show_season_list(students: list):
    """Список по временам года сортировка по дате"""
    clear_screen()
    
    season = input_season()
    filtered = filter_by_season(students, season)
    insertion_sort(filtered, compare_by_date)
    
    season_names = {"зима": "Зима", "весна": "Весна", "лето": "Лето", "осень": "Осень"}
    title = f"Ученики {season_names.get(season, season)}"
    print_student_title(title, filtered)
    
    wait_till_enter()

def show_grade_list(students: list):
    """Список по параллели (8-11), сортировка по дате"""
    clear_screen()
    
    grade_num = input_int("Класс (8-11): ", min_value=8, max_value=11)
    filtered = filter_by_grade_num(students, grade_num)
    insertion_sort(filtered, compare_by_date)
    
    title = f"Ученики {grade_num} класса"
    print_student_title(title, filtered)
    
    wait_till_enter()

def main_menu():
    clear_screen()
    errors = check_data_errors(STUDENTS)
    
    if errors:
        print("ОШИБКИ В ДАННЫХ (программа остановлена)")
        for err in errors:
            print(f"- {err}")
        print(f"Всего ошибок {len(errors)}")
    else:
        print("Все данные корректны!")
    
    wait_till_enter()
    
    if errors:
        print("Работа остановлена из-за ошибок")
        return
    
    students = STUDENTS
    
    while True:
        clear_screen()
        
        print("1. Полный список")
        print("2. Список по времени года")
        print("3. Список по классу")
        print("0. Выход")
        
        choice = input("Выбор ").strip()
        
        if choice == "1":
            show_full_list(students)
        elif choice == "2":
            show_season_list(students)
        elif choice == "3":
            show_grade_list(students)
        elif choice == "0":
            print("До свидания!")
            break
        else:
            input("Ошибка! Нажмите Enter ")

if __name__ == "__main__":
    main_menu()
