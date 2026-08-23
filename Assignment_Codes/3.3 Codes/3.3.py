squares = [i**2 for i in range(1,21)]
print("Squares =", squares)

even = [i for i in range(1,51) if i%2 == 0]
print("Even numbers =", even)

sentence = input("Enter a sentence: ")
words = [word for word in sentence.split() if len(word) > 4]
print("Words longer than 4 characters =", words)

cubes = [i**3 for i in range(1,16) if i%2 != 0]
print("Cubes of odd numbers =", cubes)