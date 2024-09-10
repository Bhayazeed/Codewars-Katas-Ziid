def printer_error(s):
    chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    error_chars = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    count_error = 0
    for char in s:
        if char in error_chars:
            count_error += 1
    return f"{count_error}/{len(s)}"