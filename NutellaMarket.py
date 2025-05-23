'''
NutellaMarket v3.2.0
20250523
Made by AC, Sidis, Joe
'''
#import module
from time import time
from random import uniform, choice, randint
from os import system
from math import log
import sys

#the nutella class
class Nutella:
    def __init__(self,no,price,efficiency,loyalty,sexuality):
        self.no = no
        self.price = price
        self.efficiency = efficiency
        self.loyalty = loyalty
        self.sexuality = sexuality
        self.health = 100
        self.sight = 100
        self.lungNo = 1
        self.heartNo = 1
        self.eyeNo = 1
        self.kidneyNo = 1
        
#define clear screen function
def clearscreen():
    if sys.platform == "win32":
        system('cls')
    else:
        system('clear')
    
def wait():
    print("Press any key to continue")
    input()

#define bolding word function
def bold(words):
    return("\033[1m" + str(words) + "\033[0m")

#define round off two 2 decimal place function
def dp(numbers: float):
    newno = round(numbers,2)
    if newno <= 0:
        newno = 0
    return(newno)

#define random decimals function
def rd(n1: float, n2: float):
    return(dp(uniform(n1, n2)))

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

#show all the nutellas in the list
def showNutellas(nutellaList: list):
    gametick()
    print("Nutella information:\n")
    print("    No.      Price($)      Working effiency($/sec)      Loyalty(%)      Sexuality(%)      Health(%)      Sight(%)   ")
    for i in nutellaList:
        a = str(i.no)
        b = addzero(i.price)
        c = addzero(i.efficiency)
        d = addzero(i.loyalty)
        e = addzero(i.sexuality)
        f = addzero(i.health)
        g = addzero(i.sight)
        print(f"{a:^9}{b:^14}{c:^29}{d:^16}{e:^18}{f:^15}{g:^14}")

#get a nutella by no
def getByNo(no):
    global private

    for i in private:
        if i.no == no:
            return i

    return None

def getByName(name):
    global shopItems

    for i in shopItems:
        if i.name == name:
            return i

    return None

#check if the player owns the nutella
def isExist(no):
    global private

    if checkvalid(no) and getByNo(int(no)) != None:
        return True

    return False

#check if caught by fbi
def checkFbi():
    global fbiChance, caught
    if rd(0,100) < fbiChance:
        caught = True


def rdAttr(attr,org,error):
    return dp(attr*rd(org+error,org-error))

#define ending lines
def ending():
    print("If you enjoy the game, you can donate to, ")
    print(bold("  - ACgroup"))
    print(bold("  - Joe"))
    print(bold("  - Sidis"))
    print(bold("  - CKC Maths Centre"))
    print("Thank you!")
    line()
    if gamemode == -1:
        print("Press any key to exit.")
    else:
        print("Press " + bold("0") + " to exit the game")
        print("Press any other keys to restart the game")
    n = input()
    if gamemode == -1:
        clearscreen()
        exit()
    elif n == "0":
        clearscreen()
        exit()
    else:
        startpage()

