'''
Nutella Market v2.0
20240605
Code RE-written by AC
'''

#import module
import random, os, time

#define clear screen function
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

#define bolding word function
def bold(words: str):
    return("\033[1m" + words + "\033[0m")

#define round off two 2 decimal place function
def dp(numbers: float):
    return(round(numbers,2))

#define random decimals function
def rd(n1: float, n2: float):
    return(dp(random.uniform(n1, n2)))

#define add zero function to make sure that all numbers shown have 2 decimal place
def addzero(words: str):
    return("{:0.{}f}".format(words,2))

#List to store the details of nutellas
#private list the nutella on the market, private list the nutella that player have
#In the list, the first variable is the number, second is the price, third is the working effiency
private = []
public = []

#Set up variables
workspeed = 0 #total working effiency
pubnum = 0 #counting nutellas
money = rd(3.0,10.0) #amount of money
mode = 0 #operation of player
start = 0 #time when game start
stop = 0 #time when game end
timea = 0 #temperory time variable to save
timeb = 0 #temperory time variable to save
    
#define the starting page of the game
def startpage():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb
    clearscreen()
    #showing basic information to the player
    print("Welcome to " + bold("nutella Market 2.0"))
    print("In this game, your goal is to earn " + bold("$1000") + " by ordering nutellas to do there work")
    print("Try to be " + bold("fast!"))
    print("Click " + bold("ENTER") + " to start the game. ")
    print("---------------------------------------------------------")
    print(bold("Game Rule:"))
    print("You can buy nutella from the market, different nutella will have different price and working effiency")
    print("This nutella will work for you and earn money for you")
    print("You can only have 5 nutella at a same time at most. ")
    print("You can sold nutella, some merchant will buy it, but usually they won't buy it if it too expensive")
    print("If you fail to sold a nutella, you will be punished some little money")
    print("How long will you take?")
    input() #enter anything to start the game
    clearscreen()
    start = time.time() #record the time start
    
#define the main page of the game
def modelist():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb
    clearscreen()
    #showing basic information to the player
    gametick()
    print("You have " + bold("$" + addzero(money)))
    print("You use " + bold(addzero(dp(time.time() - start,))) + " seconds now")
    print("These are the things you can do, please enter the number to select what you want to do")
    print("You can press " + bold("Enter") + " to refresh the page and see how much time you use and how much you have now")
    print("0. " + bold("Quit") + " game")
    print("1. " + bold("Buy") + " nutella")
    print("2. " + bold("Sold") + " nutella")
    print("3. " + bold("Check") + " nutella")
    mode = input() #choose the mode

#define the quit game function (mode 0)
def quitgame():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb
    stop = time.time()
    clearscreen()
    print(bold("GAME OVER"))
    print("Process: " + bold(addzero(money)) + "/1000") #showing process
    print("You use " + bold(addzero(dp(stop - start))) + " seconds") #showing time taken
    while True:
        input()
        
#define the end page of the game
def endpage():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb
    stop = time.time()
    clearscreen()
    print(bold("Congrats!" + " You pass the game successfully"))
    print("You have: " + bold("$" + addzero(money))) #showing process
    print("You use " + bold(addzero(dp(stop - start))) + " seconds (" + bold((addzero(dp(stop - start)/60))) + " minutes)") #showing time taken
    print("If you enjoy the game, you can donate to, ")
    print(bold("  - ACgroup"))
    print(bold("  - Joe"))
    print(bold("  - Sidis"))
    print(bold("  - CKC Maths Centre"))
    print("Thank you!")
    while True:
        input()
        
#define function to check game process
def gametick():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb
    if money >= 1000:
        endpage()
    elif money < 0:
        quitgame()
    if timea == 0:
        timea = start
        timeb = time.time()
    else:
        timea = timeb
        timeb = time.time()
    money += (timeb-timea)*workspeed
    
#define the buy nutella function (mode 1)
def buy():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb
    while True:
        #Basic setup
        clearscreen()
        n = None #to store which nutella the player want to buy
        m = False #to store the status of trading (is there enough money)
        k = False #to store the status of nutella (is there corresponding nutella)
        f = False #to store the status of plantation (is there enough space to buy more nutellaes)
        
        gametick()
        print("You have " + bold("$" + addzero(money))) #showing money
        print("You use " + bold(addzero(dp(time.time() - start))) + " seconds now") #showing time taken
        
        #Random nutella in market
        for i in range(random.randint(1,3)):
            pubnum += 1
            #random price, working effiency for a nutella and add the nutella into the market
            if  money <= 2:
                p = rd(2,5)
                public.append([pubnum,p,(rd(p/20 - p/50, p/20 + p/50))*0.6])
            elif 2 <= money and money <= 10:
                p = rd(2, money*0.95)
                public.append([pubnum,p,(rd(p/20 - p/50, p/20 + p/50))*0.5])
            elif money > 10 and money <= 200:
                p = rd(money*0.5, money*0.8)
                public.append([pubnum,p,(rd(p/20 - p/50, p/20 + p/50))*0.4])
            elif money > 200 and money <= 500:
                p = rd(money*0.4, money*0.6)
                public.append([pubnum,p,(rd(p/20 - p/50, p/20 + p/50))*0.3])
            elif money > 500:
                p = rd(money*0.3, money*0.45)
                public.append([pubnum,p,(rd(p/20 - p/50, p/20 + p/50))*0.25])
        
        #remove some nutella if there are more than 5 nutellas in the market
        while len(public) > 5:
            public.pop(random.randint(0,len(public)-1))
            
        #showing basic information to the player
        if len(private) == 5:
            print(bold("You already have 5 nutella, you cannot buy more nutella"))
        if money < 2:
            print(bold("You don't have enough money"))
        print(bold("Avivable") + " nutellas in market")
        print("Enter the number to select which nutella you want do buy")
        print("If you don't want to buy any nutella, or you want to leave the market, press " + bold("Enter"))
        print("--------------------------------------------------------------")
        print("    No.          Price($)          Working effiency($/sec)")
        
        #show the nutella aviable in the market
        for i in range(0,len(public)):
            a = str(public[i][0])
            b = addzero(public[i][1])
            c = addzero(public[i][2])
            print(" "*(6-len(a)) + a + " "*(14-len(b)) + b + " "*(23-len(c)) + c)
            
        #buying nutellas
        while True:
            n = input() #player select nutella
            if n != "": #make sure player enter something
                if len(private) < 5: #check is there space for more nutellas
                    f = True
                    for i in range(0,len(public)): #check is the nutella exist
                        if public[i][0] == int(n): #if the nutella exist
                            k = True
                            if money >= public[i][1]: #checking is there enough money
                                m = True
                                private.append(public[i]) #add nutella 
                                money -= public[i][1] #take away money
                                workspeed += public[i][2] #increase working effiency
                                public.pop(i) #remove nutella from market
                                
                        if m == True and k == True and f == True: 
                            break #stop looping when trading done
                    #Inform player
                    if k == False:
                        print(bold("No nutella found"))
                        print("Press any key to continue")
                        input()
                    elif m == False:
                        print(bold("No Enough money"))
                        print("Press any key to continue")
                        input()
                else:
                    print(bold("No space for more nutellas"))
                    print("Press any key to continue")
                    input()
            #Go back to the main page of market when these happen
            if (m == True and k == True and f == True) or (n == "") or (k == False) or (m == False) or (f == False):
                break
        #Go back to the main page of game when player enter nothing
        if n == "":
            break

