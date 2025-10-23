dict_ott={}


isruning=True
istuning=True
while isruning:
    entry1=input("enter the name of the student")
    entry2=input("enter the student marks")
    while istuning:
        entry=input("do you want to exit y/n")
        if entry=="y":
            dict_ott[entry1]=entry2
           
            isruning=False
            istuning=False
        elif entry=="n":
            dict_ott[entry1]=entry2
            break
            
            
print(dict_ott)

while True:
    entry4=input("enter the student name to extract")
    print(dict_ott[entry4])
    entry5=input("do you want to exit y/n")
    if entry5=="y": 
        break
    elif entry5=="n":
        continue
