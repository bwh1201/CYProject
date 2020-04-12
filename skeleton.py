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

life = True
money = []
f_score = 0
karma = 0
#name = input("What is your name?")
#Cadet are stored as a list, [name, alive(bool),
# money(nested list with where it is?), frugal score, karma]
#cadet_life = [name, money]

#global screen variables

show_main = True
welcome = False
game_1 = False

def draw():
    
    if show_main == True:
        home_screen()
        
    if welcome == True:
        welcome_screen()
        
    
    
def home_screen():
    cadet.draw()
    start.draw()
    screen.draw.text('CASH COW', (250,100), color = RED)
    screen.draw.text("START", (375,393), color = GRAY)
       
def welcome_screen():        
    
    if welcome == True:
        
        screen.clear()
        screen.fill(RED)
        welcome_msg.draw()
        
    
def update():
    update_welcome_screen()

 
def update_welcome_screen():
    pass
    
def on_key_down(key):
    if key == keys.SPACE:   
        make_screen('home')
    
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
        
        
    
    
def initial_choices():
    pass
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







