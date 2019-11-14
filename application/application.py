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
                "Delete Application"
                ]
    ui.print_menu("Application menu", options, "Back to main menu")

def choose():
    myfile = "application/applications.txt"
    option = ui.get_inputs("\nPlease enter a number: ")
    table = data_manager.imports_from_file(myfile)
    if option == "1":
        ui.clear()
        companies = data_manager.imports_from_file("company/companies.txt")
        comp_name = ui.get_inputs("Enter a company name to apply: ")
        positions = data_manager.imports_from_file("position/positions.txt")
        student_id = ui.get_inputs("Enter a student id to apply: ")
        students = data_manager.imports_from_file("student/students.txt")
        opt = ui.get_inputs("Enter the status(applied/not applied): ")
        if common.check_valid_id(companies, comp_name) == False or common.check_valid_id(students, student_id) == False:
            ui.clear()
            ui.print_error("Non existing company or student!")
        else:
            if opt != "applied" and opt != "not applied":
                ui.clear()
                ui.print_error("Thats not an option")
            else:    
                data_manager.export_to_file(myfile, create_applicaion(table, opt, comp_name, student_id, companies))
    elif option == "2":##Update Applications
        '''
        ui.clear()
        idx = ui.get_inputs("Enter application ID: ")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid application ID! ('{idx}')")
            return True
        else:
            if check_if_applied(table, idx) == False:
                ui.clear()
                ui.print_error("You cant modify not accepted status")
            else:
                data_manager.export_to_file
        '''
    elif option == "3":
        pass
    elif option == "0":
        ui.clear()
        return False
    else:
        raise KeyError(f"There is no such option. ({option})")
    return True

def create_applicaion(table, opt, comp_name, student_id, companies):
    comp_id = -1
    for row in companies:
        if row[1] == comp_name:
            comp_id = row[0]
    
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
    temp.append(comp_id)
    kakao = []
    kakao.extend(temp)
    table.append(kakao)
    return table

def update_application(table, idx, att, new_att):
    return common.update_element(table, idx, att, new_att, {"name": 1})