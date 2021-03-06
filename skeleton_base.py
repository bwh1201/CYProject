
'''
Name: Nick Ashby and Blake Havern
Project Skeleton: Cow Loan Projection
Description:
The product that we wish to provide is a simulator that will allow cadets to practice their 
financial habits before they take out their Cow Loan. In this simulator, users will not only
 be able to choose what to spend their money on (car, class ring, engagement ring, etc), but
 also see what may happen to their money if they choose to put it in the stock market. During 
 their time as cadets, major events will take place that can influence what happens to their money.
 This simulator will allow Cadets to see the projected results of their financial habits 10, 20, 
 and 30 years after they receive their Cow Loan. The project will operate like a game, using the 
 pygame zero library which will help create the graphic user interface.  The game will present 
 options for portions of the cow loan and then will simulate a potential future as a result of 
 these decisions. Using pygame zero will allow images and user control over the decisions being taken and 
 increase the aesthetic of the game.  Overall, the creation of this project will be entirely 
 in python using the skills we have learned from the course.  The final product will yield an
 entertaining and informative way for cadets to maximize their cow loan. 
Things we need: clever name, image of cadet, backgrounds, 
'''
import copy
import random

#Global Constants- background, colors, bank
WIDTH = 500
HEIGHT = 500
GRAY = (138,138,138)
RED = (200,0,0)
GOLD = (255,215,0)
BLACK = (0,0,0)
BLUE = (0 ,0, 255)
CHARTREUSE = (127,255,0)
WHITE = (255,255,255)

#Global Variables - Characters, boxes, pictures, etc.
cadet = Actor('cadet')
cadet.pos = (100, 300)

start = Actor('button_default')
start.pos = (400,400)

button1 = Actor('element_grey_rectangle_glossy')
button1.pos = (400,20)

welcome_msg = Actor('welcome')
welcome_msg.pos = (250,250)

take_quit_msg = Actor('take_quit')
welcome_msg.pos = (250,250)

gender_female = Actor('button_default') 
gender_male = Actor('button_default')

next_button = Actor('element_red_rectangle')
next_button.pos = (450,450)

wek_back_button = Actor('element_blue_rectangle', (50,450))

car = Actor('car')
car.pos = (250, 100)
car_expensive = Actor('element_grey_rectangle_glossy')
car_cheap = Actor('element_grey_rectangle_glossy')

text_rect = Rect((180,242), (140,30))
text_active = 0
text = 'Click to enter your name:'
new_text = ''

yes_take = Actor('button_default') 
no_take = Actor('button_default') 

mentor_x = Actor('cadet_x_hov')
mentor_x_yes = Actor('element_red_rectangle')
mentor_good = Actor('mento_good_bio')
mentor_good_yes = Actor('element_red_rectangle')
ment_select = False

#Weekend events
nyc = Actor('nyc', (125,375))
ski = Actor('ski', (375,375))
barracks = Actor('barracks', (125,125))
opp = Actor('palisades',(375,125))

nyc_but = Actor('letter_d', (350, 350))
barracks_but = Actor('letter_c', (350, 203))
ski_but = Actor('letter_e', (145, 205))
opp_but = Actor('letter_b', (145,350))

wek_choice = True
ny_choi = False
bar_choi = False
ski_choi = False
opp_choi = False

#life event
choice = 0
#name = input("What is your name?")
#Cadet are stored as a list, [name, alive(bool),
# money(nested list with where it is?), frugal score, karma]
life = True
name = ''
gender = ''
money = 0
possesions = ['car',0]
karma = 0

cadet_life = [name, gender, money, possesions, karma]

maj_event = False
#global screen variables
quit_msg = False

show_main = True
welcome = False
char_choice = False
life_choi = False
mentor_bool = False
f_weekend = False
major_event = False
arm_nav = False
leave_plan = False
class_week = False
bool_list = [show_main,welcome,char_choice,life_choi,mentor_bool,f_weekend,major_event, arm_nav, leave_plan, class_week]

