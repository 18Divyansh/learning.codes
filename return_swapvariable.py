def swap_variable(A , B ):
    A , B = B , A
   

    return A , B


a = input(" what is a ")
b = input("what is b ")

new_a, new_b = swap_variable(a, b)

print(f"a = {new_a}")
print(f"b = {new_b}")