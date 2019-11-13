def get_inputs(title):
    return input(title)

def print_menu(title, options, exit):
    title = "|" + title + "|"
    print(f"{title.upper().center(20, '#')}\n")
    for i, opt in enumerate(options):
        print(f"({i+1}.) {opt}")
    print(f"\n(0.) {exit}")

def print_error(message):
    print(f"[ERROR]: {message}")

def clear():
    import os
    os.system("clear")

def print_result(result, label):
    clear()

    if type(result) == dict:
        print(f"{label}:\n")
        for key in result:
            print(f"{key}: {result[key]}")

    elif type(result) == list:
        print(f"{label}:\n")
        for item in result:
            print(item)

    else:
        print(f"{label}:\n - {result}")

def print_table(table, title_list):
    widths = []
    for i in range(len(title_list)):
        column = choose_column(table, i)
        column.append(title_list[i])
        longest_width = get_longest_width(column)
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

def choose_column(table, col):
    column = []
    for row in table:
        column.append(row[col])
    return column

def get_longest_width(mylist):
    max_length = 0
    for i in mylist:
        if len(i) > max_length:
            max_length = len(i)
    return max_length