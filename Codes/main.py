import product as p

while True:

    print("\n1. Add Record")
    print("2. Display Record")
    print("3. Search Record")
    print("4. Exit")

    choice=int(input("Enter your choice "))

    if(choice==1):
        p.insert()

    elif(choice==2):
        p.display()

    elif(choice==3):
        p.search()

    elif(choice==4):
        p.exit()
        break

    else:
        print("Wrong choice")