import random

#Contsants (sorted alphabetically)
BLACK = (0,0,0)
BLUE = (0 ,0, 255)
CHARTREUSE = (127,255,0)
GOLD = (255,215,0)
GRAY = (138,138,138)
HEIGHT = 500
RED = (200,0,0)
WIDTH = 500


#GLobal Variables (sorted alphabetically)
big_active = False

bio_x = Actor('bio_x')

button1 = Actor('element_grey_rectangle_glossy')

cadet = Actor('cadet')

car_cheap = Actor('car_cheap')

car_cheap_text = Actor('button_default')

car_expensive = Actor('car_expensive')

car_expensive_text = Actor('button_default')

choice_1 = Actor('element_green_rectangle', (120,250))
choice_2 = Actor('element_blue_rectangle', (250,250))
choice_3 = Actor('element_red_rectangle', (370,250))
choose_a = False
choose_b = False
choose_c = False

cloud = Actor('cloud')

gender_female = Actor('button_default')

gender_male = Actor('button_default')

mentor_x = Actor('cadet_x_hov')
mentor_x_yes = Actor('element_red_rectangle')
mentor_good = Actor('mento_good_bio')
mentor_good_yes = Actor('element_red_rectangle')
ment_select = False

money_talk = Actor('money_split_desc')


next_button = Actor('element_blue_rectangle', (460,470))

no_car = Actor('element_blue_rectangle', (250, 400))

no_take = Actor('button_default') 

start = Actor('button_default')

text_rect = Rect((180,245), (140,30))
text_active = 0
text = 'Click to enter your name'
new_text = ''

take_quit_msg = Actor('take_quit')

vegas = Actor('chip_1')

vermont = Actor('house')

welcome_msg = Actor('welcome')

yes_take = Actor('button_default') 


#User Information
cadet_life = {}
cadet_life['life'] = True
cadet_life['name'] = ''
cadet_life['gender'] = ''
cadet_life['mentor'] = ''
cadet_life['money'] = 36000
cadet_life['stock_data'] = []

#Control dictionary
control = {}
control['show_main'] = True
control['welcome'] = False
control['char_choice'] = False
control['mentor_choice'] = False
control['loan_choice'] = False
control['life_choice'] = False
control['f_weekend'] = False
control['major_event'] = False
control['money_split'] = False
control['year_ten'] = False
control['year_twenty'] = False
control['year_thirty'] = False
control['quit_menu'] = False
control['end'] = False

def draw():
    print(cadet_life)

    if control['show_main'] == True:
        home_screen()

    if control['welcome'] == True:
        welcome_screen()

    if control['char_choice'] == True:
        char_choices()

    if control['mentor_choice'] == True:
        select_mentors()

    #if control['loan_choice'] == True:
        #take_cow_loan()
    
    if control['life_choice'] == True:
        car_choice()
    
    if control['quit_menu'] == True:
        take_quit()
    
    if control['f_weekend'] == True:
        free_weekend()
    
    if control['major_event'] == True:
        big_event()
    
    if control['money_split'] == True:
        money_split()
    
    if control['year_ten'] == True:
        year_ten()
    
    if control['year_twenty'] == True:
        year_twenty()
    
    if control['year_thirty'] == True:
        year_thirty()
    
    if control['end'] ==True:
        the_end()
        
    if cadet_life['money'] <= 0:
        death_screen()


def home_screen():
    """Displays the homescreen of the pygame (background, cadet picture, title"""
    screen.fill(GRAY)
    cadet.pos = (100,300)
    cadet.draw()
    start.center = (400,400)
    start.draw()
    screen.draw.text('CASH COW', (250,100), color = GOLD, fontsize = 64)
    screen.draw.text("START", center = (400,400), color = BLACK)

