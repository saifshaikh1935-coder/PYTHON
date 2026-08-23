paragraph = input("Enter paragraph: ")

words = paragraph.lower().split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words:
    print(word, ":", count)