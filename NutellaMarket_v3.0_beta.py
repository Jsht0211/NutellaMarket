'''
NutellaMarket v3.0_beta
20250427
Made by AC, Sidis, Joe
'''
CKC_members = ["ac", "jolex", "sidis", "joe", "alvin", "arvin", "carson", "davis", "jacky", "kayden", "aiden", "kevin"]
#import module
import random, os, time
n = 0
#define clear screen function
def clearscreen():
    os.system('cls')

#define bolding word function
def bold(words: str):
    return("\033[1m" + words + "\033[0m")

#define round off two 2 decimal place function
def dp(numbers: float):
    newno = round(numbers,2)
    if newno <= 0:
        newno = 0
    return(newno)

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
        print("Press " + bold("0") + " to restart the game")
        print("Press any other keys to exit the game")
    n = input()
    if n == "0" and gamemode != -1:
        startpage()
    else:
        exit()

#define the starting page of the game
def startpage():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb, gamemode
    clearscreen()
    #showing basic information to the player
    print("Welcome to " + bold("Nutella Market 3.0_beta"))
    print("In this game, there are three game modes.")
    print("Press " + bold("1") + " for gamemode 1. ")
    print("Press " + bold("2") + " for gamemode 2. ")
    print("Press " + bold("3") + " for gamemode 3. ")
    print("Press " + bold("0") + " for the rules. ")
    print("Press Enter to exit the game")
    line()
    n = input()
    if n == "0":
        clearscreen()
        print(bold("Game Rule of gamemode 1:"))
        print("You can buy nutellas from the market, different nutella will have different price and differnent working effiency. ")
        print("These nutellas will work for you and earn money for you. ")
        print("You can only have 5 nutella at a same time at most. ")
        print("You can sell nutella, some merchant will buy it, but usually they won't buy it if it's too expensive. ")
        print("If you fail to sell a nutella, your money will be deducted. ")
        print("How long will you take to earn $1000?")
        line()
        print(bold("Game Rule of gamemode 2:"))
        print("Similar to above, but your goal, instead of earn $1000, ")
        print("to earn as much money as you can in 2 minutes. ")
        print("How much will you earn?")
        line()
        print(bold("Game Rule of gamemode 3:"))
        print("Free mode!")
        print("Just enjoy the game. ")
        line()
        print("Press the corresponding number key to enter different game modes.")
        print("You can exit the game anytime by pressing Enter key. ")
        gamemode = 0
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
    elif n == "3":
        clearscreen()
        start = time.time()
        gamemode = 3 #change gamemode to 3
    elif n =="-1":
        clearscreen()
        gamemode = -1
        start = time.time()
        negative() # =P
    elif n != "":
        line()
        print("Input invalid. ")
        print("Press any key to continue")
        input()
        startpage()
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
    print("You use " + bold(addzero(dp(time.time() - start))) + " seconds now")
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
    clearscreen()
    ending()