def welcome_screen():
    screen.clear()
    screen.fill(GRAY) 
    money = Actor('money', (250,250))
    money.draw()
    screen.draw.text('Welcome to CASH COW!',  center = (250,100), color = GOLD, fontsize = 40)
    screen.draw.text('\n This is a game where you can practice spending \n your hard earned cow loan. \n This game was created with cadets in mind. \n Hopefully you have fun and end up making wise choices! \n Enjoy!', center = (250,240), color = BLACK, fontsize = 25)
    screen.draw.text('Created by Nick Ashby and Blake Havern\n \n Press SPACE bar to continue', center = (250,370), color = BLACK, fontsize = 40)
    
   



#procedureL char_choices()
#Objects rep themselves 
#None -> None
def char_choices():
    gender()
    cadet_name()
    take_cow_loan()

def cadet_name():

    global text_active
    global text
    
    screen.draw.text('What is your name? \n (type last name then enter)', center = (250,220), color = GOLD, fontsize = 30)
    if text_active == 1:
        rect_act = screen.draw.filled_rect(text_rect, BLUE)
    elif text_active == 2: 
        rect_act = screen.draw.filled_rect (text_rect, CHARTREUSE)
    else:
        rect_in = screen.draw.filled_rect(text_rect, RED)
    screen.draw.text(text, center = (250,260), color = BLACK, fontsize = 15)
    
def gender():
    """Offers the user two buttons to select their gender. Modifies
    cadet_lift list to reflect their selections.
    """
    
    screen.clear()
    screen.fill(GRAY)
    screen.draw.text('Select your gender:', center = (250, 100), color = GOLD, fontsize = 40)
    
    gender_male.pos = (150,150)
    gender_male.draw()
    screen.draw.text('Male', center = (150, 150), color = BLACK)
    
    
    gender_female.pos = (350,150)
    gender_female.draw()
    screen.draw.text('Female', center = (350,150), color = BLACK)

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
    
    screen.draw.text('NEXT', center = (460,470), fontsize = 15, color = BLACK)
    

#Procedure: take_cow_loan
#yes or no question
#None -> None 
def take_cow_loan():
    
    global yes_take
    global no_take
    
    yes_take.pos = (150,410)
    yes_take.draw()
    no_take.pos = (350, 410)
    no_take.draw()
    screen.draw.text('Yes', center = (150,410), color = BLACK)
    screen.draw.text('No', center = (350,410), color = BLACK)

    #no_take.pos = (350,410)
    #no_take.draw()
    
    screen.draw.text('Click "Yes" to take the Cow Cash!', center = (250,350), fontsize = 40, color = GOLD)

#Procedure: car_choice
#Objects represent two buttons for users to select what 
# car they'd like to buy.
#None -> None
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
    #screen.draw.text("{}".format(cadet_life), center = (250, 100), color = GOLD, fontsize = 15)
    screen.draw.text('Cow loan remaining:  ' + str(cadet_life['money']), center = (250, 100), color = GOLD, fontsize = 15)

    
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
    no_car.draw()
    screen.draw.text('No Car', center = (250,400), color = BLACK)
    
#blake
#Procedure: free_weekend
#Object represets a screen where users can make a decision
# None -> None
def free_weekend():
    """Presents a screen to users asking them how they would spend their free weekend.
    Choices will subtract various amounts of money from users' bank accounts.
    """
    screen.clear()
    screen.fill(GRAY)
    screen.draw.text('Free Weekend!!!', center = (250, 50), color = GOLD, fontsize = 64)
    screen.draw.text("It's Labor Day Weekend. Where do you want to go?", center = (250, 100),color = BLACK, fontsize = 26)
    
    vegas.center = (350,250)
    vegas.draw()
    screen.draw.text("Vegas",center = (350, 350))
    
    vermont.center = (150, 250)
    vermont.draw()
    screen.draw.text('Vermont', center = (150, 350))

