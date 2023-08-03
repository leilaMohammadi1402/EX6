import random
pc_number=random.randint(0,20)


Hads=1
for i in range(10):
    user_number=int(input("Enter a number az 0 ta 20:"))


    if  user_number<0 or user_number>20:
        print("you should tell number az 0 ta 20!")

    elif user_number==pc_number:
        print("     :)  win   "," your hads is :",Hads)
        break
    elif user_number<pc_number:
        print("Enter a biger number")
    elif  user_number>pc_number:
        print("Enter a smaler number")
    Hads+=1

