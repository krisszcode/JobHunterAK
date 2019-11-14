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
    options = ["Create Student",
                "Read Student",
                "Read Students",
                "Update Student",
                "Activated/Deactive Student",
                "Delete Student"
                ]
    ui.print_menu("Student menu", options, "Back to main menu")

def choose():
    myfile = "student/students.txt"
    option = ui.get_inputs("\nPlease enter a number: ")
    table = data_manager.imports_from_file(myfile)
    if option == "1":
        ui.clear()
        data_manager.export_to_file(myfile, create_student(table))
    elif option == "2":
        ui.clear()
        idx = ui.get_inputs("Enter the student ID: ")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid student ID! ('{idx}')")
        else:
            result = get_student_applications(idx, read_student(table, idx))
            ui.print_result(result, "Student details")
    elif option == "3":
        ui.clear()
        result = read_students(table)
        if len(result) == 0:
            ui.clear()
            ui.print_error("There are no students in this list!")
        else:
            show_table(result)
    elif option == "4":
        ui.clear()
        attributes = ["name", "age", "status"]
        idx = ui.get_inputs("Enter student ID: ")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid student ID! ('{idx}')")
            return True
        update = ui.get_inputs("Which attribute do you want to change?\n")
        update = update.lower()
        if update not in attributes:
            ui.clear()
            ui.print_error(f"You cannot change this attribute! ('{update}')")
        else:
            data_manager.export_to_file(myfile, update_student(table, idx, update, ui.get_inputs(f"Enter the new value of the {update}.\n")))
    elif option == "5":
        ui.clear()
        idx = ui.get_inputs("Enter student ID: ")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid student ID! ('{idx}')")
        else:
            data_manager.export_to_file(myfile, update_student(table, idx, "status", get_new_status(table, idx)))
    elif option == "6":
        ui.clear()
        idx = ui.get_inputs("Enter student ID: ")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid student ID! ('{idx}')")
            return True
            
        if check_student_app(idx) == True:
            ui.clear()
            ui.print_error("You cannot delete this student!")
        else:
            data_manager.export_to_file(myfile, common.delete_element(table, idx))
    elif option == "0":
        ui.clear()
        return False
    else:
        raise KeyError(f"There is no such option. ({option})")
    return True

def create_student(table):
    options = [
                "Enter student name: ",
                "Enter student age: ",
                "Enter student activation status: "
                ]

    table.append(common.create_element(table, options))
    return table

def read_student(table, idx):
    options = ["ID", "Name", "Age", "Activation status"]
    return common.read_element(table, idx, options)

def read_students(table):
    mylist = []
    temp = common.read_elements(table)
    for n, student in enumerate(temp):
        mylist.append([])
        for i in range(len(student)):
            if i <= 1:
                mylist[n].append(student[i])
    return mylist

def update_student(table, idx, att, new_att):
    attributes = {"name": 1, "age": 2, "status": 3}
    return common.update_element(table, idx, att, new_att, attributes)

def get_new_status(table, idx):
    for student in table:
        if student[0] == idx:
            if student[-1] == "active":
                return "deactive"
            elif student[-1] == "deactive":
                return "active"

def show_table(table):
    titles = ["ID", "NAME"]
    ui.print_table(table, titles)

def get_student_applications(idx, mydict):
    applications = data_manager.imports_from_file("application/applications.txt")
    options = ["Application ID","Status","Position"]
    title = ""
    app_count = 0

    for i, item in enumerate(applications):
        if item[2] == idx:
            app_count += 1
            for n in range(len(item)):
                if n < 3:
                    title = f"{app_count}_{options[n]}"
                else:
                    continue

                if n == 2:
                    mydict.update({title: get_position_by_id(item[-1])})
                    mydict.update({f"{app_count}_Company": get_company_name_by_pid(item[-1])})
                else:
                    mydict.update({title: item[n]})

    return mydict

def get_position_by_id(idx):
    positions = data_manager.imports_from_file("position/positions.txt")

    for position in positions:
        if position[0] == idx:
            return position[1]

def get_company_name_by_pid(idx):
    positions = data_manager.imports_from_file("position/positions.txt")
    c_id = -1

    for position in positions:
        if position[0] == idx:
            c_id = position[3]
            break

    companies = data_manager.imports_from_file("company/companies.txt")

    for company in companies:
        if company[0] == c_id:
            return company[1]

def check_student_app(idx):
    applications = data_manager.imports_from_file("application/applications.txt")

    for item in applications:
        if item[-2] == idx:
            return True
    
    return False