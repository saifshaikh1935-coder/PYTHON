phone_book = {}

phone_book["TAHA"] = "9876543210"
phone_book["SHARIF"] = "9876543211"
phone_book["ASAD"] = "9876543212"
phone_book["SAHIL"] = "9876543213"
phone_book["FAIZ"] = "9876543214"

print("Phone Book =", phone_book)

name = input("Enter name to search: ")

if name in phone_book:
    print("Number =", phone_book[name])
else:
    print("Contact not found")

phone_book["SHARIF"] = "9999999999"

del phone_book["FAIZ"]

for name in sorted(phone_book):
    print(name, ":", phone_book[name])