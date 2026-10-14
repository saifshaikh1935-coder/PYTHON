import employee2

lstEmployee = []

while True:

    print("1.To Insert Employee Data")
    print("2.Update Employee")
    print("3.Search Data")
    print("4.Sort Data")
    print("5.Delete Data")
    print("6.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        e1 = employee2.Emp()

        e1.getData()

        found = False

        for e in lstEmployee:
            if e.eid == e1.eid:
                found = True
                break

        if found:
            print("Employee id already exists!")

        else:
            e1.calSalary()
            lstEmployee.append(e1)
            print("Employee added successfully!")

    elif choice == 2:

        id = int(input("Enter employee id: "))

        found = False

        for e in lstEmployee:
            if e.eid == id:
                e.updateData()
                found = True
                break

        if found == False:
            print("Employee id not found!")

    elif choice == 3:

        id = int(input("Enter employee id: "))

        found = False

        for e in lstEmployee:
            if e.eid == id:
                e.searchData()
                found = True
                break

        if found == False:
            print("Employee id not found!")

    elif choice == 4:

        lstEmployee.sort(key=lambda e: e.bs)

        print("Employee data sorted successfully!")

        for e in lstEmployee:
            e.putData()

    elif choice == 5:

        id = int(input("Enter employee id: "))

        found = False

        for e in lstEmployee:
            if e.eid == id:
                lstEmployee.remove(e)
                found = True
                print("Employee deleted successfully!")
                break

        if found == False:
            print("Employee id not found!")

    elif choice == 6:

        print("Thank You!")
        break

    else:

        print("Invalid choice")

