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
                ui.get_inputs('\nPress ENTER to continue')
                ui.clear()
        except KeyError as err:
            ui.clear()
            ui.print_error(str(err))

def Show_menu():
    options = ["Create Application",
                "Update Application",
                "Delete Application",
                "Read Applications"
                ]
    ui.print_menu("Application menu", options, "Back to main menu")

def choose():
    myfile = "application/applications.txt"
    option = ui.get_inputs("\nPlease enter a number: ")
    table = data_manager.imports_from_file(myfile)
    if option == "1":
        ui.clear()
        pos_name = ui.get_inputs("Enter a position name to apply: ")
        positions = data_manager.imports_from_file("position/positions.txt")
        student_id = ui.get_inputs("Enter a student id to apply: ")
        students = data_manager.imports_from_file("student/students.txt")
        opt = ui.get_inputs("Enter the status(applied/not applied): ")
        if common.check_valid_id(positions, pos_name) == False or common.check_valid_id(students, student_id) == False:
            ui.clear()
            ui.print_error("Non existing position or student!")
        else:
            if opt != "applied" and opt != "not applied":
                ui.clear()
                ui.print_error("Thats not an option")
            else:    
                data_manager.export_to_file(myfile, create_applicaion(table, opt, pos_name, student_id, positions))
    elif option == "2":##Update Applications
        ui.clear()
        idx = ui.get_inputs("Enter application ID: ")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid application ID! ('{idx}')")
            return True
        else:
            if common.check_if_applied(table, idx) == True:
                ui.clear()
                ui.print_error("You cant modify not applied status")
            else:
                for row in table:
                    if row[0] == idx:
                        row[1] = "not applied"
                data_manager.export_to_file(myfile, table)
    elif option == "3":
        ui.clear()
        idx = ui.get_inputs("Enter application ID: ")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid application ID! ('{idx}')")
        else:
            data_manager.export_to_file(myfile, common.delete_element(table, idx))
    elif option == "4":
        ui.clear()
        result = common.read_elements(table)
        if len(result) == 0:
            ui.clear()
            ui.print_error("There are no application in this list!")
        else:
            show_table(result)
    elif option == "0":
        ui.clear()
        return False
    else:
        raise KeyError(f"There is no such option. ({option})")
    return True

def create_applicaion(table, opt, pos_name, student_id, positions):
    pos_id = -1
    for row in positions:
        if row[1] == pos_name:
            pos_id = row[0]
    
    idx = ""
    
    while True:
        idx = common.generate_random()
        if common.check_valid_id(table, idx) == False:
            break
    
    ops = []
    ops.append(idx)
    ops.append(opt)
    temp = []
    for i in ops:
        temp.append(i)
    temp.append(student_id)
    temp.append(pos_id)
    kakao = []
    kakao.extend(temp)
    table.append(kakao)
    return table

def show_table(table):
    titles = ["Application_id", "Status","Student_id", "Positon_id" ]
    ui.print_table(table, titles)