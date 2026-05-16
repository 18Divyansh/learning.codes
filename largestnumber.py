def largest_number(a,b,c):
    if a > b and a > c:
        return a 
    elif b > a and b > c:
        return b 
    else:
        return c 

a = int(input(" what is a ?"))
b = int(input(" what is b "))
c = int(input(" what is c "))



result = largest_number(a,b,c) 
print(" the largest number is " , result )
