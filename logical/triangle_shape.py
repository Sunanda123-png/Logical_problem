def triaangle(n):
    for i in range(1, n+1):
        print(" " * (n-i), end="")
        for j in range(1, i+1):
            print(j, end=" ")
        print()

n=5
triaangle(n)


def inverted_triangle(n):
    for i in range(n,0, -1):
        print(" "*(n-i), end="")
        for j in range(1, i+1):
            print(j, end=" ")
        print()

inverted_triangle(5)