#define the starting page of the game
def startpage():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb, gamemode, capacity, fbiChance, caught, shopItems, storage
    clearscreen()
    #showing basic information to the player
    print("Welcome to " + bold("Nutella Market 3.2.0"))
    print("Enter " + bold("rule") + " for the rules. ")
    line()
    print("In this game, there are three game modes.")
    print("Press " + bold("1") + " for gamemode 1. ")
    print("Press " + bold("2") + " for gamemode 2. ")
    print("Press " + bold("3") + " for gamemode 3. ")
    line()
    print("Enter " + bold("funfact") + " for some fun fact I guess. ")
    print("Enter " + bold("history") + " for some history I guess. ")
    print("Press 0 to exit the game")
    n = input()
    if n.lower() == "rule":
        clearscreen()
        print(bold("General Game Rule: "))
        print("You can buy nutellas from the market, different nutella will have different price and differnent working effiency. ")
        print("These nutellas will work for you and earn money for you. ")
        print("You can increase the capacity of nutellas by expanding your cotton field (100m² for each nutella)")
        print("You can sell nutella, some merchant will buy it, but usually they won't buy it if it's too expensive. ")
        print("If you fail to sell a nutella, your money will be deducted.")
        print("You can whip a nutella to increase their working effiency, but their loyalty will decrease. ")
        print("If the loyalty of nutella is too low, they may refused to work, or even escape and steal your money!")
        print("You can also reward the nutella using some money, then their loyalty will increase. ")
        line()
        print(bold("Game Rule of gamemode 1:"))
        print("Your goal is to earn $1000 as fast as you could. ")
        print(bold("Game Rule of gamemode 2:"))
        print("Your goal is to earn as much as you could in 3 minutes")
        print(bold("Game Rule of gamemode 3:"))
        print("Your goal is to enjoy the game!")
        line()
        print("Press any key to go back to the mode selection menu. ")
        n = input()
        startpage()
    
    #public list the nutella on the market, private list the nutella that player have
    #In the list, the first variable is the number, second is the price, third is the working effiency, fourth is the loyalty
    private = []
    public = []

    #Set up variables
    workspeed = 0 #total working effiency
    pubnum = 0 #counting nutellas
    money = rd(3.0,10.0) #amount of money
    capacity = 5 #capacity of nutellas
    mode = 0 #operation of player
    start = 0 #time when game start
    stop = 0 #time when game end
    timea = 0 #temperory time variable to save
    timeb = 0 #temperory time variable to save
    gamemode = 1 #gamemode
    shopItems = [
                    Item("mobile phone",60,["loyalty x 110%","sight - 30%","efficiency x 120%"],0,True),         
                    Item("cannabis",100,["loyalty x 130%","health - 15%","sexuality - 30%","efficiency x 170%"],10,True),
                    Item("cult belief",370,["loyalty -> 100%","efficiency x 110%"],70,True),
                    Item("indulgences",3000,["chance caught by FBI - 20%"],0,False)
                ] #add new items here
    storage = {"mobile phone": 0, "cannabis": 0, "cult belief": 0, "indulgences": 0}  #items the player owns
    fbiChance = 0 #chance of being caught when carrying out risky behaviours
    caught = False
    
    #decide operation
    if n == "1":
        clearscreen()
        start = time() #record the time start
        gamemode = 1 #change gamemode to 1
    elif n == "2":
        clearscreen()
        start = time()
        gamemode = 2 #change gamemode to 2
    elif n == "3":
        clearscreen()
        start = time()
        gamemode = 3 #change gamemode to 3
    elif n == "-1":
        clearscreen()
        gamemode = -1
        start = time()
        negative() # =P
    elif n.lower() == "funfact" or n.lower() == "fun fact":
        clearscreen()
        print(bold("Do you know that:\n"))
        print("The minimum price of a nutella is $2, ")
        print("The minimun working effiency of a nutella is $0.04/s, ")
        print("There is a 3.23% chance of a merchant giving out a price higher than the orginal price to buy a nutella.")
        print("\nAnd in the " + bold("gamemode 1") + " only,")
        print("The maximum price of a nutella is $450", )
        print("The maximum working effiency of a nutella without whipping is $7.87/s, ")
        print("The maximum working efficiency of a nutella without rewarding is $12.30/s,")
        print("and there is no maximum working efficiency of a nutella with rewarding")
        print("while in other modes, there is no upper limit of them!")
        print("(How about a mode with negative number code?... )\n")
        print("In 963 lines of code, Joe contribute 19.84%, Sidis contribute 27.62%, and AC contribute 52.54%!\n")
        print("Press any key to go back to the mode selection menu. ")
        input()
        startpage()
    elif n.lower() == "history":
        clearscreen()
        print(bold("History of Nutella Market:\n"))
        print(bold("v1.0"), "-- 20240314 -- by Joe -- 158 lines of code")
        print("This is the start of everything\n")
        print(bold("v2.0"), "-- 20240605 -- by AC -- 339 lines of code")
        print("Every code have been rewritten, and this become a real game.\n ")
        print(bold("v2.1"), "-- 20240607 -- by AC -- 431 lines of code")
        print("Fix some bug and add gamemode 2. \n")
        print(bold("v2.2"), "-- 20250427 -- by AC -- 470 lines of code")
        print("Fix some bug and add gamemode 3. \n")
        print(bold("v3.0 beta"), "-- 20250501 -- by Sidis -- 736 lines of code")
        print("A mysterious gamemode...\n")
        print(bold("v3.0.0"), "-- 20250502 -- by AC -- 930 lines of code")
        print("Fix some bug and you can now whip or reward the Nutellas. \n")
        print(bold("v3.0.1"), "-- 20250502 -- by Joe -- 920 lines of code")
        print("Reconstruct the data saving system again. \n")
        print(bold("v3.0.2"), "-- 20250502 -- by Joe -- 963 lines of code")
        print("You can now expand your cotton farm!\n")
        print(bold("v3.0.3"), "-- 202505019 -- by Joe -- 1090 lines of code")
        print("You can now breed new nutellas!\n")
        print(bold("v3.1.0"), "-- 20250521 -- by Joe -- 1325 lines of code")
        print("You can now do shopping!\n")
        print(bold("v3.2.0"), "-- 20250523 -- by Joe -- 1471 lines of code")
        print("You can now sell organs of nutellas\n")
        print("Press any key to go back to the mode selection menu. ")
        input()
        startpage()
    elif n == "0":
        exit()
    else:
        line()
        print("Input invalid. ")
        wait()
        startpage()
    
#define the main page of the game
def modelist():
    global money, mode, start, workspeed, capacity, pubnum, fbiChance, storage, caught
    if caught:
        clearscreen()
        line()
        print("Oops! You have been caught by the FBI! " + bold("GAMEOVER"))
        line()
        wait()
        ending()
    else:
        clearscreen()
        #showing basic information to the player
        gametick()
        print(bold("Main Page"))
        line()
        print("You have " + bold("$" + addzero(money)))
        print("You have used " + bold(addzero(dp(time() - start))) + " seconds now")
        print("You have " + bold(capacity*100) + "m² of cotton fields")
        print("Your chance of being arrested by FBI is: " + str(dp(fbiChance)) + "%")
        print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec") #showing effiency
        line()
        print("These are the things you can do, please enter the number to select what you want to do")
        print("You can press " + bold("Enter") + " to refresh the page and update the time you use and money you have now")
        print("0. " + bold("Quit") + " game")
        print("1. " + bold("Buy") + " nutella")
        print("2. " + bold("Sell") + " nutella")
        print("3. " + bold("Expand") + " cotton field")
        print("4. " + bold("Check") + " nutella")
        print("5. " + bold("Manage") + " nutella")
        print("6. " + bold("Shop"))
        print("7. " + bold("Storage"))
        mode = input() #choose the mode
        if mode == "0":
            quitgame()
        elif mode == "1":
            buy()
        elif mode == "2":
            sold()
        elif mode == "3":
            expand()
        elif mode == "4":
            check()
        elif mode == "5":
            clearscreen()
            print("1. " + bold("Whip") + " nutella")
            print("2. " + bold("Reward") + " nutella")
            print("3. " + bold("Breed") + " nutella")
            print("4. " + bold("Sell organ") + " of nutella")
            manage = input()#choose the management
            
            if manage == "1":
                whip()
            elif manage == "2":
                reward()
            elif manage == "3":
                breed()
            elif manage == "4":
                organ()
            #check validity
            elif manage != "":
               line()
               print("Input invalid. ")
               wait()
        elif mode == "6":
            shop()
        elif mode == "7":
            storing()
        elif mode == "&&--&&":
            line()
            print(bold("Developer mode enabled"))
            line()
            capacity = 10000
            money = 1000000
            for i in range(50):
                pubnum += 1
                private.append(Nutella(pubnum,105010,99999,90,90))
            for i in storage:
                storage[i] += 1000
            wait()
        #check validity
        elif mode != "":
            line()
            print("Input invalid. ")
            wait()