#blake
#Procedure: life_event
#Object represents a screen where users can make a decision
# None -> None
def life_event():
    """Presents a user with a random life event (engagement, family member hospitalization, etc) and
    prompts them to respond. Responses will subtract various amounts of money from users' bank accounts.
    """
    screen.fill(GRAY)
    screen.draw.text('MAJOR LIFE EVENT!', center = (250,50), color = GOLD, fontsize = 64)
    num = random.randint(0,100)
    num2 = random.randint(1,cadet_life['money'])
    if num % 2 == 0:
        screen.draw.text("YOU'RE GETTING MARRIED!!!", center = (250,100), fontsize = 26)
        screen.draw.text("This is going to cost you ${}".format(num2), center = (250, 200), fontsize = 26)
        cadet_life['money'] -= num2
        screen.draw.text('Press space to continue', center = (250, 400), fontsize = 20)
    else:
        screen.draw.text("ALCOHOL BOARD :(", center = (250,100), fontsize = 26)
        screen.draw.text("On the bright side, at least you're not spending any money", center = (250,200), fontsize = 20)
        screen.draw.text('Press space to continue', center = (250, 400), fontsize = 20)

def big_event():
    ''' Gives three random choices and displays what your life event is
    '''
    screen.clear()
    screen.fill(GRAY)

    global choose_a
    global choose_b
    global choose_c
    
    if choose_a:
        choice_a()
    elif choose_b:
        choice_b()
    elif choose_c:
        choice_c()
    else:
        screen.draw.text('Choose option A, B, or C', center = (250,50))
        screen.draw.text('A', center = (120,220), fontsize = 40)
        screen.draw.text('B', center = (250,220), fontsize = 40)
        screen.draw.text('C', center = (370,220), fontsize = 40)
    
        choice_1.draw()
        choice_2.draw()
        choice_3.draw()
    
    next_button.draw()
    screen.draw.text('NEXT', center = (460,470), fontsize = 15, color = BLACK)

    
    
    
def choice_a():
    global cadet_life
    screen.clear()
    num = random.randint(0,11)
    
    if num % 2 == 0 :
        screen.fill(RED)
        screen.draw.text('You chose choice A.  \n A stands for Alcohol Board! \n At the least your saving money!\n \n Click next', center = (250,250), fontsize = 30, color = BLACK)
        screen.draw.text('Current Balance: ' + str(cadet_life['money']), center = (250,400), fontsize = 35, color = BLACK)
    else: 
        screen.fill(CHARTREUSE)
        screen.draw.text('You chose choice A.  \n You\'re getting married! Congrats! \n Slightly expensive... \n \n Click next', center = (250,250), fontsize = 30, color = BLACK)
        cadet_life['money'] -= 2000
        screen.draw.text('-2000', center = (250,350), fontsize = 35, color = RED)
        screen.draw.text('Current Balance: ' + str(cadet_life['money']), center = (250,400), fontsize = 35, color = BLACK)

    
def choice_b():
    global cadet_life
    screen.clear()
    
    num = random.randint(0,11)
    
    if num % 4 == 0 :
        screen.fill(CHARTREUSE)
        screen.draw.text('You chose choice B. \n You just won the lottery! \n Here is an extra $10k\n \n Click next', center = (250,250), fontsize = 30, color = BLACK)
        cadet_life['money'] += 10000
        screen.draw.text('+10000', center = (250,350), fontsize = 35, color = BLUE)
        screen.draw.text('Current Balance: ' + str(cadet_life['money']), center = (250,400), fontsize = 35, color = BLACK)
    else: 
        screen.fill(RED)
        screen.draw.text('Current Balance: ' + str(cadet_life['money']), center = (250,400), fontsize = 35, color = BLACK)
        screen.draw.text('You chose choice B. \n B stands for BOARD! \n At the least your saving money!\n \n Click next', center = (250,250), fontsize = 30, color = BLACK)
        
    
