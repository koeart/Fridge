#!/usr/bin/python

import json
import sys

fridge = {}
product = ""
action  = ""

def main(args):
    fridge  = load()
    if len(args) <= 1:
        action  = raw_input("Operator = ")
        if action == "show":
            show_fridge()
            return
        amount  = int(raw_input("Anzahl = "))
        product = raw_input("Produkt = ")
    elif args[1] == "show":
        show_fridge()
        return
    else:
        action  = args[1]
        amount = int(args[2])
        product = args[3]
    open_fridge(action, product, amount)

def open_fridge(action, product, amount):
    if action == "add":
        for i in range(amount):
            add_product(product)
        print str(amount) + " " + product + " hinzugefuegt"
        save(fridge)
    elif action == "sub":
        if (not(fridge.has_key(product))):
            print "erst reinlegen dann raus nehmen!!"
            return
        for i in range(amount):
            sub_product(product)
        print str(amount) + " " + product + "rausgenommen"
        print str(fridge[product]) + " " + product + "verbleiben"
        save(fridge)
    else:
         print "falsche Eingabe. Bitte nutze \"show\", \"add\" oder \"sub\"."

def show_fridge():
    for product in fridge.keys():
        print "" + product + " " + str(fridge[product])


def add_product(product):
    if (not(fridge.has_key(product))):
        fridge.update({product : 0})
        add_product(product)
    else:
        fridge[product] += 1

def sub_product(product):
    if fridge[product] >= 1:
        fridge[product] -= 1
    else:
        print "Fridge leer!"

def save(fridge):
    f = open("fridge.json", "w")
    json.dump(fridge,f)
    f.close()

def load():
    try:
        global fridge
        f = open("fridge.json","r")
        fridge = json.load(f)
        f.close()
    except:
        fridge = {}
    finally:
        return fridge

if __name__ == '__main__':
    sys.exit(main(sys.argv))