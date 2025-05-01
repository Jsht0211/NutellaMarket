'''
NutellaMarket v2.1
20240607
Made by AC
'''

#import module
import random, os, time

#define clear screen function
def clearscreen():
    os.system('cls')

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

#define function to check input validity
def checkvalid(choice: str):
    try: #test can the input be change to integer
        int(choice)
        return True
    except:
        return False
        
#define function to add line segment
def line():
    print("--------------------------------------------------------------")

#define the starting page of the game
def startpage():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb, gamemode
    clearscreen()
    #showing basic information to the player
    print("Welcome to " + bold("nutella Market 2.1"))
    print("In this game, there are two game mode")
    print("Press " + bold("1") + " for gamemode 1. ")
    print("Press " + bold("2") + " for gamemode 2. ")
    print("The rule of them are shown below")
    print("Press any other keys to exit the game")
    line()
    print(bold("Game Rule of gamemode 1:"))
    print("You can buy nutellas from the market, different nutella will have different price and differnent working effiency. ")
    print("These nutellas will work for you and earn money for you. ")
    print("You can only have 5 nutella at a same time at most. ")
    print("You can sell nutella, some merchant will buy it, but usually they won't buy it if it too expensive. ")
    print("If you fail to sell a nutella, your money will be deducted. ")
    print("How long will you take to earn $1000?")
    line()
    print(bold("Game Rule of gamemode 2:"))
    print("Similar to above, but your goal, instead of earn $1000, ")
    print("to earn as much money as you can in 2.5 minutes")
    print("How much will you earn?")
    n = input()
    
    #public list the nutella on the market, private list the nutella that player have
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
    gamemode = 1 #gamemode
    
    #decide operation
    if n == "1":
        clearscreen()
        start = time.time() #record the time start
        gamemode = 1 #change gamemode to 1
    elif n == "2":
        clearscreen()
        start = time.time()
        gamemode = 2 #change gamemode to 2
    else:
        exit()
    
#define the main page of the game
def modelist():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb, gamemode
    clearscreen()
    #showing basic information to the player
    gametick()
    print(bold("Main Page"))
    line()
    print("You have " + bold("$" + addzero(money)))
    print("You use " + bold(addzero(dp(time.time() - start,))) + " seconds now")
    print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec") #showing effiency
    line()
    print("These are the things you can do, please enter the number to select what you want to do")
    print("You can press " + bold("Enter") + " to refresh the page and update the time you use and money you have now")
    print("0. " + bold("Quit") + " game")
    print("1. " + bold("Buy") + " nutella")
    print("2. " + bold("Sold") + " nutella")
    print("3. " + bold("Check") + " nutella")
    mode = input() #choose the mode
    if mode == "0":
            quitgame()
    elif mode == "1":
            buy()
    elif mode == "2":
            sold()
    elif mode == "3":
            check()
    #check validity
    elif mode != "":
        line()
        print("Input invalid. ")
        print("Press any key to continue")
        input()

#define the quit game function (mode 0)
def quitgame():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb, gamemode
    stop = time.time()
    clearscreen()
    print(bold("GAME OVER"))
    line()
    print("Process: " + bold(addzero(money)) + "/1000") #showing process
    print("You use " + bold(addzero(dp(stop - start))) + " seconds") #showing time taken
    print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec") #showing effiency
    line()
    print("Press " + bold("0") + " to restart the game")
    print("Press any other keys to exit the game")
    n = input()
    if n == "0":
        startpage()
    else:
        exit()
        
#define the end page of the game
def endpage():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb, gamemode
    stop = time.time()
    clearscreen()
    print(bold("Congrats!" + " You pass the game successfully"))
    line()
    print("You have " + bold("$" + addzero(money))) #showing money
    print("You use " + bold(addzero(dp(time.time() - start))) + " seconds (" + bold(addzero(dp((time.time() - start)/60))) + " minutes)") #showing time taken
    print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec") #showing effiency
    line()
    print("If you enjoy the game, you can donate to, ")
    print(bold("  - ACgroup"))
    print(bold("  - Joe"))
    print(bold("  - Sidis"))
    print(bold("  - CKC Maths Centre"))
    print("Thank you!")
    line()
    print("Press " + bold("0") + " to restart the game")
    print("Press any other keys to exit the game")
    n = input()
    if n == "0":
        startpage()
    else:
        exit()
        
