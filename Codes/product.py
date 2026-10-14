p1=[]


def insert():
    pid=int(input("Enter product id "))
    pnm=input("Enter product Name ")
    price=int(input("Enter product Price "))

    d1={
        "PID":pid,
        "PName":pnm,
        "PPrice":price
    }

    p1.append(d1)
    print("Record inserted successfully")


def display():
    print("\nProduct Records")

    for i in p1:
        print("Product ID :",i["PID"])
        print("Product Name :",i["PName"])
        print("Product Price :",i["PPrice"])
        print("--------------------")


def search():
    pid=int(input("Enter product id to search "))

    for i in p1:
        if i["PID"]==pid:
            print("Product ID :",i["PID"])
            print("Product Name :",i["PName"])
            print("Product Price :",i["PPrice"])
            return

    print("Product not found")


def exit():
    print("Program End")