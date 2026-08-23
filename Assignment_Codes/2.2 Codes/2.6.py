def count_vowels(s):
    count = 0

    for ch in s:
        if ch in "aeiouAEIOU":
            count = count+1

    return count


def char_frequency(s):
    frequency = {}

    for ch in s:
        if ch in frequency:
            frequency[ch] = frequency[ch]+1
        else:
            frequency[ch] = 1

    return frequency


sentence = input("Enter a sentence: ")

print("Vowels =", count_vowels(sentence))
print("Character Frequency =", char_frequency(sentence))