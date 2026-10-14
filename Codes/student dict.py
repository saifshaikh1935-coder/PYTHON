student = {}

while True:
    print("----------------------menue---------------------")
    print("press 1 to insert:-")
    print("press 2 to dispaly:-")
    print("press 3 to delet:-")
    print("press 4 to update:-")

    choice = input("Enter your choise:-")

    match choice:

        case '1':
            key = input("enter the key:-")
            value = input("enter the value:-")
            student.update({key: value})
            print("inserted record into the student:-")

        case '2':
            print(student)

        case '3':
            key = input("enter the key for delet:-")
            student.pop(key)
            print(student)
            print("data deleted from student")

        case '4':
            key = input("enter the key for update:- ")
            if key in student:
                new_value = input("enter the new value:- ")
                student[key] = new_value
                print("Record updated successfully!")
            else:
                print("Error: This key does not exist! Cannot update.")

        case _:
            print("u want to continue??")