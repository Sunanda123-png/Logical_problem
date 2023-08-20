# file = open("/Users/sunandashil/Downloads/python_test.txt", "r")
# r = file.read()
# print(r)
#


file = open("./python_test.txt", "w")
j = "i am in india and india is beautiful"
write_text = file.write(j)
file.close()
file1 = open("./python_test.txt", "r")
r = file1.readline()
print(r)
file1.close()
