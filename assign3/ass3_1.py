number=input("enter the number to be factorial: ")


def funct(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(f"the {number} factorial is {fact}")


num=int(number)
funct(num)