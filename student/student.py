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
    option = ui.get_input("\nPlease enter a number: ")
    table = data_manager.imports_from_file(myfile)
    if option == "1":
        ui.clear()
        data_manager.export_to_file(myfile, create_student(table))
    elif option == "2":
        ui.clear()
        idx = ui.get_input("Enter the student ID: ")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid student ID! ('{idx}')")
        else:
            ui.print_result(read_student(table, idx), "Student details")
    elif option == "3":
        ui.clear()
        result = read_students(table)
        if len(result) == 0:
            ui.clear()
            ui.print_error("There are no students in this list!")
        else:
            ui.print_result(result, "Students list")
    elif option == "4":
        ui.clear()
        attributes = ["name", "age", "status"]
        idx = ui.get_input("Enter student ID: ")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid student ID! ('{idx}')")
            return True
        update = ui.get_input("Which attribute do you want to change?\n")
        update = update.lower()
        if update not in attributes:
            ui.clear()
            ui.print_error(f"You cannot change this attribute! ('{update}')")
        else:
            data_manager.export_to_file(myfile, update_student(table, idx, update, ui.get_input(f"Enter the new value of the {update}.\n")))
    elif option == "5":
        ui.clear()
        idx = ui.get_input("Enter student ID: ")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid student ID! ('{idx}')")
        else:
            data_manager.export_to_file(myfile, update_student(table, idx, "status", get_new_status(table, idx)))
    elif option == "6":
        ui.clear()
        idx = ui.get_input("Enter student ID: ")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid student ID! ('{idx}')")
        else:
            data_manager.export_to_file(myfile, delete_student(table, idx))
    elif option == "0":
        return False
    else:
        raise KeyError(f"There is no such option. ({option})")
    return True

def show_table(table):
    ui.clear()
    titles = ["ID", "NAME", "AGE", "ACTIVE"]
    ui.print_table(table, titles)

def create_student(table):
    mylist = []
    options = [
                "Enter student name: ",
                "Enter student age: ",
                "Enter student activation status: "]

    idx = ""
    while True:
        idx = common.generate_random()
        if common.check_valid_id(table, idx) == False:
            break

    mylist.append(idx)
    for i in range(len(options)):
        mylist.append(ui.get_input(options[i]))

    table.append(mylist)
    
    return table

def read_student(table, idx):
    mydict = {}
    options = ["ID", "Name", "Age", "Activation status"]
    for student in table:
        if idx == student[0]:
            for i, item in enumerate(student):
                mydict.update({options[i]: item})

    return mydict

def read_students(table):
    mylist = []
    for i, student in enumerate(table):
        mylist.append([])
        for n in range(len(student)):
            if n <= 1:
                mylist[i].append(student[n])
    return mylist

def update_student(table, idx, att, new_att):
    attributes = {"name": 1, "age": 2, "status": 3}
    for i in range(len(table)):
        student = table[i]
        if student[0] == idx:
            for n in range(len(student)):
                if n == attributes[att]:
                    table[i][n] = new_att
    return table

def get_new_status(table, idx):
    for student in table:
        if student[0] == idx:
            if student[-1] == "active":
                return "deactive"
            elif student[-1] == "deactive":
                return "active"

def delete_student(table, idx):
    for i, student in enumerate(table):
        if idx in student:
            del table[i]
            return table