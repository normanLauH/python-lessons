for x in range(1, 101):
    isEven = True
    for i in range(1, x):
        if x % i == 0 and x != i and i != 1:
            isEven = False
    if isEven:
        print(x)