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
    pass


def print_todos() -> None:
    pass


def delete_task() -> None:
    pass


def update_task() -> None:
    pass


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
            print("❌ Noto‘g‘ri menu tanlandi.")

main()
