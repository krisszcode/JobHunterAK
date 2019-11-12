import sys
import ui
import data_manager
from student import student

def choose():
    option = ui.get_input("\nPlease enter a number: ")
    if option == "1":
        student.start_module()
    elif option == "2":
        print()
    elif option == "3":
        print()
    elif option == "4":
        print()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")

def handle_menu():
    options = ["Student",
               "Company",
               "Position",
               "Application"]

    ui.print_menu("Main menu", options, "Exit")

def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error(str(err))

if __name__ == '__main__':
    main()