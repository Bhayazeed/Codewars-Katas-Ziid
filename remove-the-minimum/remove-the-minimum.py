def remove_smallest(numbers):
    if not numbers:
        return []
    
    hasil = numbers.copy()
    smallest_index = 0
    for i in range(1, len(hasil)):
        if hasil[i] < hasil[smallest_index]:
            smallest_index = i
    hasil.pop(smallest_index)
    return hasil