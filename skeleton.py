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

#Global Constants- main character, background, colors, bank
WIDTH = 500
HEIGHT = 500

GRAY = (138,138,138)
RED = (200,0,0)


cadet = Actor('cadet')
cadet.pos = (100, 300)

start = Actor('button_default')
start.pos = (400,400)

button1 = Actor('element_grey_rectangle_glossy')
button1.pos = (400,20)

welcome_msg = Actor('welcome')
welcome_msg.pos = (250,250)

gender_female = Actor('element_grey_rectangle_glossy') 
gender_male = Actor('element_grey_rectangle_glossy')
life = True
name = ''
gender = ''
money = []
f_score = 0
karma = 0
#name = input("What is your name?")
#Cadet are stored as a list, [name, alive(bool),
# money(nested list with where it is?), frugal score, karma]
cadet_life = [name, gender, money, f_score, karma]

#global screen variables
 
show_main = True
welcome = False
game_1 = False
game_2 = False
game_3 = False
game_4 = False
game_5 = False
game_6 = False
game_7 = False

def draw():
    
    if show_main == True:
        home_screen()
        
    if welcome == True:
        welcome_screen()
    
    if game_1 == True:
        character_choices()
    
    if game_2 == True:
        life_choices()
    
    if game_3 == True:
        select_mentors()
        
    if game_4 == True:
        free_weekend()
    
    if game_5 == True:
        life_event()
    
    if game_6 == True:
        army_navy()
    
    if game_6 == True:
        leave_plans()
    
    if game_7 == True:
        class_weekend()
    
def home_screen():
    cadet.draw()
    start.draw()
    screen.draw.text('CASH COW', (250,100), color = RED)
    screen.draw.text("START", (375,393), color = GRAY)
       
def welcome_screen():
        
    screen.clear()
    screen.fill(RED)
    welcome_msg.draw()

#blake        
def character_choices():
    #draw main background
    global gender_male
    global gender_female
    
    screen.clear()
    screen.draw.text('Select your gender:', (10,20), color = RED)
    
    gender_male.pos = (33,70)
    gender_male.draw()
    screen.draw.text('Male', (12,63))
    
    
    gender_female.pos = (100,70)
    gender_female.draw()
    screen.draw.text('Female', (70,63))
    
#nick
def life_choices():
    pass

#blake
def select_mentors():
    pass

#blake
def free_weekend():
    pass
    
#blake
def life_event():
    pass

#nick
def army_navy():
    pass
    
#nick
def leave_plans():
    pass
    
#nick
def class_weekend():
    pass


def update():
    pass

    
def on_key_down(key):
    global welcome
    global game_1
    if key == keys.SPACE and welcome == True:
        welcome = False
        game_1 = True
        
    
def on_mouse_down(pos,button):
    
    #if button == mouse.LEFT and cadet.collidepoint(pos):
        #print('Open menu')
        #opens menu
        
    if button == mouse.LEFT and button1.collidepoint(pos):
        print('button1 chosen')
        
    if button == mouse.LEFT and start.collidepoint(pos):
        
        global show_main 
        global welcome
        welcome = True
        show_main = False
        print('Start the game')
        
    global gender_female    
    if button == mouse.LEFT and gender_female.collidepoint(pos):
        cadet_life[1] = 'female'
    global gender_male    
    if button == mouse.LEFT and gender_male.collidepoint(pos): 
        gender_male = Actor('element_blue_rectangle_glossy')
        cadet_life[1] = 'male'
        
    #create square with texts
    
    #allow mouse to click square
    
    #input numbers
    
    #



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