#define the quit game function (mode 0)
def quitgame():
    global money, start, stop, workspeed, gamemode
    stop = time()
    clearscreen()
    if gamemode == 1 or gamemode == 2:
        print(bold("GAME OVER"))
    if gamemode == 3:
        print(bold("WELLDONE!"))
    line()
    if gamemode == 1:
        print("Process: " + bold(addzero(money)) + "/1000") #showing process
        print("You use " + bold(addzero(dp(stop - start))) + " seconds (" + bold(addzero(dp((stop - start)/60))) + " minutes)") #showing time taken
        print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec") #showing effiency
    elif gamemode == 2:
        print("Your money amount: " + bold(addzero(money)))
        print("Time used: " + bold(addzero(dp(stop - start))) + "/120 seconds (" + bold(addzero(dp((stop - start)/60))) + "/2 minutes)")
        print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec") #showing effiency
    else: 
        print("You have " + bold("$" + addzero(money))) #showing money
        print("You use " + bold(addzero(dp(stop - start))) + " seconds (" + bold(addzero(dp((stop - start)/60))) + " minutes)") #showing time taken
        print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec") #showing effiency
    line()
    print("Press any key to continue...")
    input()
    ending()

#wow
def negative():
    line()
    print(bold("HOW CAN YOU FIND THIS"))
    input()
    for i in range(3):
        print("--------------")
        print("---********---")
        print("--*--------*--")
        print("--*--****--*--")
        print("--*--*--*--*--")
        print("---**---*--*--")
        print("-------**--*--")
        print("------*----*--")
        print("-----*--**----")
        print("-----*--*-----")
        print("------**------")
        print("--------------")
        print("------**------")
        print("-----*--*-----")
        print("------**------")
        print("--------------")
    input()
    work_eff = 0
    exercise_time = 0
    start = time()
    bought_time = rd(10, 30)
    while True:
        clearscreen()
        print("You are a", bold("nutella"), "now.")
        print("Behave yourself well until someone buy you.")
        print("(If your working efficiency increases, your price increases.)")
        line()
        print("Press 1 to exercise and increase your working efficiency.")
        print("Press 2 to beg for help.")
        if exercise_time >= 11 and (time() - start) < bought_time:
            print("(Press 3 to rebel against CKC members who imprison you.)")
        n_respond = input()
        clearscreen()
        if bought_time <= (time() - start):
            print("Congrats! You are bought by " + choice(CKC_members) + " with the price $" + str(dp(rd(250/7, 250/3)*work_eff)))
            print("You can choose to work hard for him or start to rebel.")
            print("Press 1 to start working for CKC professors for your whole life.")
            print("Press 2 to rebel.")
            n_fight = input()
            if n_fight == "1":
                clearscreen()
                print("You worked as hard as you can during your rest of life.")
                print("You died in your 11.45th birthday")
                print("You used " + bold(str(dp(time() - start))) + " secs to finish your life as a nutella." )
                print("Press any key to continue.")
                input()
                ending()
            elif n_fight == "2":
                n_respond = "3"
            else:
                print("You didn't give a right choise, isnt it?")
                print("You are forced to work for your whole life.")
                print("You died in your 11.45th birthday")
                print("You used " + bold(str(dp(time() - start))) + " secs to finish your life as a nutella." )
                print("Press any key to continue.")
                input()
                ending()
        if n_respond == "":
            clearscreen()
            print(bold("YOU CANNOT ESCAPE FROM THIS"))
            input()
            print(bold("BEHAVE WELL, WORK HARD"))
            input()
            print(bold("OR DIE"))
            input()
            for i in range(3):
                print("--------------")
                print("-----****-----")
                for i in range(8):
                    print("-----*--*-----")
                print("-----****-----")
                print("--------------")
                print("------**------")
                print("-----*--*-----")
                print("------**------")
                print("--------------")
            input()
        elif n_respond == "1":
            exercise_time += 1
            if exercise_time < 2:
                print("Good")
                work_eff += rd(0.01, 0.03)
                print("Exercise sussess.")
                print("Your new working efficiency is", dp(work_eff),"." )
                print("Press any key to continue.")
                input()
            elif exercise_time <= 15:
                chance = uniform(-0.1,1)
                if chance <= 0:
                    print("Exercise failed.")
                    work_eff -= rd(0.01, 0.1)
                    print("Your new working efficiency is", dp(work_eff),"." )
                    input()
                else:
                    print("Exercise sussess.")
                    work_eff += rd(0.01, 0.1)
                    print("Your new working efficiency is", dp(work_eff),"." )   
                    input() 
            elif exercise_time <= 100:
                chance = uniform(-0.5,1)
                if chance <= 0:
                    print("Exercise failed.")
                    work_eff -= rd(0.01, 0.5)
                    print("Your new working efficiency is", dp(work_eff),"." )
                    input()
                else:
                    print("Exercise sussess.")
                    work_eff += rd(0.01, 0.5)
                    print("Your new working efficiency is", dp(work_eff),"." ) 
                    input()
            else:
                chance = uniform(-1,1)
                if chance <= 0:
                    print("Exercise failed.")
                    work_eff -= rd(0.01, 0.5)
                    print("Your new working efficiency is", dp(work_eff),"." )
                    input()
                else:
                    print("Exercise sussess.")
                    work_eff += rd(0.01, 0.5)
                    print("Your new working efficiency is", dp(work_eff),"." )
                    input()  
            if work_eff < 0.01:
                clearscreen()
                print("Your can't even work.") 
                print("You are thrown into the Athlantic Ocean.")
                print(bold("YOU DIED!"))
                input()
                line()
                print("You used " + str(bold(str(dp(time() - start)))) + " secs to finish your life as a nutella." )
                ending()
                break
        elif n_respond == "2":
            clearscreen()
            print(bold("It is no use crying for help, you stupid nutella"))
            print("You are too noisy crying.")
            print("You are thrown into the Athlantic Ocean.")
            print(bold("YOU DIED!"))
            line()
            print("You used " + str(bold(str(dp(time() - start)))) + " secs to finish your life as a nutella." )
            wait()
            ending()
        elif n_respond == "3" and exercise_time >= 11:
            HP = 100
            action_time = 0
            have_gun = False
            while True:
                clearscreen()
                print("You and other nutellas decided to start a REVOLUTION.")
                print("Bullets were shoot to you guys but you still keep determinated.")
                print("What would you do next?")
                print("Your HP = " + str(HP))
                if have_gun == True:
                    print(bold("You have got a gun."))
                else:
                    print(bold("You don't have a gun now"))
                line()
                print("Press 1 to take a gun.")
                print("Press 2 to shot at Professor AC.")
                n_respond = input()
                action_time += 1
                if n_respond == "1":
                    clearscreen()
                    if action_time > 1:
                        randomguy = str(choice(CKC_members))
                        print("No gun are lefted in the warehosue")
                        print("Try to steal one from " + randomguy + "!")
                        print("Press " + bold("Enter") + " to steal!")
                        n_respond = input()
                        clearscreen()
                        if n_respond != "":
                            print("Why do you type in something?")
                            print("Seems like you don't have enough determination. ")
                            print("You died.")
                            HP -= 100
                            input()
                        else:
                            if rd(-1,1) < 0:
                                print("You failed!")
                                print("You are shoot by " + randomguy)
                                print("HP -100")
                                HP -= 100
                                input()
                            else:
                                print("You succeed!")
                                print("You've got a gun now. However, you used too much energy while stealing guns.")
                                have_gun = True
                                print("HP -10")
                                HP -= 10
                                input()
                    if have_gun == True:
                        print("You got a gun already!")
                        print("You watse time thinking and got hurted.")
                        print("HP -50")
                        HP -= 50
                        wait()
                    else:
                        print("You got a gun from the warehosue successfully.")
                        wait()
                        have_gun = True
                    clearscreen()
                elif n_respond == "2":
                    if have_gun != True:
                        clearscreen()
                        print("You don't have a gun yet!")
                        print("You watse time thinking and got hurted.")
                        print("HP -50")
                        HP -= 50
                        wait()
                    else:
                        if rd(-1,1) <= -0.5:
                            clearscreen()
                            print("Headshot!")
                            print("You successfully killed the leader of CKCmaths")
                            print("You and fellow nutellas escaped.")
                            print("You "+ bold("WON") + "!")
                            input()
                            clearscreen()
                            ending()
                        else:
                            clearscreen()
                            print("Assassination failed")
                            print("Professor Jolex shot at you.")
                            print(bold("YOU DIED!"))
                            input()
                            clearscreen()
                            print("You used " + bold(str(dp(time() - start))) + " secs to finish your life as a nutella." )
                            ending()
                if HP <= 0:
                    print("You lost all your HP!")
                    print(bold("YOU DIED!"))
                    print("Press any key to continue.")
                    input()
                    clearscreen()
                    ending()
        else:
            line()
            print("Input invalid. ")
            wait()
           
