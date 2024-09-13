def summation(num):
    count = 1
    x = 0
    if num == 1:
        return 1
    while count <= num:
        x += count
        count += 1
    return x
    