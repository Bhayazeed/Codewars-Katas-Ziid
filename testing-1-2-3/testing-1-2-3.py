def number(lines):
    count = 1
    for i in range(len(lines)):
        x = lines[i]
        lines.pop(i)
        lines.insert(i,f"{count}: {x}")
        count += 1
        i += 1
    return lines