#wow
def negative():
    line()
    print(bold("HOW CAN YOU FIND THIS MODE"))
    for i in range(0,10):
        line()
    input()
    work_eff = 0
    exercise_time = 0
    n_choise3 = 1
    start = time.time()
    bought_time = rd(10, 600)
    while True:
        clearscreen()
        print("You are a", bold("nutella"), "now.")
        print("Behave yourself well until someone buy you.")
        print("(If your working efficiency increases, your price increases.)")
        line()
        print("Press 1 to exercise and increase your working efficiency.")
        print("Press 2 to beg for help.")
        if exercise_time >= 11 and (time.time() - start) < bought_time:
            print("(press 3 to rebel against CKC members who ruled you.)")
        n_respond = input()
        clearscreen()
        if bought_time <= (time.time() - start):
            buyer = random.choice(CKC_members)
            print("Congrats! You are bought by " + buyer + " with the price " + str(rd(25,55)**rd(0.85, 1.5)*work_eff))
            print("You can choose to work hard for him or start to rebel.")
            print("Press 1 to start working for CKC professors for your whole life.")
            print("Press 2 to rebel.")
            n_fight = input()
            if n_fight == "1":
                print("You worked as hard as you can during your rest of life.")
                print("In the year of your " + rd(16,55) + "th birthday, you DIED.")
                print("Press any key to continue...")
                input()
                line()
                print("You,ve used " + bold(dp(time.time() - start)) + " secs to finish your life as a nutella." )
                ending()
            elif n_fight == "2":
                n_respond = "3"
            else:
                print("You didn't give a right choise, isnt it?")
                print("You are forced to work for your whole life.")
                print("In the year of your " + rd(16,55) + "th birthday, you DIED.")
                print("Press any key to continue...")
                input()
                line()
                print("You,ve used " + str(bold(dp(time.time() - start))) + " secs to finish your life as a nutella." )
                ending()
        if n_respond == "":
            clearscreen()
            print(bold("YOU CANNOT ESCAPE FROM THIS"))
            input()
            print(bold("BEHAVE WELL, WORK HARD"))
            input()
            print(bold("OR DIE"))
            for i in range(0,10):
                line()
            input()
        elif n_respond == "1":
            exercise_time += 1
            if exercise_time < 2:
                print("Good")
                work_eff += rd(0.01, 0.03)
                print("Exercise sussess.")
                print("Your new working efficiency is", dp(work_eff),"." )
                print("Press any key to continue...")
                input()
            elif exercise_time <= 15:
                rate = rd(0.01, 0.1)
                chance = random.uniform(-0.1,1)
                if chance <= 0:
                    print("Exercise failed.")
                    work_eff -= rate
                    print("Your new working efficiency is", dp(work_eff),"." )
                    input()
                else:
                    print("Exercise sussess.")
                    work_eff += rate
                    print("Your new working efficiency is", dp(work_eff),"." )   
                    input() 
            elif exercise_time <= 100:
                rate = rd(0.01, 0.5)
                chance = random.uniform(-0.5,1)
                if chance <= 0:
                    print("Exercise failed.")
                    work_eff -= rate
                    print("Your new working efficiency is", dp(work_eff),"." )
                    input()
                else:
                    print("Exercise sussess.")
                    work_eff += rate
                    print("Your new working efficiency is", dp(work_eff),"." ) 
                    input()
            else:
                rate = rd(0.01, 0.5)
                chance = random.uniform(-1,1)
                if chance <= 0:
                    print("Exercise failed.")
                    work_eff -= rate
                    print("Your new working efficiency is", dp(work_eff),"." )
                    input()
                else:
                    print("Exercise sussess.")
                    work_eff += rate
                    print("Your new working efficiency is", dp(work_eff),"." )
                    input()  
            if work_eff < 0.01:
                clearscreen()
                print("Your working efficiency is gone!") 
                print("You are thrown into the Athlantic Ocean.")
                print(bold("YOU DIED!"))
                input()
                line()
                print("You,ve used " + str(bold(str(dp(time.time() - start)))) + " secs to finish your life as a nutella." )
                ending()
                break
        elif n_respond == "2":
            clearscreen()
            print(bold("It is no use crying for help, you stupid nutella"))
            print("You are too noisy crying.")
            print("You are thrown into the Athlantic Ocean.")
            print(bold("YOU DIED!"))
            input()
            line()
            print("You,ve used " + str(bold(str(dp(time.time() - start)))) + " secs to finish your life as a nutella." )
            ending()
        elif n_respond == "3" and exercise_time >= 11:
            HP = 100
            action_time = 0
            have_gun = False
            while n_choise3 != 0:
                clearscreen()
                print("You and the nutellas around decided to start a 'NUTELLA REVOLUTION'.")
                print("Bullets were shot to you guys but you still keep determinated.")
                print("What would you do next?")
                print("Your HP = " + str(HP))
                if have_gun == True:
                    print("You have got a gun.")
                line()
                print("Press 1 to take a gun.")
                print("Press 2 to shot at Professor AC.")
                n_respond = input()
                action_time += 1
                if n_respond == "1":
                    clearscreen()
                    if action_time > 3:
                        print("The guns are all taken by the CKC members")
                        print("Try to steal one from " + str(random.choice(CKC_members)) + "!")
                        print("Press " + bold("Enter") + " to steal!")
                        n_respond = input()
                        chance = rd(-1,1)
                        clearscreen()
                        if chance < 0 or n_respond != "":
                            print("You failed!")
                            print("You are shot by Professor AC.")
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
                    elif have_gun == True:
                        print("You got a gun already!")
                        print("You watse time thinking and got hurted.")
                        print("HP -50")
                        HP -= 50
                        input()
                    else:
                        print("You get a gun from the storing room successfully.")
                        input()
                        have_gun = True
                    clearscreen()
                if n_respond == "2":
                    if have_gun != True:
                        print("You don't have a gun yet!")
                        print("You watse time thinking and got hurted.")
                        print("HP -50")
                        HP -= 50
                        input()
                    else:
                        sbac = rd(-1,1)
                        if sbac <= -0.5:
                            clearscreen()
                            print("Nice shot!")
                            print("You successfully killed the leader of CKCmaths")
                            print("You and fellow nutellaS escaped.")
                            print("You "+ bold("WON") + "!")
                            input()
                            clearscreen()
                            ending()
                            if gamemode not in ["1", "2", "3", "-1"]:
                                startpage()
                            else:
                                while True:
                                    modelist() #display main page
                        else:
                            clearscreen()
                            print("You failed!")
                            print("Professor Jolex shot at you.")
                            print(bold("YOU DIED!"))
                            input()
                            clearscreen()
                            print("You,ve used " + bold(str(dp(time.time() - start))) + " secs to finish your life as a nutella." )
                            ending()
                            startpage()
                            if str(gamemode) not in ["1", "2", "3", "-1"]:
                                startpage()
                            else:
                                while True:
                                    modelist() #display main page

                if HP <= 0:
                    print("You lost all your HP!")
                    print(bold("YOU DIED!"))
                    input()
                    clearscreen()
                    ending()
                    startpage()
                    if str(gamemode) not in ["1", "2", "3", "-1"]:
                        startpage()
                    else:
                        while True:
                            modelist() #display main page
        else:
            line()
            print("Input invalid. ")
            print("Press any key to continue")
            input()
        

           
