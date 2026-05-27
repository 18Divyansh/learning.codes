def table(number):
    count = 1 
    for i in range( 1 , 11):
        count = i*number
        print(number,"x" , i,"=", count)

    

n = int(input("what is your number "))
result = table(n)
print(result)