#Procedure: draw
# This manages the flow of the game from screen to screen
#None -> None
def draw():
    """As the program loops through multiple times per second, this procedure determines what will be displayed.
    whatever element of the main control list == True when the program loops through this list corresponds
    to a function, which displays a specific screen"""
    global bool_list
    global quit_msg
    
    
    if bool_list[0] == True:
        quit_msg = False
        home_screen()
        
    if bool_list[1] == True:
        welcome_screen()
    
    if bool_list[2] == True:
        if quit_msg == False:
            character_choices()
        else:
            take_quit()
    
    if bool_list[3] == True:
        life_choices()
    
    if bool_list[4] == True:
        select_mentors()
        maj_event = True
        
    if bool_list[5] == True:
        free_weekend()
    
    if bool_list[6] == True:
        life_event()
    
    if bool_list[7] == True:
        army_navy()
    
    if bool_list[8] == True:
        leave_plans()
    
    if bool_list[9] == True:
        class_weekend()
    
    
#Procedure: home_screen
#numbers represent position and fontsize, letters represent colors and text
#None -> None
def home_screen():
    """Displays the homescreen of the pygame (background, cadet picture, title"""
    screen.fill(GRAY)
    cadet.draw()
    start.draw()
    screen.draw.text('CASH COW', (250,100), color = GOLD, fontsize = 64)
    screen.draw.text("START", (375,393), color = BLACK)
 
#Procedure: welcome_screen
#Objects represent themselves
#None -> None
def welcome_screen():
    """Displays the welcome screen with our welcome message (detailed instructions, 
    creators' biographies, navigation in the game)
    """     
    screen.clear()
    screen.fill(GRAY)
    welcome_msg.draw()

#blake
#procedure: character_choices
#Objects represent themselves
#None -> None
def character_choices():
    """Prompts user to select their gender and their name. In conjunction with
    on_mouse_down, modifies the user's list to display the appropriate avatar
    and player name
    """
    
    gender()
    cadet_name()
    take_cow_loan()

#Procedure: gender
#Objects reprent a button for male and female
#None -> None
def gender():
    """Offers the user two buttons to select their gender. Modifies
    cadet_lift list to reflect their selections.
    """
    global gender_male
    global gender_female
    
    
    screen.clear()
    screen.fill(GRAY)
    screen.draw.text('Select your gender:', center = (250, 100), color = GOLD, fontsize = 64)
    
    gender_male.pos = (150,170)
    gender_male.draw()
    screen.draw.text('Male', center = (150, 170), color = BLACK)
    
    
    gender_female.pos = (350,170)
    gender_female.draw()
    screen.draw.text('Female', center = (350,170), color = BLACK)
    
    
    next_button.draw()
#Prodedure: cadet_name
#Strings represnet a person's screen name
#None -> None
def cadet_name():
    """References an input function that requests a person enter
    their name.
    """
    global text_active
    global text
    if text_active == 1:
        rect_act = screen.draw.filled_rect(text_rect, BLUE)
    elif text_active == 2:
        rect_act = screen.draw.filled_rect(text_rect, CHARTREUSE)
    else:
        rect_in = screen.draw.filled_rect(text_rect, RED)
        
    screen.draw.text(text, center = (250,260), color = BLACK, fontsize = 15)

#Procedure: take_cow_loan
#yes or no question
#None -> None 
def take_cow_loan():
    
    global yes_take
    global no_take
    
    
    yes_take.pos = (150,370)
    yes_take.draw()
    screen.draw.text('Yes', center = (150,370), color = BLACK)
    
    no_take.pos = (350,370)
    no_take.draw()
    screen.draw.text('No', center = (350,370), color = BLACK)
    
    screen.draw.text('Would you like to take the Cow Cash?', center = (250,330), fontsize = 25, color = BLACK)

