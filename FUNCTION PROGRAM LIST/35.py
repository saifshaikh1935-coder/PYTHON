scores = [88, 92, 78, 95, 86]
grade = lambda score: "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else "F"))
result = list(map(grade, scores))
print(result)
