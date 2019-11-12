import ui
import common
import data_manager

def start_module():
    ui.clear()
    while True:
        Show_menu()
        try:
            if not choose():
                break
            else:
                ui.get_input('\nPress ENTER to continue')
                ui.clear()
        except KeyError as err:
            ui.clear()
            ui.print_error(str(err))

def Show_menu():
    options = ["Create Position",
                "Read Position",
                "Read Positions",
                "Update Position",
                "Delete Student"
                ]
    ui.print_menu("Position menu", options, "Back to main menu")

def choose():
    myfile = "position/positions.txt"
    option = ui.get_input("\nPlease enter a number: ")
    table = data_manager.imports_from_file(myfile)
    if option == "1":
        print()
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option.")
    return True