#define the end page of the game
def endpage():
    global money, start, stop, workspeed, gamemode
    stop = time()
    clearscreen()
    print(bold("Congrats!" + " You pass the game successfully"))
    line()
    if gamemode == 1:
        print("You earn $1000 by using " + bold(addzero(dp(stop - start))) + " seconds (" + bold(addzero(dp((stop - start)/60))) + " minutes)") #showing time taken
        print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec") #showing effiency
    elif gamemode == 2: 
        print("You earn " + bold("$" + addzero(money)) + " by using 120 seconds / 2 minutes. ")
        print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec") #showing effiency
    line()
    print("Press any key to continue.")
    input()
    ending()
        
#define function to check game process
def gametick():
    global private, money, start, workspeed, timea, timeb, gamemode, fbiChance, blind
    if gamemode == 1:
        if money >= 1000:
            endpage()
        elif money < 0:
            quitgame()
    elif gamemode == 2:
        if (time() - start) >= 120:
            endpage()
        elif money < 0:
            quitgame()
    if timea == 0:
        timea = start
        timeb = time()
    else:
        timea = timeb
        timeb = time()
    money += (timeb-timea)*workspeed
    for i in private:
        if i.loyalty <= 15:
            print(bold("NEWS!!!"))
            print("nutella " + str(i.no) + " has a loyalty that was too low, so it escape from your farm. ")
            print("Other nutella spetator his escaption, their working effiency and loyalty decrease. ")
            private.remove(i)
            for j in private:
                j.efficiency *= rd(0.8,0.9)
                j.loyalty *= rd(0.8,0.9)
            line()
            
        if i.health <= 0:
            print(bold("NEWS!!!"))
            print("nutella " + str(i.no) + " has died because of low health.")
            print("the loyalties of all the other nutellas decrease")

            private.remove(i)
            for j in private:
                j.loyalty *= rd(0.8,0.9)
            line()

        if i.kidneyNo > 0 and i.sexuality <= 0:
            print(bold("NEWS!!!"))
            print("nutella " + str(i.no) + " has become sexually disabled")
            print("It cannot breed new nutellas anymore")
            i.sexuality = 0
            i.kidneyNo = 0
            line()

        if i.eyeNo > 0 and i.sight <= 0:
            print(bold("NEWS!!!"))
            print("nutella " + str(i.no) + " has become blind")
            print("It's work efficiency will decrease by 80%")

            i.efficiency *= 0.2
            i.sight = 0
            i.eyeNo = 0
            line()


        if i.loyalty > 100:
            i.loyalty = 100
        if i.sexuality > 100:
            i.sexuality = 100
        if i.health > 100:
            i.health = 100
        if i.sight > 100:
            i.sight = 100

    if fbiChance > 100:
        fbiChance = 100
    if fbiChance < 0:
        fbiChance = 0

    workspeed = 0
    for i in private:
        workspeed += i.efficiency
    
