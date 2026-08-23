def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
    return s == reverse_string(s)


print("madam:", is_palindrome("madam"))
print("racecar:", is_palindrome("racecar"))

name = input("Enter your name: ")
city = input("Enter your city: ")

print(name, ":", is_palindrome(name))
print(city, ":", is_palindrome(city))