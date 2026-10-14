words = ["level", "python", "madam", "world", "radar"]
palindromes = list(filter(lambda word: word == word[::-1], words))
print("Palindrome words:", palindromes)
