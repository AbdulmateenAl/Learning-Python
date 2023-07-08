for i in range(0, 10):
    for j in range(0, 10):
        if (j == i and i == j):
            break
        else:
            print("{}{}, ".format(i, j), end = "")