def abbrev_name(name):
    x, y = name.split(" ", 1)
    return f"{x[0].upper()}.{y[0].upper()}"