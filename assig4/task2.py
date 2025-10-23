
import os

textfile="C:\\Users\\ragha\\Downloads\\python_ass\\assig4\\task2.txt"
userinp=input("enter the data to be printed on the file")

if os.path.exists(textfile):
    print(f"the location{textfile}exists")

    with open(textfile,"w") as file:
        file.write(userinp)

        

else:
    print("not exist")
