PasswordList = [""] * 5
tos = -1

def AddPassword():
    global PasswordList , tos
    Password = input("Enter A Password = ")
    if tos == 4:
        print("Stack Is Full...")
    else:
        tos = tos + 1
        PasswordList[tos] = Password

def RemovePassword():
    global PasswordList , tos
    if tos == -1:
        print("Stack Is Empty...")
    else:
        PasswordList[tos] = ""
        tos = tos - 1
        
    

def ViewPassword():
    global PasswordList
    print(f"Passwords Stored In Stacks Are {PasswordList}")

def Main():
    
    choice = 0
    while choice != 4:
        print("1 = Add Password")
        print("2 = Remove Password")
        print("3 = View Password")
        print("4 = Exit")

        choice = int(input("Enter Your Choice = "))
        
        if choice == 1:
            AddPassword()
        elif choice == 2:
            RemovePassword()
        elif choice == 3:
            ViewPassword()
        elif choice == 4:
            break
        else:
            print("Invalid Choice Select Valid Option...")

Main()




