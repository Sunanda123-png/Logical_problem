def outer_function():
    y = 10

    def inner_function():
        s = y * 2
        return s
    return inner_function()


print(outer_function())
