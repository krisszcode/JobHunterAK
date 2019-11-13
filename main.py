import sys
import ui
import data_manager
from student import student
from position import position
from company import company

def choose():
    option = ui.get_input("\nPlease enter a number: ")
    if option == "1":
        student.start_module()
    elif option == "2":
        company.start_module()
    elif option == "3":
        position.start_module()
    elif option == "4":
        print()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError(f"There is no such option. ({option})")

def handle_menu():
    options = ["Student",
               "Company",
               "Position",
               "Application"]

    ui.print_menu("Main menu", options, "Exit")

def main():
    ui.clear()
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.clear()
            ui.print_error(str(err))

if __name__ == '__main__':
    main()