#define the buy nutella function (mode 1)
def buy():
    global private, public, pubnum, money, start, workspeed, capacity
    while True:
        #Basic setup
        clearscreen()
        n = None #to store which nutella the player want to buy
        m = False #to store the status of trading (is there enough money)
        k = False #to store the status of nutella (is there corresponding nutella)
        f = False #to store the status of plantation (is there enough space to buy more nutellaes)
        
        gametick()
        print(bold("Market (buying)"))
        line()
        print("You have " + bold("$" + addzero(money))) #showing money
        print("You use " + bold(addzero(dp(time() - start))) + " seconds now") #showing time taken
        print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec") #showing effiency
        line()
        
        #Random nutella in market
        for i in range(randint(1,3)):
            pubnum += 1
            #random price, working effiency for a nutella and add the nutella into the market
            if money <= 2:
                p = rd(2,5)
                public.append(Nutella(pubnum,p,(rd(p/20 - p/50, p/20 + p/50))*0.6, rd(40,60),rd(20,80)))
            elif money <= 10:
                p = rd(2, money*0.95)
                public.append(Nutella(pubnum,p,(rd(p/20 - p/50, p/20 + p/50))*0.5, rd(40,60),rd(20,80)))
            elif money <= 200:
                p = rd(money*0.5, money*0.8)
                public.append(Nutella(pubnum,p,(rd(p/20 - p/50, p/20 + p/50))*0.4, rd(40,60),rd(20,80)))
            elif money <= 500:
                p = rd(money*0.4, money*0.6)
                public.append(Nutella(pubnum,p,(rd(p/20 - p/50, p/20 + p/50))*0.3, rd(40,60),rd(20,80)))
            elif money > 500:
                p = rd(money*0.3, money*0.45)
                public.append(Nutella(pubnum,p,(rd(p/20 - p/50, p/20 + p/50))*0.25, rd(40,60),rd(20,80)))
        
        while len(public) > 5: #remove some nutella if there are more than 5 nutellass in the market
            public.pop(randint(0,len(public)-1))
            
        #showing basic information to the player
        if len(private) == capacity:
            print(bold("You already have " + str(capacity) + " nutellas, you cannot buy more nutellas"))
        if money < 2:
            print(bold("You don't have enough money"))
        print("Aviable nutellas in market")
        print("Enter the number to select which nutella you want do buy")
        print("If you don't want to buy any nutella, or you want to leave the market, press " + bold("Enter"))
        line()
        showNutellas(public)
            
        #buying nutellas
        while True:
            n = input() #player select nutella
            if checkvalid(n): #check validity
                if n != "": #make sure player enter something
                    if len(private) < capacity: #check is there space for more nutellas
                        f = True
                        for i in public: #check is the nutella exist
                            if i.no == int(n): #if the nutella exist
                                k = True
                                if money >= i.price: #checking is there enough money
                                    m = True
                                    private.append(i) #add nutella 
                                    money -= i.price #take away money
                                    workspeed += i.efficiency #increase working effiency
                                    line()
                                    print("nutella " + str(i.no) + " have been bought succesfully. ")
                                    public.remove(i) #remove nutella from market
                                    wait()
                            if m == True and k == True and f == True: 
                                break #stop looping when trading done
                        #Inform player
                        if k == False:
                            line()
                            print(bold("No nutella found"))
                            wait()
                        elif m == False:
                            line()
                            print(bold("No Enough money"))
                            wait()
                    else:
                        line()
                        print(bold("No space for more nutellas"))
                        wait()
            elif n != "":
                line()
                print("Input invalid. ")
                wait()
            #Go back to the main page of market when these happen
            if (m == True and k == True and f == True) or (n == "") or (k == False) or (m == False) or (f == False):
                break
        #Go back to the main page of game when player enter nothing
        if n == "":
            break

