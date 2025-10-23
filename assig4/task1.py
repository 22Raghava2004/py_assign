
import os

textfile="C:\\Users\\ragha\\Downloads\\python_ass\\assig4\\task1.txt"

if os.path.exists(textfile):
    print(f"the location{textfile}exists")

    with open(textfile,"r") as file:
        reader=file.read()
        print(reader)

else:
    print("not exist")

