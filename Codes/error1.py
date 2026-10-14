class PriceError(Exception):
    pass

class ZeroPriceError(Exception):
    pass

class NegativePriceError(Exception):
    pass


try:
    price = int(input("Enter your price: "))

    if price == 0:
        raise ZeroPriceError("Price cannot be zero")

    if price < 0:
        raise NegativePriceError("Price cannot be negative")

    if price < 2000:
        raise PriceError("Price must be 2000 or above")

    print("Eligible")

except ValueError:
    print("Error: Please enter a valid number")

except ZeroPriceError as e:
    print("Error:", e)

except NegativePriceError as e:
    print("Error:", e)

except PriceError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e)
