menu = """
========= Menu =========
1. Task qo'shish
2. Tasklarni ko'rish
3. Taskni o'chirish
4. Taskni yangilash
5. Chiqish
"""
todos: list[str] = []


def print_menu() -> None:
    print(menu)


def add_task() -> None:

    print("========= Task qo'shish =========")
    task = input("Task kiriting: ").strip().capitalize()
    if task in todos:
        print("Bu taskni avval kiritgansiz")
    else:
        todos.append(task)
        print("Task qo'shildi✅")
              

def print_todos() -> None:
    print("========= Barcha Tasklar =========")
    for index, todo in enumerate(todos, start=1):
        print(f"{index}. {todo}")


def delete_task() -> None:
    print_todos()
    index = int(input("O'chirmoqchi bo'lgan task raqamini kiriting: "))
    if index != int:
        if 1 <= index <= len(todos):
            deleted = todos.pop(index - 1)
            print(f"✅ '{deleted}' o'chirildi.")
        else:
            print("Xato raqam.")
    else:
        print("Iltimos, faqat raqam kiriting.")


def update_task() -> None:
    print_todos()
    index = int(input("Qaysi taskni yangilamoqchisiz? Raqamini kiriting: "))
    if index != int:
        if 1 <= index <= len(todos):
            new_task = input("Yangi task kiriting: ").strip().capitalize()
            if new_task in todos:
                print("❗ Bu task allaqachon mavjud.")
            else:
                old_task = todos[index - 1]
                todos[index - 1] = new_task
                print(f"'{old_task}' -> '{new_task}' ga yangilandi.")
        else:
            print("Noto'g'ri raqam.")
    else:
        print("Iltimos, faqat raqam kiriting.")


def main() -> None:
    while True:
        print_menu()
        choice = input("Menu tanlang: ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            print_todos()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            update_task()
        elif choice == '5':
            confirm = input("Chiqishni xohlaysizmi? (ha/yo'q): ").strip().lower()
            if confirm in ('ha', 'h'):
                print("👋 Dasturdan chiqildi.")
                break
        else:
            print("Noto'g'ri menu tanlandi.")

main()