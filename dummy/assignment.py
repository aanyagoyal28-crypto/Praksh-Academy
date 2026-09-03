while True:
    choice= input("Enter the option(0- exit, 1- enter): ")
    if choice=="0":
        break
    elif choice=="1":
        name= input("Enter your name: ")
        age= int(input("Enter your age: "))
        if age> 18:
            file= open("/Users/aanya/Downloads/Praksh-Academy/dummy/valid_users.txt" , "a")
            file.write(name + str(age))
        elif age>0:
            file= open("/Users/aanya/Downloads/Praksh-Academy/dummy/invalid_users.txt" , "a")
            file.write(name +str(age))
    else:
        print("Invalid input")
    
        

    