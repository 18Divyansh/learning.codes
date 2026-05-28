def sum_loop(number):
    return sum(range(1,number+1))

x = int(input("what is x"))



result=sum_loop(x)
print(f"The sum of numbers from 1 to {x} is: {result}")