#define the end page of the game
def endpage():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb, gamemode
    stop = time.time()
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
    print("Press any key to continue...")
    input()
    ending()
        
#define function to check game process
def gametick():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb, gamemode
    if gamemode == 1:
        if money >= 1000:
            endpage()
        elif money < 0:
            quitgame()
    elif gamemode == 2:
        if (time.time() - start) >= 120:
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
            if money <= 2:
                p = rd(2,5)
                public.append([pubnum,p,(rd(p/20 - p/50, p/20 + p/50))*0.6])
            elif money <= 10:
                p = rd(2, money*0.95)
                public.append([pubnum,p,(rd(p/20 - p/50, p/20 + p/50))*0.5])
            elif money <= 200:
                p = rd(money*0.5, money*0.8)
                public.append([pubnum,p,(rd(p/20 - p/50, p/20 + p/50))*0.4])
            elif money <= 500:
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

#define the sold nutella function (mode 2)
def sold():
    global private, public, pubnum, money, mode, start, stop, workspeed, timea, timeb, gamemode
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
                            r = random.choice([2,3,3]) #the number of merchants
                            for j in range(r):
                                clearscreen()
                                wordlist = [bold("first"), bold("second"), bold("third")] #words to distingish different merchant
                                #basic information of the nutella that player have chosen
                                print("Information of the nutella: ")
                                print("No. " + str(private[i][0]))
                                print("Price($): " + addzero(private[i][1]))
                                print("Working effiency($/sec): " + addzero(private[i][2]))
                                print("--------------------------------------")
                                p = rd(private[i][1]*0.7, private[i][1]*1.01) #deiciding how much the merchant use
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
                                        workspeed -= private[i][2]
                                        private[i][1] = p #remarking the price
                                        private.pop(i) #remove the nutella from player
                                        m = True
                                        print("Press any key to continue")
                                        input()
                                        break
                                    elif c == "2":
                                        line()
                                        if j == r-1:
                                            u = rd(private[i][1]*0.01, private[i][1]*0.025) #deiciding the service charges
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
                            
#define the checking function (mode 3)
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
        
enter = input("Enter your player name: ")
if enter.lower() in CKC_members:
    CKC_members.remove(enter.lower())
print("Welcome! " + bold(enter) + '!')
print("Please enjoy our game.")
print("Press any key to continue.")
input()
startpage() #display starting page
if str(gamemode) not in ["1", "2", "3", "-1"]:
    startpage()
else:
    while True:
        modelist() #display main page