def take_quit():
    bool_list[2] = False
    bool_list[0] = True
    #quit_msg = True
    #screen.clear()
    #screen.fill(GRAY)
    #take_quit_msg.draw()
    #cadet_life[3] = 10
    #next_button.draw()
    
    
#Procedure: car_choice
#Objects represent two buttons for users to select what 
# car they'd like to buy.
#None -> None
'''
def car_choice():
    """Prompts users to select one of two cars they'd like
    to buy. This decision is reflected in their bank account,
    which is displayed in the top right of the screen.
    """
    global car_cheap
    global car_expensive
    
   
    
    screen.clear()
    screen.fill(GRAY)
    screen.draw.text("What car do you want to buy:", center = (250,50), color = GOLD, fontsize = 40)
    screen.draw.text("{}".format(cadet_life), center = (250, 100), color = GOLD, fontsize = 15)
    
    car_cheap_text.center =(100,150)
    car_cheap_text.draw()
    car_cheap.pos = (100, 250)
    car_cheap.draw()
    screen.draw.text('Cheap', center = (100,150), color = BLACK)
    
    car_expensive_text.center = (400, 150)
    car_expensive_text.draw()
    car_expensive.pos = (400, 250)
    car_expensive.draw()
    screen.draw.text('Expensive', center= (400,150), color = BLACK)
#Procedure life_choices

#Objects represent a screen where users will make purchases.

#None -> None
'''
def life_choices():

    """Calls multiple functions and displays the options they present on screen.

    Displays a next button at the bottom of the screen to navigate as well.

    """

    screen.clear()

    screen.fill(GRAY)

    screen.draw.text('Lets make some purchases', center = (250,100),color = GOLD)

    #car_choice()

    screen.draw.text(str(cadet_life[2]), center = (400,30), color = GOLD)

    next_button.draw()
   
    
#blake
#Procedure: select_mentors
#Object represents a screen where users can make a decision
# None -> None
def select_mentors():
    """Presents a screen to users which allows them to choose whether or not they'd
    like a mentor through this process. The mentor will always instruct them to 
    follow the safest option.
    """
    global mentor_x
    global mentor_good
    global mentor_x_yes
    global mentor_good_yes
    
    
    
    
    
    screen.clear()
    screen.fill(GRAY)
    screen.draw.text('Select your mentor:', center = (150,50), fontsize = 40, color = BLACK)
   
    mentor_good_yes.pos = (120,100)
    mentor_x_yes.pos = (360,100)
    mentor_x.pos = (360,265)
    mentor_good.pos = (120,265)
    
    mentor_good_yes.draw()
    mentor_x_yes.draw()
    
    screen.draw.text('Cadet X', center = (360,100), fontsize = 15, color = BLACK)
    screen.draw.text('LTC Cody', center = (120,100), fontsize = 15, color = BLACK)
    
    mentor_good.draw()
    mentor_x.draw()
    
    next_button.draw()
    
    
#blake
#Procedure: free_weekend
#Object represets a screen where users can make a decision
# None -> None
def free_weekend():
    """Presents a screen to users asking them how they would spend their free weekend.
    Choices will subtract various amounts of money from users' bank accounts.
    """
    global wek_choice 
    global ny_choi 
    global bar_choi 
    global ski_choi
    global opp_choi
    
    
    if ny_choi:
        nyc_wek()
    elif bar_choi:
        barrack_wek()
    elif ski_choi:
        ski_wek()
    elif opp_choi:
        opp_wek()
    else: 
        make_the_choice()

def nyc_wek():
    screen.clear()
    screen.fill(GRAY)
    global cadet_life
    screen.draw.text('Here is what your mentor has to say:', center = (200,50), color = BLACK)
    
    if cadet_life[3][1] == 0:
        screen.draw.text('Are you sure you want to do this? \n Thayer week coming up. \n Can your wallet take the hit?\n Also higher risk of a board', center = (250,250), fontsize = 30, color = BLACK)
    else:
        screen.draw.text('Great decision.  School doesn\'t matter anyway. \n Use that cow loan go have fun!' , center = (250,250), fontsize = 30, color = BLACK)
    next_button.draw()
    wek_back_button.draw()        
        