#define the sold nutella function (mode 2)
def sold():
    global private, money, start, workspeed
    while True:
        #basic setup
        clearscreen()
        n = None
        c = None
        k = False
        m = False
        r = None
        #showing basic information to the player
        gametick()
        print(bold("Market (selling)"))
        line()
        print("You have " + bold("$" + addzero(money)))
        print("You use " + bold(addzero(dp(time() - start))) + " seconds now")
        print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec")
        print("Enter the number to select the nutella you want to sold")
        print("If you don't want to sold any nutella, or you want to leave this page, press " + bold("Enter"))
        line()
        showNutellas(private)
            
        #sold nutella
        while True:
            n = input() #player select nutella
            if checkvalid(n): #check validity
                if n != "": #make sure the player enter something
                    for i in private: #check is the nutella exist
                        if i.no == int(n): #if the nutella exist
                            k = True
                            #merchant buying
                            r = choice([2,3,3]) #the number of merchants
                            for j in range(r):
                                clearscreen()
                                wordlist = [bold("first"), bold("second"), bold("third")] #words to distingish different merchant
                                #basic information of the nutella that player have chosen
                                print("Information of the nutella: ")
                                print("No. " + str(i.no))
                                print("Price($): " + addzero(i.price))
                                print("Working effiency($/sec): " + addzero(i.efficiency))
                                print("--------------------------------------")
                                p = rd(i.price*0.7, i.price*1.01) #deiciding how much the merchant use
                                #showing the basic information of the merchants
                                print("The " + wordlist[j] + " merchant want to buy this nutella using " + bold("$" + addzero(p)))
                                print("Would you sold it?")
                                print("Enter your choice")
                                print("1. " + bold("yes"))
                                print("2. " + bold("no"))                            
                                while True:
                                    c = input() #player decide is it going to be sold
                                    if c == "1": #sold
                                        line()
                                        print("Trade Complete")
                                        money += p #increase money
                                        workspeed -= i.efficiency
                                        i.price = p #remarking the price
                                        private.remove(i) #remove the nutella from player
                                        m = True
                                        wait()
                                        break
                                    elif c == "2":
                                        line()
                                        if j == r-1:
                                            u = rd(i.price*0.01, i.price*0.025) #deiciding the service charges
                                            print("Trade Fail, " + bold("$" + addzero(u)) + " will be deducted as service charges")
                                            money -= u #deduct service charges  
                                            print("Press any key to return to the main page")
                                        else: 
                                            print("Press any key to see the next merchant")
                                        input()
                                        break
                                    else:
                                        line()
                                        print("Input invalid. ")
                                        print("Enter your choice again")                                                                            
                                if c == "1":
                                    break
                        if m == True and k == True:
                            break #stop looping when trading done
                    #inform player
                    if k == False:
                        line()
                        print(bold("No nutella found"))
                        wait()
            elif n != "":
                line()
                print("Input invalid. ")
                wait()
            #go back to the main page of solding when these happen
            if k == False or m == False or (k == True and m == True) or n == "":
                break
        #go back to the main page of game when player enter nothing
        if n == "":
            break
                            
#define the whipping function (mode 3)
def whip():
    global private, money, start, workspeed
    while True:
        #basic setup
        clearscreen()
        k = False #to store the status of nutella (is there corresponding nutella)
        #showing basic information to the player
        gametick()
        print(bold("Your nutella menu (whipping)"))
        line()
        print("You have " + bold("$" + addzero(money)))
        print("You use " + bold(addzero(dp(time() - start))) + " seconds now")
        print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec")
        print("Enter the number to select the nutella you want to whip")
        print("If you don't want to sold any nutella, or you want to leave this page, press " + bold("Enter"))
        line()
        showNutellas(private)
            
        #whip nutella
        while True:
            n = input() #player select nutella
            if checkvalid(n): #check validity
                if n != "": #make sure the player enter something
                    for i in private: #check is the nutella exist
                        if i.no == int(n): #if the nutella exist
                            k = True
                            line()
                            print("nutella whipped. It's working effiency increase by a bit, but it loyalty decrease. ")
                            #changing property of the nutella
                            i.efficiency *= rd(1.13, 1.25)
                            i.loyalty -= rd(15, 20)
                            #punishment for getting a too low layalty
                            if i.loyalty <= 30 and rd(0,1) <= 0.8:
                                line()
                                print("Your nutella has a loyalty that was too low. The working effiency decrease by a lot. ")
                                i.efficiency *= rd(0.4,0.6)
                            wait()
                            break
                    if k == False:
                        line()
                        print(bold("No nutella found"))
                        wait()
            elif n != "":
                line()
                print("Input invalid. ")
                wait()
            if k == True or n == "":
                break
        #go back to the main page of game when player enter nothing
        if n == "":
            break
        
#define the rewarding function (mode 4)
def reward():
    global private, money, start, workspeed
    while True:
        #basic setup
        clearscreen()
        k = False #to store the status of nutella (is there corresponding nutella)
        #showing basic information to the player
        gametick()
        print(bold("Your nutella menu (rewarding)"))
        line()
        print("You have " + bold("$" + addzero(money)))
        print("You use " + bold(addzero(dp(time() - start))) + " seconds now")
        print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec")
        print("Enter the number to select the nutella you want to reward")
        print("If you don't want to sold any nutella, or you want to leave this page, press " + bold("Enter"))
        line()
        showNutellas(private)
        #reward nutella
        while True:
            n = input() #player select nutella
            if checkvalid(n): #check validity
                if n != "": #make sure the player enter something
                    for i in private: #check is the nutella exist
                        if i.no == int(n): #if the nutella exist
                            k = True
                            line()
                            rewardmoney = i.price * rd(0.05,0.2)
                            print("Are you sure to reward nutella " + str(i.no) + " using $" + str(dp(rewardmoney)) + "?")
                            print("Enter 1 for yes. ")
                            print("Enter any other key for no. ")
                            m = input()
                            line()
                            if m == "1":
                                if money >= rewardmoney:
                                    print("Reward done. The loyalty of nutella increase. ")
                                    i.loyalty += rd(10,20)
                                    money -= rewardmoney
                                else: 
                                    print("You don't have enough money to reward the nutella. ")
                            else:
                                print("You do not reward the nutella") 
                            wait()
                            break
                    if k == False:
                        line()
                        print(bold("No nutella found"))
                        wait()
            elif n != "":
                line()
                print("Input invalid. ")
                wait()
            if k == True or n == "":
                break
        #go back to the main page of game when player enter nothing
        if n == "":
            break
            
def expand():
    global money, start, workspeed, capacity
    landPrice = dp(log(4*capacity, 1.2))
    while True:
        clearscreen()
        #showing basic information to the player
        print(bold("Cotton field expansion menu"))
        line()
        print("You have " + bold("$" + addzero(money)))
        print("You have " + bold(capacity*100) + "m² of cotton fields")
        print("You use " + bold(addzero(dp(time() - start))) + " seconds now")
        print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec")
        line()
        print("The price for 100m² of land is $" + str(landPrice))
        print("Will you expand your field?")
        print("1." + bold("Yes"))
        print("2." + bold("No"))
        n = input() 
        if n == "1":
            if(money >= landPrice):
                money -= landPrice
                capacity += 1
                print("Field expanded successfully")
            else:
                print(bold("Not enough money"))
            wait()
            break
        elif n == "2":
            break   
        else:
            line()
            print("Input invalid. ")
            wait()
           
