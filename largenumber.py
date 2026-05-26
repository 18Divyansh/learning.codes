def find_largest(a, b, c):
    if a > b and a > c:
        print("largest number is", a)
    elif b > a and b > c:
        print("largest number is", b)
    else:
        print("largest number is", c)


a = int(input("what is a: "))
b = int(input("what is b: "))
c = int(input("what is c: "))



find_largest(a, b, c)