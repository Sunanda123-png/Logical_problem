"""printing the number given between and skipping multiple of 5"""
def number(x, y):
    for i in range(x, y):
        if i % 5 == 0:
            continue
        print(i)


number(0, 16)