def choice_c():
    global cadet_life
    screen.clear()
    
    num = random.randint(0,100)
    
    if num % 5 == 0 :
        screen.fill(RED)
        screen.draw.text('You chose choice C.  \n C stands for CORONA! \n That means markets crash! Bye bye money!\n \n Click next', center = (250,250), fontsize = 30, color = BLACK)
        cadet_life['money'] -= 3000
        screen.draw.text('-3000', center = (250,350), fontsize = 35, color = GOLD)
        screen.draw.text('Current Balance: ' + str(cadet_life['money']), center = (250,400), fontsize = 35, color = BLACK)
    else: 
        screen.fill(CHARTREUSE)
        screen.draw.text('You chose choice C. \n C stands for CHILLING. \n Nothing major happened in your life. \n \n Click next', center = (250,250), fontsize = 30, color = BLACK)
        screen.draw.text('Current Balance: ' + str(cadet_life['money']), center = (250,400), fontsize = 35, color = BLACK)
    
def money_split():
    screen.clear()
    screen.fill(GRAY)
    money_talk.draw()
    screen.draw.text('What percent of your ${} \n would you like to put in a brokerage account?'.format(cadet_life['money']), center = (250,250), fontsize = 30, color = GOLD)
    screen.draw.text('(1 = 10%, 2 = 20%, 3 = 30%...)', center = (250, 300))
    screen.draw.text('click anywhere to continue', center = (250,400), color = BLACK)

def interest(P,r,n,t):
    amount = P*(1+(r/n))**(n*t)
    return amount

def get_stock_data(InFile):
    new = []
    InFile = open(InFile, 'r')
    for line in InFile:
        line = line.strip()
        new.append(float(line))
    InFile.close()
    return new

def get_random(data):
    random.shuffle(data)
    return data

def get_10_year(data):
    data = data[:10]
    multiplier = (max(data)-min(data))/len(data)
    return multiplier

def get_20_year(data):
    data = data[11:21]
    multiplier = (max(data)-min(data))/len(data)
    return multiplier

def get_30_year(data):
    data = data[22:32]
    multiplier = (max(data)-min(data))/len(data)
    return multiplier

def year_ten():
    screen.clear()
    screen.fill(GRAY)
    screen.draw.text("10 Years Later", center = (250, 50), color = GOLD, fontsize = 64)
    screen.draw.text('Welcome CPT {}'.format(cadet_life['name']), center = (250, 100), color = GOLD, fontsize = 32)
    cadet_life['savings_10'] = interest(cadet_life['savings'], 0.05, 1, 10)
    
    dat = get_stock_data('sandp.txt')
    get_random(dat)
    money_multiplier = get_10_year(dat)
    cadet_life['stock_data'] = dat
    cadet_life['brokerage_10'] = cadet_life['brokerage']*money_multiplier
    
    screen.draw.text('Savings = ${:.2f}'.format(cadet_life['savings_10']),center = (250, 200),fontsize = 40)
    screen.draw.text('Your savings account has gained \n ${:.2f} \n in 10 years'.format(cadet_life['savings_10']-cadet_life['savings']),center = (250,250), fontsize = 25, color = BLACK)
    screen.draw.text('Brokerage = ${:.2f}'.format(cadet_life['brokerage_10']), center = (250, 300), fontsize = 40)
    screen.draw.text('Your brokerage account has gained \n ${:.2f} \n in 10 years'.format(cadet_life['brokerage_10']-cadet_life['brokerage']),center = (250,350), fontsize = 25, color = BLACK)
    screen.draw.text('Press enter to continue', center = (250, 450), fontsize = 30, color = BLACK)
    
