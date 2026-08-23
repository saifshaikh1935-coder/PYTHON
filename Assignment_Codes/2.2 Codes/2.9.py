def is_anagram(s1,s2):
    return sorted(s1) == sorted(s2)


pairs = [
    ("listen","silent"),
    ("evil","vile"),
    ("heart","earth"),
    ("hello","world")
]

for s1,s2 in pairs:
    print(s1, s2, ":", is_anagram(s1,s2))