#define the checking function (mode 6)
def check():
    global private, money, start, workspeed, capacity
    while True:
        clearscreen()
        #showing basic information to the player
        gametick()
        print(bold("Your nutella menu"))
        line()
        print("You have " + bold("$" + addzero(money)))
        print("You use " + bold(addzero(dp(time() - start))) + " seconds now")
        print("The accumalative working effiency of your nutellas are " + bold(addzero(dp(workspeed))) + " $/sec")
        print("These are the nutella you have now. ")
        print("Note that you can only have", str(capacity) + " nutellas at most")
        print("Press " + bold("Enter") + " to return to the main page")
        line()
        showNutellas(private)
        n = input() 
        if n == "":
            break #go back to mainpage when player enter nothing            



#breed nutellas
def breed():
    global private, money, capacity, pubnum

    if len(private) >= capacity:
        print("Your land needs expansion to hold more nutellas")
        wait()
        return

    while True:
        clearscreen()
        gametick()

        print(bold("Your breeding menu"))
        print("You have " + bold("$" + addzero(money)))
        print("You have used " + bold(addzero(dp(time() - start))) + " seconds now")
        print("If you don't want to breed any nutellas, or you want to leave this page, press " + bold("Enter"))

        line()
        showNutellas(private)
    
        dad = input("\nEnter the no. of the father:")
        if isExist(dad):
            if getByNo(int(dad)).kidneyNo > 0:
                mom = input("Enter the no. of the mother:")
                if isExist(mom) and mom != dad:
                    if getByNo(int(mom)).kidneyNo > 0:
                        dad = getByNo(int(dad))
                        mom = getByNo(int(mom))

                        cost = rdAttr((dad.price+mom.price)/2,0.5,0.15)
                        sucRate = rdAttr((dad.sexuality+mom.sexuality)/2,1,0.3)
                        print("Cost for breeding is: $" + str(cost))
                        print("Success rate for breeding is: " + str(sucRate) + "%")
                        if input("Enter 1 to continue breeding, else stops breeding:") == "1":
                            if money >= cost:
                                money -= cost
                                if rd(0,100) < sucRate:
                                    #success
                                    #rat for ratio
                                    dadRat = rdAttr(dad.sexuality/(dad.sexuality + mom.sexuality),1,0.1)
                                    momRat = 1 - dadRat

                                    pubnum += 1
                                    kid = Nutella(
                                        pubnum,
                                        dad.price*dadRat+mom.price*momRat,
                                        dad.efficiency*dadRat+mom.efficiency*momRat,
                                        #lower loyalty
                                        rdAttr(dad.loyalty*dadRat+mom.loyalty*momRat,0.7,0.15),
                                        dad.sexuality*dadRat+mom.sexuality*momRat
                                    )
                                    line()
                                    print("Breeding succeeded")
                                    print("Kid's attributes:\n")
                                    showNutellas([kid])
                                    private.append(kid)
                                    wait()
                                    break

                                else:
                                    #fails
                                    print("Breeding failed")
                                    wait()
                            else:
                                print("Do not have enough money")
                                wait()
                        else:
                            break
                    else:
                        print("The mom cannot breed")
                        wait()
                elif mom != "":
                    print("Input invalid")
                    wait()
                else:
                    break
            else:
                print("The dad cannot breed")
                wait()
        elif dad != "":
            print("Input invalid")
            wait()
        else:
            break
  
#shop item class
class Item:
    def __init__(self,name,price,eff,fbi,ndNut):
        self.name = name
        self.price = price
        self.eff = eff
        self.fbi = fbi
        self.ndNut = ndNut


#Buy items in the shop
def shop():
    global private, money, shopItems, fbiChance, storage

    while True:
        clearscreen()
        gametick()

        print(bold("Your shop menu"))
        print("You have " + bold("$" + addzero(money)))
        print("You have used " + bold(addzero(dp(time() - start))) + " seconds now")
        print("Your chance of being arrested by FBI is: " + str(dp(fbiChance)) + "%")
        print("If you don't want to buy anything, or you want to leave this page, press " + bold("Enter"))

        line()
        showNutellas(private)

        line()
        print("Shop items(The items with '" + bold("(RISKY)") + "' may attract FBI to arrest you when you buy the item):\n\n")
        
        for i in range(len(shopItems)):
            item = shopItems[i]
            itemEff = " ["
            for j in range(len(item.eff)):
                itemEff += item.eff[j]
                if j != len(item.eff) - 1:
                    itemEff += ", "
                else:
                    itemEff += "] "

            itemRisk = "\nChance to be caught by FBI increased by: " + str(item.fbi) + "%"
            if item.fbi > 0:
                itemRisk += bold(" (RISKY)")

            print(str(i+1) + ". " + item.name + " $" + str(item.price) + itemEff + itemRisk + "\n")

        line()
        choice = input("Which item would you like to buy:")
        if checkvalid(choice):
            choice = int(choice)
            if choice > 0 and choice <= len(shopItems):
                #valid choice
                item = shopItems[choice-1]
                if money >= item.price:
                    money -= item.price
                    storage[item.name] += 1
                    fbiChance += item.fbi
                    if item.fbi > 0:
                        checkFbi()
                    print("Item " + item.name + " bought successfully!")
                    wait()
                    break
                else:
                    print("Not enough money")
                    wait()

            else:
                print("Input out of range,please choose again")
                wait()
        elif choice != "":
            print("Input invalid")
            wait()
        else:
            break


