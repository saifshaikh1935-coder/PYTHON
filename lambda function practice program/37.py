words = ["apple", "orange", "banana", "umbrella", "grapes", "ice"]
selected = list(filter(lambda x: x[0].lower() in "aeiou", words))
result = sorted(selected, key=lambda x: len(x))
print("Words starting with a vowel, sorted by length:", result)
