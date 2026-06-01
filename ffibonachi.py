def print_fibonacci(n):
    a = 0
    b = 1
    
    while a <= n:
        print(a, end=" ") 
        
       
        a, b = b, a + b
        
    print() 



limit = int(input("Print Fibonacci numbers up to what number? "))



print_fibonacci(limit)