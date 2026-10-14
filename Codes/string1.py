# find() - checks where the word starts
s1="understanding"
if "stand" in s1:
    print("word is exist")
else:
    print("not")


# find() - returns the position of the word
s1="understanding"
a=s1.find("stand")
print(a)


# in - checks whether word exists or not
a="stand" in s1
print(a)


# find() - finds first occurrence
s1="standingunderstanding"
a=s1.find("stand")
print(a)


# rfind() - finds word from right side
a=s1.rfind("not")
print(a)


# index() - returns position of word
s1="understanding"
a=s1.index("stand")
print(a)


# count() - counts how many times word occurs
s1="understanding"
a=s1.count("stand")
print(a)


# startswith() - checks whether string starts with word
s1="understanding"
a=s1.startswith("stand")
print(a)


# endswith() - checks whether string ends with word
s1="understanding"
a=s1.endswith("stand")
print(a)


# isdigit() - checks whether all characters are digits
s1="123"
print(s1.isdigit())


# isalpha() - checks whether all characters are alphabets
s1="abc1"
print(s1.isalpha())


# isdecimal() - checks whether all characters are decimal numbers
s1="1"
print(s1.isdecimal())


# isalnum() - checks whether characters are alphabet or number
s1="123abc"
print(s1.isalnum())


# isspace() - checks whether string contains only spaces
s1=" "
print(s1.isspace())


# isupper() - checks whether string is uppercase
s1="abc"
print(s1.isupper())


# islower() - checks whether string is lowercase
s1="ABC"
print(s1.islower())


# split() - splits string into parts
s1=" under standing is hard "
a=s1.split(",")
print(a)
print(len(a))


# join() - joins strings using a separator
s1=["under","standing","is","hard"]
a=" ".join(s1)
print(a)


# partition() - divides string into 3 parts
s="understanding"
a=s.partition("stand")
print(a)


# rpartition() - divides string into 3 parts from right side
s="standingunderstanding"
a=s.rpartition("stand")
print(a)