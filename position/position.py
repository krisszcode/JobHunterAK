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
    options = ["Create Position",
                "Read Position",
                "Read Positions",
                "Update Position",
                "Delete Student"
                ]
    ui.print_menu("Position menu", options, "Back to main menu")

def choose():
    myfile = "position/positions.txt"
    option = ui.get_inputs("\nPlease enter a number: ")
    table = data_manager.imports_from_file(myfile)
    if option == "1":
        ui.clear()
        data_manager.export_to_file(myfile, create_position(table))
    elif option == "2":
        # ++
        ui.clear()
        idx = ui.get_inputs("Enter the position ID: ")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid position ID! ('{idx}')")
        else:
            ui.print_result(read_position(table, idx), "Position details")
    elif option == "3":
        # ++
        ui.clear()
        result = common.read_elements(table)
        if len(result) == 0:
            ui.clear()
            ui.print_error("There are no positions in this list!")
        else:
            show_table(result)
    elif option == "4":
        ui.clear()
        idx = ui.get_inputs("Enter position ID: ")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid position ID! ('{idx}')")
        else:
            data_manager.export_to_file(myfile, update_position(table, idx, "description", ui.get_inputs("Enter the new value of the description.\n")))
    elif option == "5":
        # ++
        ui.clear()
        idx = ui.get_inputs("Enter position ID: ")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid position ID! ('{idx}')")
        else:
            data_manager.export_to_file(myfile, common.delete_element(table, idx))
    elif option == "0":
        ui.clear()
        return False
    else:
        raise KeyError(f"There is no such option. ({option})")
    return True

def create_position(table):
    options = [
                "Enter a description: ",
                "Enter the number of seats: ",
                "Enter the company name: "
                ]

    table.append(common.create_element(table, options))
    table[-1][-1] = get_company_data(data_manager.imports_from_file("company/companies.txt"), table[-1][-1], "id")
    return table

def read_position(table, idx):
    options = ["ID", "Description", "Seats", "Company"]
    mydict = common.read_element(table, idx, options)
    mydict["Company"] = get_company_data(data_manager.imports_from_file("company/companies.txt"), mydict["Company"], "name")
    return mydict

def get_company_data(table, idx, data):
    index = -1
    if data == "id":
        index = 0
    elif data == "name":
        index = 1

    for company in table:
        if idx in company:
            return company[index]

def update_position(table, idx, att, new_att):
    return common.update_element(table, idx, att, new_att, {"description": 1})

def show_table(table):
    titles = ["ID", "DESCRIPTION", "SEATS", "COMPANY_ID"]
    ui.print_table(table, titles)