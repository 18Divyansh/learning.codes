def sum_list(number_list):
    count = 0  
    
    for numbers in number_list:
        count = count+int(numbers)
        return count
       


list = input(" enter items seprated by  commaas:").split(",")

result = sum_list(list)
print("sum of the list is ", result)
    