mobile_phones = {}

def create():
    global mobile_phones
    mobile_phones = {
        "Samsung": {"price": 30000, "features": "AMOLED display"},
        "Apple": {"price": 70000, "features": "Face ID"}
    }

def add_mobile(name, price, features):
    mobile_phones[name] = {"price": price, "features": features}

def update_mobile(name, price=None, features=None):
    if name in mobile_phones:
        if price is not None:
            mobile_phones[name]["price"] = price
        if features is not None:
            mobile_phones[name]["features"] = features

def delete_mobile(name):
    if name in mobile_phones:
        del mobile_phones[name]

create()
add_mobile("OnePlus", 40000, "Fast charging")
update_mobile("Samsung", price=32000)
delete_mobile("Apple")
print(mobile_phones)
