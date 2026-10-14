def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

numbers = [2, 3, 4, 5]
print("Product =", multiply_list(numbers))
