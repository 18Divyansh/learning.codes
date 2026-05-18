def main():
    number = get_number()
    yoo(number)


def get_number():
    while True:
        n = int(input("what is n ?"))
        if n > 0:
            return n
    

def yoo(n):
    for i in range(n):
        print("yoo ")


main()



    