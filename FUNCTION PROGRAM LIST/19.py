values = [10, "Hello", 20, "Python", 3.5, True, 30]
strings = list(filter(lambda x: isinstance(x, str), values))
print("String elements:", strings)

text = input("Enter a string: ")
vowels = list(filter(lambda x: x.lower() in "aeiou", text))
print("Vowels:", vowels)
