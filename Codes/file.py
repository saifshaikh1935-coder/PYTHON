# ============================================================
# PYTHON FILE HANDLING PRACTICAL PROGRAMS
# ============================================================


# 1. Write 5 names in a file
with open("names.txt", "w") as f:
    for i in range(5):
        name = input("Enter name: ")
        f.write(name + "\n")


# 2. Read 5 names from a file
with open("names.txt", "r") as f:
    print(f.read())


# 3. Count number of characters, words and lines in a file
with open("names.txt", "r") as f:
    data = f.read()

characters = len(data)
words = len(data.split())
lines = len(data.splitlines())

print("Characters =", characters)
print("Words =", words)
print("Lines =", lines)


# 4. Count number of vowels in a file
with open("names.txt", "r") as f:
    data = f.read()

count = 0
for ch in data.lower():
    if ch in "aeiou":
        count += 1

print("Vowels =", count)


# 5. Copy one file data into another file in uppercase
with open("names.txt", "r") as f:
    data = f.read()

with open("copy.txt", "w") as f:
    f.write(data.upper())

print("File copied in uppercase")


# 6. Read one line from a file
with open("names.txt", "r") as f:
    print(f.readline())


# 7. Read all lines using readlines()
with open("names.txt", "r") as f:
    lines = f.readlines()

print(lines)


# 8. Count total uppercase and lowercase letters in a file
with open("names.txt", "r") as f:
    data = f.read()

upper = 0
lower = 0

for ch in data:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase =", upper)
print("Lowercase =", lower)


# 9. Count characters, symbols, digits and white spaces
with open("names.txt", "r") as f:
    data = f.read()

characters = 0
symbols = 0
digits = 0
spaces = 0

for ch in data:
    if ch.isalpha():
        characters += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        symbols += 1

print("Characters =", characters)
print("Digits =", digits)
print("Symbols =", symbols)
print("White spaces =", spaces)


# 10. Search a word in a file
word = input("Enter word to search: ")

with open("names.txt", "r") as f:
    data = f.read()

if word in data:
    print("Word found")
else:
    print("Word not found")


# 11. Replace a specific word in a file
old = input("Enter word to replace: ")
new = input("Enter new word: ")

with open("names.txt", "r") as f:
    data = f.read()

data = data.replace(old, new)

with open("names.txt", "w") as f:
    f.write(data)

print("Word replaced")


# 12. Append data into a file
name = input("Enter name to add: ")

with open("names.txt", "a") as f:
    f.write(name + "\n")

print("Data added")