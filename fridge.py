import json

def load():
    try:
        f = open("fridge.json","r")
        fridge = json.load(f)
        f.close()
    except:
        fridge = {}
    return fridge

fridge = load()


def open_fridge(product, action, amount):
    if (not(fridge.has_key(product)) and action != sub):
        fridge.update({product : 0})
        add_product(product)
    else:
        if action == "add":
            for i in range(amount):
                add_product(product)
            save(fridge)
        elif action == "sub":
            for i in range(amount):
                sub_product(product)
            save(fridge)
        else:
            return "Bitte sub oder add ein Produkt!"

def add_product(product):
    fridge[product] += 1
    message = product + " hinzugefuegt"
    return message

def sub_product(product):
    if fridge[product] >= 1:
        fridge[product] -= 1
        message = produkt + "rausgenommen"
    else:
        message = "Fridge leer!"
    return message

def save(fridge):
    json.dump(fridge, jfridge)
    f = open("fridge.json", "w")
    f.write(jfridge)
    f.close()
    return "saved"