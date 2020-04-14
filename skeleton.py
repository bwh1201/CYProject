
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
GOLD = (255,215,0)
BLACK = (0,0,0)


cadet = Actor('cadet')
cadet.pos = (100, 300)

car = Actor('car')
car.pos = (250, 100)
car_expensive = Actor('element_grey_rectangle_glossy')
car_cheap = Actor('element_grey_rectangle_glossy')

start = Actor('button_default')
start.pos = (400,400)

button1 = Actor('element_grey_rectangle_glossy')
button1.pos = (400,20)

welcome_msg = Actor('welcome')
welcome_msg.pos = (250,250)

gender_female = Actor('button_default') 
gender_male = Actor('button_default')

next_button = Actor('element_red_rectangle')
next_button.pos = (450,450)



#name = input("What is your name?")
#Cadet are stored as a list, [name, alive(bool),
# money(nested list with where it is?), frugal score, karma]
life = True
name = ''
gender = ''
money = 36000
f_score = 0
karma = 0

cadet_life = [name, gender, money, f_score, karma]

#global screen variables


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

def draw():
    global bool_list
    
    if bool_list[0] == True:
        home_screen()
        
    if bool_list[1] == True:
        welcome_screen()
    
    if bool_list[2] == True:
        character_choices()
    
    if bool_list[3] == True:
        life_choices()
    
    if bool_list[4] == True:
        select_mentors()
        
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
    
def home_screen():
    screen.fill(GRAY)
    cadet.draw()
    start.draw()
    screen.draw.text('CASH COW', (250,100), color = GOLD, fontsize = 64)
    screen.draw.text("START", (375,393), color = BLACK)
       
def welcome_screen():
        
    screen.clear()
    screen.fill(GRAY)
    welcome_msg.draw()

#blake        
def character_choices():
    gender()
    cadet_name()
    
    #draw main background
    
def gender():

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

def cadet_name():
    global name
    
    
#nick
def car_choice():
    global car_cheap
    global car_expensive
    
   
    
    screen.clear()
    screen.fill(GRAY)
    screen.draw.text("What car do you want to buy:", (10,20), color = GOLD)
    
    car_cheap.pos =(33,70)
    car_cheap.draw()
    screen.draw.text('Cheap', (12,63), color = BLACK)
    
    car_expensive.pos = (100, 70)
    car_expensive.draw()
    screen.draw.text('Expensive', (70,63), color = BLACK)

def loan_choice():
    screen.clear()
    screen.fill(GRAY)
    screen.draw.text("Do you wish to take the Cow Loan (approximately $36,000 in 2020)",center = (250,100), color = GOLD)
    
    
def life_choices():

    screen.clear()
    screen.fill(GRAY)
    screen.draw.text('Lets make some purchases', center = (250,100),color = GOLD)
    car_choice()
    screen.draw.text(str(cadet_life[2]), center = (400,30), color = GOLD)
    next_button.draw()

#blake
def select_mentors():
    screen.fill(GRAY)
    

#blake
def free_weekend():
    screen.fill(GRAY)

    
#blake
def life_event():
   screen.fill(GRAY)


#nick
def army_navy():
    screen.fill(GRAY)

    
#nick
def leave_plans():
    screen.fill(GRAY)

    
#nick
def class_weekend():
    screen.fill(GRAY)



def update():
    screen.fill(GRAY)


    
def on_key_down(key):

    global bool_list
    
    if key == keys.SPACE and bool_list[1] == True:
        bool_list[1] = False
        bool_list[2] = True
        
    
def on_mouse_down(pos,button):
    
    #if button == mouse.LEFT and cadet.collidepoint(pos):
        #print('Open menu')
        #opens menu
    global bool_list
    global cadet_life
    
    if button == mouse.LEFT and next_button.collidepoint(pos):
        x = True
        i = 0
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
    if button == mouse.LEFT and gender_female.collidepoint(pos):
        gender_female = Actor('button_selected')
        cadet_life[1] = 'female'
        
    global gender_male    
    if button == mouse.LEFT and gender_male.collidepoint(pos): 
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
GOLD = (255,215,0)
BLACK = (0,0,0)


cadet = Actor('cadet')
cadet.pos = (100, 300)

car_cheap = Actor('car_cheap')
car_cheap.pos = (150,400)
car_expensive = Actor('car_expensive')
car_expensive.pos = (350,400)
car_expensive_text = Actor('button_default')
car_cheap_text = Actor('button_default')

start = Actor('button_default')
start.pos = (400,400)