def barrack_wek():
    screen.clear()
    screen.fill(GRAY)
    global cadet_life
    screen.draw.text('Here is what your mentor has to say:', center = (200,50), color = BLACK)
    
    if cadet_life[3][1] == 0:
        screen.draw.text('Fantastic decision. You had a rough week coming up and this is definitely best. \n You deserve the rest and recovery and extra time to work ahead.', center = (250,250), fontsize = 30, color = BLACK)
    else:
        screen.draw.text('You are so lame!\n You are in college for goodness sake. \n  This is a terrible decision. \n You deserve a break.', center = (250,250), fontsize = 30, color = BLACK)
    next_button.draw()
    wek_back_button.draw()           

def ski_wek():
    screen.clear()
    screen.fill(GRAY)
    global cadet_life
    screen.draw.text('Here is what your mentor has to say:', center = (200,50), color = BLACK)
    
    if cadet_life[3][1] == 0:
        screen.draw.text('Are you sure you want to do this? \n Thayer week coming up. \n Think if your wallet can sustain. \n Also very high risk of injury.', center = (250,250), fontsize = 30, color = BLACK)
    else:
        screen.draw.text('Skiing is dope! You earned it. \n Just don\'t get hurt. \n Wouldn\'t want to miss out on floor hockey', center = (250,250), fontsize = 30, color = BLACK)
    next_button.draw()
    wek_back_button.draw()           
       
def opp_wek():
    screen.clear()
    screen.fill(GRAY)
    global cadet_life
    screen.draw.text('Here is what your mentor has to say:', center = (200,50), color = BLACK)
    
    if cadet_life[3][1] == 0:
        screen.draw.text('Not a terrible decision but make sure to take some time and work ahead.', center = (250,250), fontsize = 30, color = BLACK)
    else:
        screen.draw.text('Do not be lame.  You have the pass, take it!', center = (250,250), fontsize = 30, color = BLACK)
    next_button.draw()
    wek_back_button.draw()          
#selection screen for weekend
def make_the_choice():   
    global nyc
    global barracks
    global ski
    global opp
    global nyc_but
    global barracks_but
    global ski_but
    global opp_but
    screen.clear()
    screen.fill(CHARTREUSE)
    
    barracks_but.draw()
    nyc_but.draw()
    ski_but.draw()
    opp_but.draw()
    
    screen.draw.text('Congrats! \n You have made it to your \n first free weekend!', center = (250,45), fontsize = 40, color = BLACK)
    screen.draw.text('Select the picture for your plans this weekend', center = (250,110), fontsize = 20, color = BLACK)
    weekend = Actor('free_week',(250,280))
    weekend.draw()
    
    
    
   
    
    
#blake
#Procedure: life_event
#Object represents a screen where users can make a decision
# None -> None
def life_event():
    """Presents a user with a random life event (engagement, family member hospitalization, etc) and
    prompts them to respond. Responses will subtract various amounts of money from users' bank accounts.
    """
    global cadet_life
    global choice
    screen.fill(GRAY)
    screen.draw.text('Choose option A, B, or C', center = (250,50))
    screen.draw.text('A', center = (120,220), fontsize = 40)
    screen.draw.text('B', center = (250,220), fontsize = 40)
    screen.draw.text('C', center = (370,220), fontsize = 40)
    
    
    choice_1 = Actor('element_green_rectangle', (120,250))
    choice_2 = Actor('element_blue_rectangle', (250,250))
    choice_3 = Actor('element_red_rectangle', (370,250))
    choice_1.draw()
    choice_2.draw()
    choice_3.draw()
    
    
    if choice == 1:
        life_event1()
    elif choice == 2:
        life_event2()
    elif choice == 3:
        life_event3()
        