def year_twenty():
    screen.clear()
    screen.fill(GRAY)
    screen.draw.text("20 Years Later", center = (250, 50), color = GOLD, fontsize = 64)
    screen.draw.text('Welcome LTC {}'.format(cadet_life['name']), center = (250, 100), color = GOLD, fontsize = 32)
    
    dat = cadet_life['stock_data']
    money_multiplier = get_20_year(dat)
    cadet_life['brokerage_20'] = cadet_life['brokerage_10']*money_multiplier
    cadet_life['savings_20'] = interest(cadet_life['savings_10'], 0.05, 1, 10)
    
    screen.draw.text('Savings = ${:.2f}'.format(cadet_life['savings_20']),center = (250, 200),fontsize = 40)
    screen.draw.text('Your savings account has gained \n ${:.2f} \n in 20 years'.format(cadet_life['savings_20']-cadet_life['savings']),center = (250,250), fontsize = 25, color = BLACK)
    screen.draw.text('Brokerage = ${:.2f}'.format(cadet_life['brokerage_20']), center = (250, 300), fontsize = 40)
    screen.draw.text('Your brokerage account has gained \n ${:.2f} \n in 20 years'.format(cadet_life['brokerage_20']-cadet_life['brokerage']),center = (250,350), fontsize = 25, color = BLACK)
    screen.draw.text('Click anywhere to continue', center = (250, 450), fontsize = 30, color = BLACK)

def year_thirty():
    screen.clear()
    screen.fill(GRAY)
    screen.draw.text("30 Years Later", center = (250, 50), color = GOLD, fontsize = 64)
    screen.draw.text('Welcome BG {}'.format(cadet_life['name']), center = (250, 100), color = GOLD, fontsize = 32)
    
    dat = cadet_life['stock_data']
    money_multiplier = get_30_year(dat)
    cadet_life['brokerage_30'] = cadet_life['brokerage_20']*money_multiplier
    cadet_life['savings_30'] = interest(cadet_life['savings_20'], 0.05, 1, 10)
    
    screen.draw.text('Savings = ${:.2f}'.format(cadet_life['savings_30']),center = (250, 200),fontsize = 40)
    screen.draw.text('Your savings account has gained \n ${:.2f} \n in 30 years'.format(cadet_life['savings_30']-cadet_life['savings']),center = (250,250), fontsize = 25, color = BLACK)
    screen.draw.text('Brokerage = ${:.2f}'.format(cadet_life['brokerage_30']), center = (250, 300), fontsize = 40)
    screen.draw.text('Your brokerage account has gained \n ${:.2f} \n in 30 years'.format(cadet_life['brokerage_30']-cadet_life['brokerage']),center = (250,350), fontsize = 25, color = BLACK)
    screen.draw.text('Press enter to continue', center = (250, 450), fontsize = 30, color = BLACK)

def the_end():
    screen.clear()
    screen.fill(CHARTREUSE)
    
    money = Actor('money', (250,250))
    money.draw()
    screen.draw.text('You have reached the end', center = (250, 100), fontsize = 30, color = BLACK)
    screen.draw.text('You ended your journey\n with a now meaningless ' + str(cadet_life['car']) + ' car \n and $' + str(cadet_life['money']) + ' in savings', center = (260,300), fontsize = 30, color = BLACK)
    
def take_quit():
    cadet_life['life'] = False
    screen.clear()
    screen.fill(GRAY)
    take_quit_msg.center = (WIDTH/2, HEIGHT/2)
    take_quit_msg.draw()

def death_screen():
    screen.clear()
    screen.fill(RED)
    screen.draw.text('Uh-Oh something went wrong', center = (250, 250))
    
