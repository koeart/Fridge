fridge ={}

def open_fridge(product, action, amount):
    if (not(fridge.has_key(product)) and action != sub):
        fridge.update({product : 0})
        add_product(product)
    else:
        if action == "add":
            for i in range(amount):
                add_product(product)
        elif action == "sub":
            for i in range(amount):
                sub_product(product)
        else:
            return "Bitte sub oder add ein Produkt!"


def add_product(product):
    fridge[product] += 1
    message = "Produkt hinzugefuegt"
    return message

def sub_product(product):
    if fridge[product] >= 1:
        fridge[product] -= 1
        message = "Produkt rausgenommen"
    else:
        message = "Fridge leer!"
    return message


