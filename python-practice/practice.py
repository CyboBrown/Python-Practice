# name = input("Enter name: ")
# print("Hello, " + name + "!")

# change this code
mystring = "hello"
myfloat = float(10)
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d %f" % (myint, myfloat))