#define the sold nutella function
def sold():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb
    while True:
        #basic setup
        clearscreen()
        n = None
        c = None
        k = False
        m = False
        
        #showing basic information to the player
        gametick()
        print("You have " + bold("$" + addzero(money)))
        print("You use " + bold(addzero(dp(time.time() - start,))) + " seconds now")
        print("Enter the number to select the nutella you want to sold")
        print("If you don't want to sold any nutella, or you want to leave this page, press " + bold("Enter"))
        print("--------------------------------------------------------------")
        print("    No.          Price($)          Working effiency($/sec)")
        
        #show the nutella the player have
        for i in range(0,len(private)):
            a = str(private[i][0])
            b = addzero(private[i][1])
            c = addzero(private[i][2])
            print(" "*(6-len(a)) + a + " "*(14-len(b)) + b + " "*(23-len(c)) + c)
            
        #sold nutella
        while True:
            n = input() #player select nutella
            if n != "": #make sure the player enter something
                for i in range(0,len(private)): #check is the nutella exist
                    if private[i][0] == int(n): #if the nutella exist
                        k = True
                        #merchant buying
                        for j in range(random.randint(2,3)):
                            clearscreen()
                            #basic information of the nutella that player have chosen
                            print("Information of the nutella: ")
                            print("No. " + str(private[i][0]))
                            print("Price($): " + addzero(private[i][1]))
                            print("Working effiency($/sec): " + addzero(private[i][2]))
                            print("--------------------------------------")
                            p = rd(private[i][1]*0.75, private[i][1]*1.1) #deiciding how much the merchant use
                            #showing the basic information of the merchants
                            print("A merchant want to buy this nutella using " + bold("$" + addzero(p)))
                            print("Would you sold it?")
                            print("Enter your choice (anything rather than 1 will be look as 2)")
                            print("1. " + bold("yes"))
                            print("2. " + bold("no"))
                            c = input() #player decide is it going to be sold
                            if c == "1": #sold
                                print("Trade Complete")
                                money += p #increase money
                                private[i][1] = p #remarking the price
                                private.pop(i) #remove the nutella from player
                                m = True
                                print("Press any key to continue")
                                input()
                                break
                        if m == False: #not sold
                            u = rd(private[i][1]*0.01, private[i][1]*0.025) #deiciding the service charges
                            print("Trade Fail, " + bold("$" + addzero(u)) + " will be deducted as service charges")
                            money -= u #deduct service charges  
                            print("Press any key to continue")
                            input()
                            break
                    if m == True and k == True:
                        break #stop looping when trading done
                #inform player
                if k == False:
                    print(bold("No nutella found"))
                    print("Press any key to continue")
                    input()
            #go back to the main page of solding when these happen
            if k == False or m == False or (k == True and m == True) or n == "":
                break
        #go back to the main page of game when player enter nothing
        if n == "":
            break
                            
#define the checking function
def check():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb
    while True:
        clearscreen()
        #showing basic information to the player
        gametick()
        print("You have " + bold("$" + addzero(money)))
        print("You use " + bold(addzero(dp(time.time() - start,))) + " seconds now")
        print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec")
        print("These are the nutella you have now. ")
        print("Note that you can only have 5 nutella at most")
        print("Press " + bold("Enter") + " to return to the main page")
        print("--------------------------------------------------------------")
        print("    No.          Price($)          Working effiency($/sec)")
        for i in range(0,len(private)):
            a = str(private[i][0])
            b = addzero(private[i][1])
            c = addzero(private[i][2])
            print(" "*(6-len(a)) + a + " "*(14-len(b)) + b + " "*(23-len(c)) + c)
        #go back to mainpage when player enter nothing
        n = input()
        if n == "":
            break

startpage() #display starting page
while True: 
    modelist() #display main page
    clearscreen()
    #go to different mode according to player choice
    if mode == "0":
        quitgame()
    elif mode == "1":
        buy()
    elif mode == "2":
        sold()
    elif mode == "3":
        check()