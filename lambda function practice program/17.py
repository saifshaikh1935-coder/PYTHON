words = ["apple", "banana", "grapes", "kiwi", "orange"]
result = list(filter(lambda x: len(x) > 5, words))
print("Words with more than 5 characters:", result)
