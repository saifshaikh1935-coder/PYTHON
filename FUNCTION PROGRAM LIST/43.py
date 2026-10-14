subject_marks = [
    ("English", 88),
    ("Science", 90),
    ("Maths", 97),
    ("Social sciences", 82)
]
result = sorted(subject_marks, key=lambda item: item[1])
print(result)
