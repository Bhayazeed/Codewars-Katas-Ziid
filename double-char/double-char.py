def double_char(s):
    arr = list(s)
    i = 0
    for i in range(len(arr) -1, -1, -1):
        arr.insert(i+1, arr[i])
        i += 1
    return ''.join(arr)