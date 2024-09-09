def to_jaden_case(string):
    char = string.split()
    for i in range(len(char)):
        char[i] = char[i].capitalize()
    return " ".join(char)