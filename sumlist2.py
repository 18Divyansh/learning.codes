def sum_list(number_list):
    total = 0
    for item in number_list:
        total = total + item  
    return total



user_input = [int(x) for x in input("Enter numbers separated by commas: ").split(",")]



result = sum_list(user_input)
print("Sum of the list is:", result)