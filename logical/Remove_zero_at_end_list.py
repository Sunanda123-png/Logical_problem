def zeroes_move(n):
    i = 0
    j = 0
    while i < len(n):
        if n[i] != 0:
            n[i], n[j] = n[j], n[i]
            j += 1
        i += 1
    return n


my = [0, 1, 0, 2, 3]
result = zeroes_move(my)
print(result)