button1 = Actor('element_grey_rectangle_glossy')
button1.pos = (400,20)

welcome_msg = Actor('welcome')
welcome_msg.pos = (250,250)

gender_female = Actor('button_default') 
gender_male = Actor('button_default')

next_button = Actor('element_red_rectangle')
next_button.pos = (450,450)



#name = input("What is your name?")
#Cadet are stored as a list, [name, alive(bool),
# money(nested list with where it is?), frugal score, karma]
life = True
name = ''
gender = ''
money = 36000
f_score = 0
karma = 0

cadet_life = [name, gender, money, f_score, karma]

#global screen variables


show_main = True
welcome = False
char_choice = False
life_choice = False
mentor_bool = False
f_weekend = False
major_event = False
arm_nav = False
leave_plan = False
class_week = False
bool_list = [show_main,welcome,char_choice,life_choice,mentor_bool,f_weekend,major_event, arm_nav, leave_plan, class_week]

def draw():
    global bool_list
    
    if bool_list[0] == True:
        home_screen()
        
    if bool_list[1] == True:
        welcome_screen()
    
    if bool_list[2] == True:
        character_choices()
    
    if bool_list[3] == True:
        life_choices()
    
    if bool_list[4] == True:
        select_mentors()
        
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
    
def home_screen():
    screen.fill(GRAY)
    cadet.draw()
    start.draw()
    screen.draw.text('CASH COW', (250,100), color = GOLD, fontsize = 64)
    screen.draw.text("START", (375,393), color = BLACK)
       
def welcome_screen():
        
    screen.clear()
    screen.fill(GRAY)
    welcome_msg.draw()

#blake        
def character_choices():
    #draw main background
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

#nick
def car_choice():
    global car_cheap
    global car_expensive
    
   
    
    screen.clear()
    screen.fill(GRAY)
    car_cheap.draw()
    car_expensive.draw()
    screen.draw.text("What car do you want to buy:", center = (250, 100), color = GOLD, fontsize = 50)
    
    car_cheap_text.pos =(150,170)
    car_cheap_text.draw()
    screen.draw.text('Cheap', center = (150,170), color = BLACK)
    
    car_expensive_text.pos = (350, 170)
    car_expensive_text.draw()
    screen.draw.text('Expensive', center = (350,170), color = BLACK)
    
    next_button.draw()
    
def loan_choice():
    screen.clear()
    screen.fill(GRAY)
    screen.draw.text("Do you wish to take the Cow Loan (approximately $36,000 in 2020)",center = (250,100), color = GOLD)
    
    
def life_choices():

    next_button.draw()
    screen.clear()
    screen.fill(GRAY)
    screen.draw.text('Lets make some purchases', center = (250,100),color = GOLD)
    car_choice()
    screen.draw.text(str(cadet_life[2]), center = (400,30), color = GOLD)


#blake
def select_mentors():
    screen.fill(GRAY)
    

#blake
def free_weekend():
    screen.fill(GRAY)

    
#blake
def life_event():
   screen.fill(GRAY)


#nick
def army_navy():
    screen.fill(GRAY)

    
#nick
def leave_plans():
    screen.fill(GRAY)

    
#nick
def class_weekend():
    screen.fill(GRAY)



def update():
    screen.fill(GRAY)


    
def on_key_down(key):

    global bool_list
    
    if key == keys.SPACE and bool_list[1] == True:
        bool_list[1] = False
        bool_list[2] = True
        
    
def on_mouse_down(pos,button):
    
    #if button == mouse.LEFT and cadet.collidepoint(pos):
        #print('Open menu')
        #opens menu
    global bool_list
    global cadet_life
    
    if button == mouse.LEFT and next_button.collidepoint(pos):
        x = True
        i = 0
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
      if char_choice == True:
          gender_female = Actor('button_selected')
          cadet_life[1] = 'female'
    if button == mouse.LEFT and gender_male.collidepoint(pos): 
        if char_choice == True:
          gender_male = Actor('button_selected')
          cadet_life[1] = 'male'

    global car_cheap
    global car_expensive
    if button == mouse.LEFT and car_cheap.collidepoint(pos):
      if life_choice == True:
        car_cheap = Actor('button_selected')
        cadet_life[2] = cadet_life[2] - 10000
    if button == mouse.LEFT and car_expensive.collidepoint(pos):
      if life_choice == True:
        car_expensive = Actor('button_selected')
        cadet_life[2] = cadet_life[2] - 20000
      
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