#define function to check game process
def gametick():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb, gamemode
    if gamemode == 1:
        if money >= 1000:
            endpage()
        elif money < 0:
            quitgame()
    elif gamemode == 2:
        if (time.time() - start) >= 150:
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
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb, gamemode
    while True:
        #Basic setup
        clearscreen()
        n = None #to store which nutella the player want to buy
        m = False #to store the status of trading (is there enough money)
        k = False #to store the status of nutella (is there corresponding nutella)
        f = False #to store the status of plantation (is there enough space to buy more nutellaes)
        
        gametick()
        print(bold("Market"))
        line()
        print("You have " + bold("$" + addzero(money))) #showing money
        print("You use " + bold(addzero(dp(time.time() - start))) + " seconds now") #showing time taken
        print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec") #showing effiency
        line()
        
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
        
        while len(public) > 5: #remove some nutella if there are more than 5 nutellas in the market
            public.pop(random.randint(0,len(public)-1))
            
        #showing basic information to the player
        if len(private) == 5:
            print(bold("You already have 5 nutella, you cannot buy more nutella"))
        if money < 2:
            print(bold("You don't have enough money"))
        print("Aviable nutellas in market")
        print("Enter the number to select which nutella you want do buy")
        print("If you don't want to buy any nutella, or you want to leave the market, press " + bold("Enter"))
        print("--------------------------------------------------------------")
        print("    No.          Price($)          Working effiency($/sec)")
        
        #show the nutella aviable in the market
        for i in range(0,len(public)):
            a = str(public[i][0])
            b = addzero(public[i][1])
            c = addzero(public[i][2])
            print(" "*(6-len(a)) + a + " "*(17-len(b)) + b + " "*(27-len(c)) + c)
            
        #buying nutellas
        while True:
            n = input() #player select nutella
            if checkvalid(n): #check validity
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
                                    line()
                                    print("nutella " + str(public[i][0]) + " have been bought succesfully. ")
                                    public.pop(i) #remove nutella from market
                                    print("Press any key to continue")
                                    input()
                                    
                            if m == True and k == True and f == True: 
                                break #stop looping when trading done
                        #Inform player
                        if k == False:
                            line()
                            print(bold("No nutella found"))
                            print("Press any key to continue")
                            input()
                        elif m == False:
                            line()
                            print(bold("No Enough money"))
                            print("Press any key to continue")
                            input()
                    else:
                        line()
                        print(bold("No space for more nutellas"))
                        print("Press any key to continue")
                        input()
            elif n != "":
                line()
                print("Input invalid. ")
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
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb, gamemode
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
        print("You use " + bold(addzero(dp(time.time() - start))) + " seconds now")
        print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec")
        print("Enter the number to select the nutella you want to sold")
        print("If you don't want to sold any nutella, or you want to leave this page, press " + bold("Enter"))
        print("--------------------------------------------------------------")
        print("    No.          Price($)          Working effiency($/sec)")
        
        #show the nutella the player have
        for i in range(0,len(private)):
            a = str(private[i][0])
            b = addzero(private[i][1])
            c = addzero(private[i][2])
            print(" "*(6-len(a)) + a + " "*(17-len(b)) + b + " "*(27-len(c)) + c)
            
        #sold nutella
        while True:
            n = input() #player select nutella
            if checkvalid(n): #check validity
                if n != "": #make sure the player enter something
                    for i in range(0,len(private)): #check is the nutella exist
                        if private[i][0] == int(n): #if the nutella exist
                            k = True
                            #merchant buying
                            for j in range(random.randint(2,3)):
                                clearscreen()
                                wordlist = [bold("first"), bold("second"), bold("third")] #words to distingish different merchant
                                #basic information of the nutella that player have chosen
                                print("Information of the nutella: ")
                                print("No. " + str(private[i][0]))
                                print("Price($): " + addzero(private[i][1]))
                                print("Working effiency($/sec): " + addzero(private[i][2]))
                                print("--------------------------------------")
                                p = rd(private[i][1]*0.8, private[i][1]*1.05) #deiciding how much the merchant use
                                #showing the basic information of the merchants
                                print("The " + wordlist[j] + " merchant want to buy this nutella using " + bold("$" + addzero(p)))
                                print("Would you sold it?")
                                print("Enter your choice")
                                print("1. " + bold("yes"))
                                print("2. " + bold("no"))
                                c = input() #player decide is it going to be sold
                                if c == "1": #sold
                                    line()
                                    print("Trade Complete")
                                    money += p #increase money
                                    workspeed -= private[i][2]
                                    private[i][1] = p #remarking the price
                                    private.pop(i) #remove the nutella from player
                                    m = True
                                    print("Press any key to continue")
                                    input()
                                    break
                                elif c != "2":
                                    line()
                                    print("Input invalid. ")
                                    print("Press any key to continue")
                                    input()
                            if m == False: #not sold
                                u = rd(private[i][1]*0.01, private[i][1]*0.025) #deiciding the service charges
                                line()
                                print("Trade Fail, " + bold("$" + addzero(u)) + " will be deducted as service charges")
                                money -= u #deduct service charges  
                                print("Press any key to continue")
                                input()
                                break
                        if m == True and k == True:
                            break #stop looping when trading done
                    #inform player
                    if k == False:
                        line()
                        print(bold("No nutella found"))
                        print("Press any key to continue")
                        input()
            elif n != "":
                line()
                print("Input invalid. ")
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
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb, gamemode
    while True:
        clearscreen()
        #showing basic information to the player
        gametick()
        print("You have " + bold("$" + addzero(money)))
        print("You use " + bold(addzero(dp(time.time() - start))) + " seconds now")
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
            print(" "*(6-len(a)) + a + " "*(17-len(b)) + b + " "*(27-len(c)) + c)
        n = input() 
        if n == "":
            break #go back to mainpage when player enter nothing

startpage() #display starting page
while True: 
    modelist() #display main page