average = lambda *numbers: sum(numbers) / len(numbers) if numbers else 0

print("Average =", average(10, 20, 30, 40, 50))
