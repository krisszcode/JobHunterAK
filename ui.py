def get_input(title):
    return input(title)

def print_menu(title, options, exit):
    clear()
    print(title.center(20, "#"))
    for i, opt in enumerate(options):
        print(f"({i+1}.) {opt}")
    print(f"\n(0.) {exit}")

def print_error(message):
    print(f"[ERROR]: {message}")

def clear():
    for i in range(30):
        print()

def get_column(table, column):
    result = []
    for row in table:
        result.append(row[column])
    return result

def get_longest_width(table):
    max_length = 0
    for i in table:
        if len(i) > max_length:
            max_length = len(i)
    return max_length

def print_result(result, label):
    clear()
    if type(result) == dict:
        print(f"{label}:\n")
        for key in result:
            print(f"{key}: {result[key]}")
    else:
        print(f"{label}:\n - {result}")

def print_table(table, title_list):
    widths = []
    for i in range(len(title_list)):
        column = choosen_col(table, i)
        column.append(title_list[i])
        longest_width = get_LW(column)
        widths.append(longest_width)

    print("  ")
    for i in range(len(title_list)):
        print("|" + title_list[i].center(widths[i], "_"), end="")
    print()

    for i in range(len(table)):
        row = table[i]
        for j in range(len(row)):
            if j <= len(row) - 2:
                print("|" + row[j].center(widths[j], "_"), end="")
            elif j == len(row) - 1:
                print("|" + row[j].center(widths[j], "_") + "\n", end="")