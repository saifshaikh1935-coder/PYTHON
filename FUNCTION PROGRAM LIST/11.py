def findString(string1, string2="all"):
    positions = []
    start = 0
    while True:
        position = string1.find(string2, start)
        if position == -1:
            break
        positions.append(position)
        start = position + 1
    return positions

str1 = "Hello all, Good Morning to all."
positions = findString(str1)
if positions:
    print("String 2 found at positions:", positions)
else:
    print("String 2 is not present in String 1")
