"""write a program to sqare of list element"""

def square(arr):
    li =[]
    for element in arr:
        if element !=0:
            result = element*element
            li.append(result)
        else:
            li.append(element)
    return li

array = [0,1,2,3,4,5]
print(square(array))