def life_event1():
    pass
def life_event2():
    pass
def life_event3():
    pass  

    
#nick
#Procedure: army_navy
#Object represents a screen where users can make a decision
# None -> None
def army_navy():
    """Presents users with a decision on how much they'd like to spend on Army-Navy weekend.
    Responses will subtract various amounts of money from users' bank accounts.
    """
    screen.fill(GRAY)
    screen.draw.text('army nav', center = (250,250))
    
#nick
#Procedure: leave_plans
#Object represents a screen where users can make a decision
# None -> None
def leave_plans():
    """Presents a user with a decision on how to get home for leave. Reponses will subtract
    various amounts of money from a user's bank account.
    """
    screen.fill(GRAY)
    screen.draw.text('leave_plans', center = (250,250))

    
#nick
#Procedure: class_weekend
#Object represnets a screen where users can make a decision
# None -> None
def class_weekend():
    """Presents a user with a decision on how much they plan on spending during a class weekend. 
    Responses will subtract various amounts of money from a user's bank account
    """
    screen.fill(GRAY)
    screen.draw.text('class weekend', center = (250,250))


#Procedure: update
#Integer represents the amount of money a user has left after their consumption decisions
#None -> None
def update():
    """This procedure will update a the second element of the cadet_life string to reflect the 
    decisions made in the procedures above.
    """
    pass


#Procedure: on_mouse_move
#represents position of mouse for gameflow
#mouse movement -> None
def on_mouse_move(pos): 
    pass
      
#Procedure: on_key_down
#list represents list that controls game flow. keys represent keys on the keyboard
# Keystroke -> None
def on_key_down(key):
    """Recieves a keystroke on the spacebar. Advances the control loop by 1 to begin the
    simulation.
    """
     
    global bool_list
    global text_active
    global text
    global cadet_life
    global new_text
    
    if text_active == 1:
        
        if key == keys.RETURN:
            cadet_life[0] = text
            text_active = 2
            
        elif key == keys.BACKSPACE:
            new_text -= new_text[:-1]
        else:
            letter = str(key)
            new_text += letter[-1]
            
        text = new_text + ''  
        
    #if key == keys.SPACE and quit_msg == True:
        #bool_list[2] = False
        #bool_list[0] = True
    
    if key == keys.SPACE and bool_list[1] == True:
        bool_list[1] = False
        bool_list[2] = True
    
    
