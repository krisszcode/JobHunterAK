def get_input(title):
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