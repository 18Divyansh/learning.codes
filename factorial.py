def factorial(n):
    total = 1
    for i in range(1, n + 1):
         total =  total*i
         
    return total

x = int(input(" what is your number "))
result = factorial(x)
print("factorial is " , result)