#Procedure: on_mouse_down()
#tuple of integers represents the (x,y) position of the mouse, string represnets
# the button of the mouse that is pushed.
#Touple of integers, str -> None
def on_mouse_down(pos,button):
    """Recieves a current mouse position (x,y) and a mouse button pressed. Depending on the
    screen displayed, this will perform various actions.
    """
    #if button == mouse.LEFT and cadet.collidepoint(pos):
        #print('Open menu')
        #opens menu
    global bool_list
    global cadet_life
    
            
    if button == mouse.LEFT and next_button.collidepoint(pos):
        x = True
        i = 0
        print(cadet_life)
        while x is True:
            if bool_list[i] == True:
                bool_list[i] = False
                bool_list[i+1] = True
                x = False
            i+=1
        
    if button == mouse.LEFT and button1.collidepoint(pos):
        print('button1 chosen')
        
    if button == mouse.LEFT and start.collidepoint(pos):
       
        bool_list[0] = False
        bool_list[1] = True
        print('Start the game')
        
    global gender_female  
    global gender_male
    if button == mouse.LEFT and gender_female.collidepoint(pos):
        gender_male = Actor('button_default')
        gender_female = Actor('button_selected')
        cadet_life[1] = 'female'
        
    if button == mouse.LEFT and gender_male.collidepoint(pos): 
        gender_female = Actor('button_default')
        gender_male = Actor('button_selected')
        cadet_life[1] = 'male'
    
    global car_cheap
    if button == mouse.LEFT and car_cheap.collidepoint(pos):
        car_cheap = Actor('element_blue_rectangle_glossy')
        cadet_life[2] = cadet_life[2] - 10000
    
    global car_expensive
    if button == mouse.LEFT and car_expensive.collidepoint(pos):
      car_expensive = Actor('element_blue_rectangle_glossy')
      cadet_life[2] = cadet_life[2] - 20000
    
    global yes_take
    global no_take
    if button == mouse.LEFT and yes_take.collidepoint(pos):
        no_take = Actor('button_default')
        yes_take = Actor('button_selected')
        cadet_life[2] = 36000
        take_message()
    
    global mentor_good_yes
    global mentor_x_yes
    global ment_select
    if button == mouse.LEFT and mentor_good_yes.collidepoint(pos):
        cadet_life[4] = 5
        mentor_good_yes = Actor('element_green_rectangle')
        mentor_x_yes = Actor('element_red_rectangle')
        cadet_life[3][1] = 0
    
    if button == mouse.LEFT and mentor_x_yes.collidepoint(pos):
        if ment_select == False:
                cadet_life[4] = 1
                mentor_x_yes = Actor('element_green_rectangle')
                mentor_good_yes = Actor('element_red_rectangle')
                cadet_life[3][1] = 1
        else:
            screen.draw.text('Error: You already selected a mentor', center =(250, 500), color = BLACK)
    
    global wek_choice 
    global ny_choi 
    global bar_choi 
    global ski_choi
    global opp_choi
    if button == mouse.LEFT and wek_back_button.collidepoint(pos):
        wek_choice = True
        ny_choi = False
        bar_choi = False
        ski_choi =False
        opp_choi = False

    if button == mouse.LEFT and opp_but.collidepoint(pos):
        wek_choice = False
        ny_choi = False
        bar_choi = False
        ski_choi =False
        opp_choi = True
        
    if button == mouse.LEFT and nyc_but.collidepoint(pos):
        wek_choice = False
        ny_choi = True
        
        bar_choi = False
        ski_choi =False
        opp_choi = False
        cadet_life[4] -= 1
        
    if button == mouse.LEFT and barracks_but.collidepoint(pos):
        wek_choice = False
        bar_choi = True
        ny_choi = False
        ski_choi =False
        opp_choi = False
        cadet_life[4] += 2
   
    if button == mouse.LEFT and ski_but.collidepoint(pos):
        wek_choice = False
        ski_choi = True
        ny_choi = False
        bar_choi = False
        opp_choi = False
        cadet_life[4] -= 2
      
    global quit_msg
    if button == mouse.LEFT and no_take.collidepoint(pos):
        yes_take = Actor('button_default')
        #no_take = Actor('button_selected')
        quit_msg = True
        
    global text_active    
    if button == mouse.LEFT and text_rect.collidepoint(pos):
        text_active = True
        
        
        
        
    
    #create square with texts
    
    #allow mouse to click square
    
    #input numbers
    
    #

def text_box():
    pass

def take_message():
    pass
#Variables:
     
#Cadet-> stored as a list, [name, alive(bool), money(nested list with where it is?), frugal score, karma]

#Timeline -> nested list shows where the cadet is at in the story

#Weekends -> Not sure how to make this a variable

#Major events -> Random potential events that could increase money or decrease it by large amounts

#Money management -> 

#General timeline-> opening screen pick character name, select mentors,  make initial financial decisions (how much money do you choose
#to invest? how much do you want to spend on your class ring? Are you going to get engaged soon? How much do you want to spend on a car?), 
#first free weekend,  major event 1(good or bad), remake selections, army-navy occurs, winter break plans, 
#class weekend, major event #2, summer plans
#Check in with the cadet in 5, 10, 20, and 30 years. Avatar changed to reflect age (character changes from cadet to LT to LTC to COL)
