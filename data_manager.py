def imports_from_file(filename):
    with open(filename, "r") as file_handle:
        f = file_handle.readlines()
        lista = []
        for lines in f:
            lines = lines[:-1]
            lines = lines.split(";")
            lista.append(lines)
        return lista


def export_to_file(filename,table):
    with open(filename, "w") as file_handle:
        for record in table:
            row = ';'.join(record)
            file_handle.write(row + "\n")


