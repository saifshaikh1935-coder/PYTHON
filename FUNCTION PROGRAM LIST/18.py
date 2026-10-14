values = [10, "Hello", 20, "Python", 3.5, True, 30]
integers = list(filter(lambda x: isinstance(x, int) and not isinstance(x, bool), values))
print("Integer elements:", integers)
