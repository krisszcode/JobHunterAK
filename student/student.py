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
        data_manager.export_to_file(myfile, create_student(table))

    elif option == "2":
        ui.clear()
        idx = ui.get_input("Enter the student ID: ")
        result = read_student(table, idx)
        if len(result) == 0:
            ui.clear()
            ui.print_error(f"Invalid student ID! ({idx})")
        else:
            ui.print_result(result, "Student details")

    elif option == "3":
        ui.clear()
        idx = ui.get_inputs(["Enter the item index: "], "")
        data_manager.write_table_to_file("store/games.csv", remove(table, idx))
    elif option == "4":
        ui.clear()
        idx = ui.get_inputs(["Enter the item index: "], "")
        update(table, idx[0])
    elif option == "5":
        ui.clear()
        my_dict = get_counts_by_manufacturers(table)
        ui.print_result(my_dict, "Count of manufacturer")
    elif option == "6":
        ui.clear()
        idx = ui.get_inputs(["Enter a manufacturer: "], "")
        number = get_average_by_manufacturer(table, idx[0])
        ui.clear()
        ui.print_result(number, "Average of manufacturer")
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option.")
    return True

def show_table(table):
    ui.clear()
    titles = ["ID", "NAME", "AGE", "ACTIVE"]
    ui.print_table(table, titles)

def create_student(table):
    ui.clear()
    mylist = []
    options = [
                "Enter student name: ",
                "Enter student age: ",
                "Enter student activation status: "]

    mylist.append(common.generate_random())
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