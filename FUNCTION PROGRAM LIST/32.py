numbers = [6.56773, 9.57668, 4.00914, 56.24241, 9.01344]
rounded_numbers = list(map(lambda number: round(number), numbers))
two_decimal_numbers = list(map(lambda number: round(number, 2), numbers))
print(rounded_numbers)
print(two_decimal_numbers)
