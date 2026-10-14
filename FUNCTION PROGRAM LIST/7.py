def count_case(text):
    uppercase = sum(1 for char in text if char.isupper())
    lowercase = sum(1 for char in text if char.islower())
    return uppercase, lowercase

text = input("Enter a string: ")
upper, lower = count_case(text)
print("Uppercase characters =", upper)
print("Lowercase characters =", lower)