def on_mouse_down(pos, button):
    global cadet_life
    global control
    global gender_female
    global gender_male
    global yes_take
    global no_take
    global mentor_good
    global mentor_good_yes
    global mentor_x_yes
    global mentor_x
    global car_cheap
    global car_expensive
    global text_active
    global no_car

    if control['show_main'] == True:
        if button == mouse.LEFT and start.collidepoint(pos):
            control['show_main'] = False
            control['welcome'] = True
            draw()
            
    if control['char_choice'] == True:
        print('char choice')
        if button == mouse.LEFT and gender_female.collidepoint(pos):
            gender_female = Actor('button_selected')
            gender_male = Actor('button_default')
            cadet_life['gender'] = 'female'
            #control['char_choice'] = False
            #control['mentor_choice'] = True
            draw()
            
        if button == mouse.LEFT and gender_male.collidepoint(pos): 
            gender_male = Actor('button_selected')
            gender_female = Actor('button_default')
            cadet_life['gender'] = 'male'
            #control['char_choice'] = False
            #control['mentor_choice'] = True
            draw()
            
        if button == mouse.LEFT and yes_take.collidepoint(pos):
            cadet_life['money'] = 36000
            control['life_choice'] = False
            control['char_choice'] = False
            control['mentor_choice'] = True
            draw()
        
        if button == mouse.LEFT and no_take.collidepoint(pos):
            cadet_life['money'] = 10
            control['char_choice'] = False
            control['quit_menu'] = True
        
        if button == mouse.LEFT and text_rect.collidepoint(pos):
            text_active = True
            
    if control['mentor_choice'] == True:
        if button == mouse.LEFT and mentor_x_yes.collidepoint(pos):
            cadet_life['karma'] = .5
            cadet_life['mentor'] = 'x'
            mentor_good_yes = Actor('element_red_rectangle')
            mentor_x_yes = Actor('element_green_rectangle')
        
        if button == mouse.LEFT and mentor_good_yes.collidepoint(pos):
            cadet_life['karma'] = 2
            cadet_life['mentor'] = 'good'
            mentor_x_yes = Actor('element_red_rectangle')
            mentor_good_yes = Actor('element_green_rectangle')
        
        if button == mouse.LEFT and next_button.collidepoint(pos):
            control['mentor_choice'] = False
            control['life_choice'] = True
 
                 
    if control['life_choice'] == True:
        if button == mouse.LEFT and car_cheap_text.collidepoint(pos):
            cadet_life['money'] = cadet_life['money'] - 10000
            cadet_life['car'] = 'cheap'
            control['life_choice'] = False
            control['f_weekend'] = True
            
        if button == mouse.LEFT and car_expensive_text.collidepoint(pos):
            cadet_life['money'] = cadet_life['money'] - 20000
            cadet_life['car'] = 'expensive'
            control['life_choice'] = False
            control['f_weekend'] = True
            
        if button == mouse.LEFT and no_car.collidepoint(pos):
            cadet_life['car'] = None
            control['life_choice'] = False
            control['f_weekend'] = True
            
    if control['f_weekend'] == True:
        if button == mouse.LEFT and vermont.collidepoint(pos):
            cadet_life['money'] = cadet_life['money'] - 500
            control['f_weekend'] = False
            control['major_event'] = True
            print(cadet_life)
            draw()
    #put this under if winter_break?  
    
        if button == mouse.LEFT and vegas.collidepoint(pos):
            cadet_life['money'] = cadet_life['money'] - 2000
            control['f_weekend'] = False
            control['major_event'] = True
            print(cadet_life)
            draw()
    
    if control['money_split'] == True:
        if button == mouse.LEFT:
            control['money_split'] = False
            control['year_ten'] = True
    global choose_a
    global choose_b
    global choose_c
    if control['major_event'] == True:
        if button == mouse.LEFT and choice_1.collidepoint(pos):
            choose_a = True
        if button == mouse.LEFT and choice_2.collidepoint(pos):
            choose_b = True
        if button == mouse.LEFT and choice_3.collidepoint(pos):
            choose_c = True
        if button == mouse.LEFT and next_button.collidepoint(pos):
            control['money_split'] = True
    
    if control['year_twenty'] == True:
        if button == mouse.LEFT:
            control['year_twenty'] = False
            control['year_thirty'] = True
            
    if control['year_thirty'] == True:
        if button == mouse.LEFT:
            control['year_thirty'] = False
            control['end'] = True    

            
