def sum_loop(number):
    count=0 
    for i in range(1,number+1):
        count=count+i
    return count

x = int(input("what is x "))
result=sum_loop(x)
print("sum of numbers is " , result)
