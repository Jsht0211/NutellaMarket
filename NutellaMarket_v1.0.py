'''
NutellaMarket v1.0
20240314
Made by Joe
'''

import random
import os

def clsc():
    os.system('cls' if os.name == 'nt' else 'clear')

money: int = 5
nutellas = []

def ifint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def yesNo():
    while True:
        ans = input("yes or no:").capitalize()
        if ans == "Yes" or ans == "Y" or ans == "Yeah":
            return True
        elif ans == "No" or ans == "N" or ans == "Nah": 
            return False  
        else:
            print("???\n")
class nutella:
    def __init__ (self,name,price):
        self.name = name
        self.price = price
        
    def sell(self,name):
        global nutellas
        global money
        print(f"Are you sure you want to sell {name}?")
        if yesNo():
            found = "n"
            for n in nutellas:
                if n.name == name:
                    found = n
                    break
            price = found.price        
            sellPrice = float(input(f"At which price do you want to sold this nutella(The original price is {price},maximum selling price is {price * 2}):"))
            if sellPrice > price:
                if sellPrice - price <= price:
                    nutellas.remove(found)
                    money += sellPrice
                    print("nutella sold successfully")
                elif sellPrice - price > price:
                    print("Too expensive")   
            elif sellPrice == price:
                print(f"You won't earn any money selling this nutella.Are you sure you are going to sell {name}?") 
                if yesNo():
                    nutellas.remove(found)
                    money += sellPrice
                    print("nutella sold successfully")
                else:
                    print("ok")    
            else:        
                print(f"You will lose money selling this nutella.Are you sure you are going to sell {name}?") 
                if yesNo():
                    nutellas.remove(found)
                    money += sellPrice
                    print("nutella sold successfully")
                else:
                    print("ok")
        else:
            print("ok")
    def buy(self,name,price):
        global money
        global nutellas
        if yesNo():
                if money >= price:
                    nutellas.append(nutella(name,price))
                    money -= price
                    print("nutella bought successfully")
                else:
                    print("You don't have money to buy him")    
        else:
                print("ok")
               
 
ctn = nutella("jak",5)

def buynutella():        
    global nutellas
    global money
    createName = input("Name of nutella you want to buy:")
    chek = False
    for n in nutellas:
        if n.name == createName:
            chek = True
            break
    if chek:
        print("You already have this nutella")
    else:
        pric = random.randint(1,money)
        print(f"The price of this nutella is ${pric}.Do you want to buy it?")
        ctn.buy(createName,pric)
        
def sellnutella():
    global nutellas
    chek = False
    sellName = input("Name of nutella you want to sell:")  
    for n in nutellas:
        if n.name == sellName:
            chek = True
            break
    if chek:
        ctn.sell(sellName)
    else:
        print(f"You don't have the nutella \"{sellName}\".")    
 
menu = 0
def quity(choices,typey):
    global menu
    while True:    
        if typey == "quit":
            chc = input(f"\nPlease Enter\"{choices}\"to quit:")
        elif typey == "choose":
            chc = input(f"Please enter:")
        if ifint(chc):   
            chc = int(chc)
            for i in choices:
                if chc == i:
                    return chc
                print("???\n")        
        else:       
            print("???\n")
                    
while True:    
    clsc()    
    if menu == 0:
        print("NutellaMarket\n")
        print(f"money:{money}\n")
        print("1.Buy a nutella")
        print("2.Sell a nutella")
        print("3.Check your nutellas\n")

        menu = quity([1,2,3],"choose")
    elif menu == 1:
        buynutella() 
        quity([1],"quit")
        menu = 0
    elif menu == 2:
        sellnutella()    
        quity([1],"quit")
        menu = 0
    elif menu == 3:
        for n in nutellas:
            print(f"{n.name}:${n.price}")
        quity([1],"quit")
        menu = 0