def rental_car_cost(d):
    # variabel harga, forloop, if else, return harga
    harga = 40 * d
    if d >= 7:
        harga -= 50
    elif d >= 3:
        harga -= 20
    return harga
        