# ==========================================
# PYTHON STRING PRACTICE
# ==========================================


# 1. \n - NEW LINE
str = 'hello\npython'
print(str)


# 2. \t - TAB SPACE
str = "fav\tpython"
print(str)


# 3. TRIPLE QUOTES
str = '''python'''
print(str)


# 4. \\ - BACKSLASH
str = '''hello\\msd'''
print(str)


# 5. PRINT DOUBLE QUOTES
str = '"msd"'
print(str)


# 6. \' - SINGLE QUOTE
str = '"saif\tmsd\'s"'
print(str)


# 7. STRING INDEXING
str = "asad"
print(str[0])


# 8. INDEXING - OTHER POSITIONS
str = "asad"
print(str[1])
print(str[2])
print(str[3])


# 9. REVERSE STRING
str = "python is easy"
print(str[: :-1])


# 10. STRING SLICING
str = "python\tlanguage"
print(str[0:6])


# 11. STRING REPEAT 2 TIMES
print(str * 2)


# 12. STRING REPEAT 7 TIMES
print(str * 7)


# 13. PRINT MULTIPLE STRINGS
str1 = "a"
str2 = "b"
str3 = "c"

print("ljku", str1, "gsbe", str2, "mscit", str3)


# 14. STRING COMPARISON - EQUAL
str4 = "abc"
str5 = "abc"

if str4 == str5:
    print("sink")
else:
    print("not")


# 15. STRING COMPARISON - NOT EQUAL
str6 = "abc"
str7 = "acd"

if str6 == str7:
    print("sink")
else:
    print("not")


# 16. STRING COMPARISON - GREATER THAN
if str6 > str7:
    print("str6 big")
else:
    print("str7 small")


# 17. UPPERCASE
str = "python"
print(str.upper())


# 18. LOWERCASE
str = "PYTHON"
print(str.lower())


# 19. CAPITALIZE
s1 = "  abcde  "
print(s1.capitalize())


# 20. TITLE
print(s1.title())


# 21. SWAPCASE
print(s1.swapcase())


# 22. STRIP - REMOVE OUTSIDE SPACES
print(s1.strip())


# 23. REPLACE
str = "csk"

s2 = str.replace("csk", "mi")

print(s2)


# 24. LENGTH - len()
str = "python"
print(len(str))


# 25. FIND - FIND POSITION
str = "python"
print(str.find("t"))


# 26. COUNT - COUNT CHARACTERS
str = "banana"
print(str.count("a"))


# 27. STARTSWITH
str = "python"

print(str.startswith("py"))


# 28. ENDSWITH
print(str.endswith("on"))


# 29. POSITIVE INDEXING
str = "python"

print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5])


# 30. NEGATIVE INDEXING
str = "python"

print(str[-1])
print(str[-2])
print(str[-3])


# 31. STRING SLICING FROM START
str = "python"

print(str[0:3])


# 32. STRING SLICING FROM MIDDLE
str = "python"

print(str[2:5])


# 33. STRING SLICING WITH STEP
str = "python"

print(str[0:6:2])


# 34. REVERSE USING SLICING
str = "python"

print(str[::-1])