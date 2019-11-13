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
    options = ["Create Application",
                "Update Application",
                "Delete Application"
                ]
    ui.print_menu("Application menu", options, "Back to main menu")

def choose():
    myfile = "application/applications.txt"
    option = ui.get_input("\nPlease enter a number: ")
    table = data_manager.imports_from_file(myfile)
    if option == "1":
        ui.clear()
        data_manager.export_to_file(myfile, create_applicaion(table))
    elif option == "2":
        ui.clear()
        idx = ui.get_input("Enter the student ID: ")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid student ID! ('{idx}')")
        else:
            ui.print_result(read_student(table, idx), "Student details")
    elif option == "3":
        pass

def create_company(table):
    
    options = ["Enter the application status: "]
    table.append(common.create_element(table, options))
    return table