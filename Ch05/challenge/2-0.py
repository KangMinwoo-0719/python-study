def mul(*values):
    time = 1
    for i in range(len(values)):
        time *= values[i]
    return time


print(mul(5, 7, 9, 10))


