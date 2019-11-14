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
    options = ["Create Company",
                "Read Company",
                "Read Companies",
                "Update Company",
                "Delete Company"
                ]
    ui.print_menu("Company menu", options, "Back to main menu")

def choose():
    myfile = "company/companies.txt"
    option = ui.get_inputs("\nPlease enter a number: ")
    table = data_manager.imports_from_file(myfile)
    if option == "1":##Create company
        ui.clear()
        data_manager.export_to_file(myfile, create_company(table))
    elif option == "2":##Read company
        ui.clear()
        idx = ui.get_inputs("Enter the company ID: ")
        positions = data_manager.imports_from_file("position/positions.txt")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid company ID! ('{idx}')")
        else:
            ui.print_result(read_company(table, idx), "Company details")
            ui.print_result_with_one_print(positions_by_companies(idx, positions), "Open positions")
    elif option == "3":##Read Companies
        ui.clear()
        result = common.read_elements(table)
        if len(result) == 0:
            ui.clear()
            ui.print_error("There are no company in this list!")
        else:
            show_table(result)
    elif option == "4":##Update Company
        ui.clear()
        idx = ui.get_inputs("Enter company ID: ")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid company ID! ('{idx}')")
            return True
        else:
            company = ui.get_inputs("Enter the new value of the name.\n")
            if common.check_valid_id(table, company):
                ui.print_error(f"This company ('{company}') is already taken!")
            else:
                data_manager.export_to_file(myfile, update_company(table, idx, "name", company))
    elif option == "5":##Delete company
        ui.clear()
        idx = ui.get_inputs("Enter company ID: ")
        positions = data_manager.imports_from_file("position/positions.txt")
        if common.check_valid_id(table, idx) == False:
            ui.clear()
            ui.print_error(f"Invalid company ID! ('{idx}')")
        else:
            if common.check_if_exist(positions, idx) == False:
                ui.clear()
                ui.print_error(f"This company has an open position!")
            else:
                data_manager.export_to_file(myfile, common.delete_element(table, idx))
    elif option == "0":
        ui.clear()
        return False
    else:
        raise KeyError(f"There is no such option. ({option})")
    return True

def create_company(table):
    table.append(common.create_element(table, ["Enter company name: "]))
    return table

def read_company(table, idx):
    options = ["ID", "Name"]
    return common.read_element(table, idx, options)

def positions_by_companies(idx, positions):
    open_pos = []
    for row in positions:
        if row[3] == idx:
            open_pos.append(row[1])
    return open_pos

def update_company(table, idx, att, new_att):
    return common.update_element(table, idx, att, new_att, {"name": 1})

def show_table(table):
    titles = ["ID", "NAME"]
    ui.print_table(table, titles)