def on_key_down(key):
    """Recieves a keystroke on the spacebar. Advances the control loop by 1 to begin the
    simulation.
    """
    if control['welcome'] == True:
        if key == keys.SPACE:
            control['welcome'] = False
            control['char_choice'] = True
    
    if control['quit_menu'] == True:
        if key == keys.SPACE:
            control['quit_menu'] = False
            control['life_choice'] = True
    
    if control['major_event'] == True:
        if key == keys.SPACE:
            control['major_event'] = False
            control['money_split'] = True
            draw()
    
    if control['money_split'] == True:
        if key == keys.K_1:
            cadet_life['brokerage'] = cadet_life['money']*0.1
            cadet_life['savings'] = cadet_life['money'] - cadet_life['brokerage']
            cadet_life['money'] = cadet_life['savings']+cadet_life['brokerage']

        elif key == keys.K_2:
            cadet_life['brokerage'] = cadet_life['money']*0.2
            cadet_life['savings'] = cadet_life['money'] - cadet_life['brokerage']
            cadet_life['money'] = cadet_life['savings']+cadet_life['brokerage']

        elif key == keys.K_3:
            cadet_life['brokerage'] = cadet_life['money']*0.3
            cadet_life['savings'] = cadet_life['money'] - cadet_life['brokerage']
            cadet_life['money'] = cadet_life['savings']+cadet_life['brokerage']

        elif key == keys.K_4:
            cadet_life['brokerage'] = cadet_life['money']*0.4
            cadet_life['savings'] = cadet_life['money'] - cadet_life['brokerage']
            cadet_life['money'] = cadet_life['savings']+cadet_life['brokerage']

        elif key == keys.K_5:
            cadet_life['brokerage'] = cadet_life['money']*0.5
            cadet_life['savings'] = cadet_life['money'] - cadet_life['brokerage']
            cadet_life['money'] = cadet_life['savings']+cadet_life['brokerage']

        elif key == keys.K_6:
            cadet_life['brokerage'] = cadet_life['money']*0.6
            cadet_life['savings'] = cadet_life['money'] - cadet_life['brokerage']
            cadet_life['money'] = cadet_life['savings']+cadet_life['brokerage']

        elif key == keys.K_7:
            cadet_life['brokerage'] = cadet_life['money']*0.7
            cadet_life['savings'] = cadet_life['money'] - cadet_life['brokerage']
            cadet_life['money'] = cadet_life['savings']+cadet_life['brokerage']

        elif key == keys.K_8:
            cadet_life['brokerage'] = cadet_life['money']*0.8
            cadet_life['savings'] = cadet_life['money'] - cadet_life['brokerage']
            cadet_life['money'] = cadet_life['savings']+cadet_life['brokerage']

        elif key == keys.K_9:
            cadet_life['brokerage'] = cadet_life['money']*0.9
            cadet_life['savings'] = cadet_life['money'] - cadet_life['brokerage']
            cadet_life['money'] = cadet_life['savings']+cadet_life['brokerage']

        elif key == keys.K_0:
            cadet_life['brokerage'] = cadet_life['money']*0.0
            cadet_life['savings'] = cadet_life['money'] - cadet_life['brokerage']
            cadet_life['money'] = cadet_life['savings']+cadet_life['brokerage']
            
        draw()

    if control['year_ten'] == True:
        if key == keys.RETURN:
            control['year_ten'] = False
            control['year_twenty'] = True
        draw()
    

       
        
    global bool_list
    global text_active
    global text
    global new_text
    
    if text_active == 1:
        
        if key == keys.RETURN:
            cadet_life['name'] = text
            text_active = 2
            
        elif key == keys.BACKSPACE:
            new_text -= new_text[:-1]
        else:
            letter = str(key)
            new_text += letter[-1]
            
        text = new_text + '' 
        