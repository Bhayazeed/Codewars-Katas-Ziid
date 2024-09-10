def positive_sum(arr):
    i = 0
    while i < len(arr):
        if arr[i] < 0:
            arr.pop(i)
        else:
            i += 1
    return sum(arr)