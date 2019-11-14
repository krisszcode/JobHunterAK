import random
import ui

def generate_random():
    spec_char = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "/", "<", ">", "=", "?", "@"]
    generated = ''
    for i in range(8):
        if i == 0 or i == 5:
            generated += chr(random.randrange(97, 122)) # a-z
        elif i == 1 or i == 4:
            generated += chr(random.randrange(65, 90)) # A-Z
        elif i == 2 or i == 3:
            generated += str(random.randrange(0, 9)) # 0-9
        elif i == 6 or i == 7:
            generated += random.choice(spec_char) # Special characters
    return generated

def check_valid_id(table, idx):
    for row in table:
        if idx in row:
            return True
    return False

def create_element(table, options):
    mylist = []
    idx = ""
    
    while True:
        idx = generate_random()
        if check_valid_id(table, idx) == False:
            break

    mylist.append(idx)
    for i in range(len(options)):
        mylist.append(ui.get_inputs(options[i]))
    
    return mylist

def read_element(table, idx, options):
    mydict = {}
    for student in table:
        if idx == student[0]:
            for i, item in enumerate(student):
                mydict.update({options[i]: item})
    return mydict

def read_elements(table):
    mylist = []
    for i, item in enumerate(table):
        mylist.append([])
        for n in range(len(item)):
            mylist[i].append(item[n])
    return mylist

def update_element(table, idx, att, new_att, options):
    for i in range(len(table)):
        item = table[i]
        if item[0] == idx:
            for n in range(len(item)):
                if n == options[att]:
                    table[i][n] = new_att
    return table
    
def delete_element(table, idx):
    for i, item in enumerate(table):
        if idx in item:
            del table[i]
            return table

def check_if_applied(table, idx):
    for row in table:
        if row[0] == idx and row[1] == "applied":
            return True
        return False
            