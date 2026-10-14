def analyze_word(word):
    vowels = "aeiou"
    vowel_counts = [{vowel: word.lower().count(vowel)} for vowel in vowels if vowel in word.lower()]
    return {word.upper(): vowel_counts, "length": len(word)}

text = input("Enter a string: ")
words = text.split()
result = list(map(analyze_word, words))
print(result)