#check and use items
def storing():
    global private, money, storage, fbiChance

    while True:
        clearscreen()
        gametick()

        print(bold("Your storage menu"))
        print("You have " + bold("$" + addzero(money)))
        print("You have used " + bold(addzero(dp(time() - start))) + " seconds now")
        print("If you don't want to use anything, or you want to leave this page, press " + bold("Enter"))

        line()
        showNutellas(private)

        line()
        print("Here are all of your items:\n\n")

        for key, value in storage.items():
            if value > 0:
                print(key + ": " + str(value) + "\n")

        line()
        choice = input("Which item do you want to use:")
        
        if choice != "":
            try:
                choice = choice.lower()
                itemNum = storage[choice]
                
                if itemNum > 0:
                    nut = None
                    if getByName(choice).ndNut:
                        nut = input("On which nutella do you want to use this item:")
                        if not isExist(nut):
                            print("Input invalid")
                            wait()
                            continue
                        nut = getByNo(int(nut))
                    #use the item
                    if choice == "mobile phone":
                        if nut in blind:
                            print("\nThe nutella is already blind, you cannot use mobile phone on it")
                            wait()
                            continue
                        nut.loyalty *= 1.1
                        nut.sight -= 30
                        nut.efficiency *= 1.2
                    
                    elif choice == "cannabis":
                        nut.loyalty *= 1.3
                        nut.health -= 15
                        nut.sexuality -= 30
                        nut.efficiency *= 1.7
                    elif choice == "cult belief":
                        nut.loyalty = 100
                        nut.efficiency *= 1.1
                    elif choice == "indulgences":
                        fbiChance -= 20

                    storage[choice] -= 1

                    print("\nItem used successfully!")
                    wait()
                    break


                else:
                    print("You don't have this item")
                    wait()

            except:
                print("Input invalid")
                wait()
        else:
            break

#sell organ
def organ():   
    global private, money, fbiChance

    while True:
        clearscreen()
        gametick()

        print(bold("Your organ selling menu"))
        print("You have " + bold("$" + addzero(money)))
        print("You have used " + bold(addzero(dp(time() - start))) + " seconds now")
        print("If you don't want to sell organs, or you want to leave this page, press " + bold("Enter"))

        line()
        showNutellas(private)

        line()
        
        nut = input("Which nutella's organ do you want to sell:")

        if isExist(nut):
            nut = getByNo(int(nut))

            #price ratio
            #lung:heart:eyes:kidney
            #3   :10   :1   :2

            lp = dp(nut.efficiency * nut.health/100 * 6.25) #6.25 is to make price of lung close to 3/16 of total price
            hp = dp(nut.price * nut.health/100 * 10/16)
            ep = dp(nut.price * nut.sight/100 * nut.health/100 * 1/16)
            kp = dp(nut.price * nut.sexuality/100 * nut.health/100 * 2/16)

            print("\nThere are 4 types of organs that you can sell(all of them are " + bold("RISKY") + "):\n\n")
            print("1. Lung $" + str(lp))
            print("Chance caught by FBI will increase by: 20%\n")
            print("2. Heart $" + str(hp))
            print("Chance caught by FBI will increase by: 50%\n")
            print("3. Eyes $" + str(ep))
            print("Chance caught by FBI will increase by: 5%\n")
            print("4. Kidney $" + str(kp))
            print("Chance caught by FBI will increase by: 10%\n")

            line()

            choice = input("Which organ do you want to sell:")
            sellSuc = True
            if choice == "1":
                if nut.lungNo > 0:
                    money += lp
                    nut.efficiency *= 0.1
                    nut.health *= 13/16
                    fbiChance += 20
                    nut.lungNo = 0
                else:
                    print("The nutella doesn't have a lung")
                    sellSuc = False
                    wait()
            elif choice == "2":
                if nut.heartNo > 0:
                    money += hp
                    nut.health *= 6/16
                    fbiChance += 50
                    nut.heartNo = 0
                else:
                    print("The nutella doesn't have a heart")
                    sellSuc = False
                    wait()
            elif choice == "3":
                if nut.eyeNo > 0:
                    money += ep
                    nut.sight = 0
                    nut.health *= 15/16
                    nut.efficiency *= 0.2
                    fbiChance += 5
                    nut.eyeNo = 0
                    print("\nThe nutella is now blind, its work efficiency decreases by 80%")
                else:
                    print("The nutella doesn't have eyes")
                    sellSuc = False
                    wait()
            elif choice == "4":
                if nut.kidneyNo > 0:
                    money += kp
                    nut.sexuality = 0
                    nut.health *= 14/16
                    fbiChance += 10
                    nut.kidneyNo = 0
                    print("\nThe nutella is now sexually disabled, it cannot breed anymore")
                else:
                    print("The nutella doesn't have a kidney")
                    sellSuc = False
                    wait()
            elif choice != "":
                print("Input invalid")
                sellSuc = False
                wait()
            else:
                break
            
            if sellSuc:
                checkFbi()
                print("\nOrgan sold successfully!")
                print("\nCurrent attributes of the nutella:\n")
                gametick()
                showNutellas([nut])
                wait()
                break


        elif nut != "":
            print("Input invalid")
            wait()
        else:
            break
        

CKC_members = ["ac", "jolex", "sidis", "joe", "alvin", "arvin", "carson", "davis", "jacky", "kayden", "aiden", "kevin"]
clearscreen()
print("Welcome to the", bold("NutellaMarket")+"!")
print("In this game, you are a master for nutellas in the U.S.A. ")
print("You have a piece of cotton field, which is left by your grandpa. ")
print("Nutellas can work on the cotton fields, they are loyal to you...or are they?")
enter = input("Enter your player name: ")
line()
if enter.lower() in CKC_members:
    CKC_members.remove(enter.lower())
print("Welcome! " + bold(enter) + '!')
print("Please enjoy our game.")
print("Press any key to continue.")
input()
startpage() #display starting page
while True: 
    modelist() 
