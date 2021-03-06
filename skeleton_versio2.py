'''


'''
import random



#Contsants (sorted alphabetically)

BLACK = (0,0,0)

GOLD = (255,215,0)

GRAY = (138,138,138)

HEIGHT = 500

RED = (200,0,0)

WIDTH = 500





#GLobal Variables (sorted alphabetically)

bio_x = Actor('bio_x')



button1 = Actor('element_grey_rectangle_glossy')



cadet = Actor('cadet')



car_cheap = Actor('car_cheap')



car_cheap_text = Actor('button_default')



car_expensive = Actor('car_expensive')



car_expensive_text = Actor('button_default')



cloud = Actor('cloud')



gender_female = Actor('button_default')



gender_male = Actor('button_default')



mentor_good = Actor('ltccody')



mentor_good_bio = Actor('mentor_good_bio')



mentor_x = Actor('cadet_x')



mentor_x_bio = Actor('cadet_x_hov')



money_talk = Actor('money_split_desc')



next_button = Actor('element_red_rectangle')



no_take = Actor('button_default') 



start = Actor('button_default')



text_rect = Rect((300,240), (100,30))



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

cadet_life['money'] = 1

cadet_life['f_score'] = 0

cadet_life['karma'] = 0



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

control['quit_menu'] = False



def draw():

    print(cadet_life)



    if control['show_main'] == True:

        home_screen()



    if control['welcome'] == True:

        welcome_screen()



    if control['char_choice'] == True:

        gender()



    if control['mentor_choice'] == True:

        select_mentors()



    if control['loan_choice'] == True:

        take_cow_loan()

    

    if control['life_choice'] == True:

        car_choice()

    

    if control['quit_menu'] == True:

        take_quit()

    

    if control['f_weekend'] == True:

        free_weekend()

    

    if control['major_event'] == True:

        life_event()

    

    if control['money_split'] == True:

        money_split()

    

    if control['year_ten'] == True:

        year_ten()

        

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

    welcome_msg.center = (WIDTH/2, HEIGHT/2)

    welcome_msg.draw()



def gender():

    """Offers the user two buttons to select their gender. Modifies

    cadet_lift list to reflect their selections.

    """

    

    screen.clear()

    screen.fill(GRAY)

    screen.draw.text('Select your gender:', center = (250, 100), color = GOLD, fontsize = 64)

    

    gender_male.pos = (150,170)

    gender_male.draw()

    screen.draw.text('Male', center = (150, 170), color = BLACK)

    

    

    gender_female.pos = (350,170)

    gender_female.draw()

    screen.draw.text('Female', center = (350,170), color = BLACK)



def select_mentors():

    """Presents a screen to users which allows them to choose whether or not they'd

    like a mentor through this process. The mentor will always instruct them to 

    follow the safest option.

    """

    screen.clear()

    screen.fill(GRAY)

    screen.draw.text('Select your mentor:', center = (250,50), fontsize = 64, color = GOLD)

    

    mentor_x.draw()

    mentor_x.midleft = (0, 350)



    mentor_good.draw()

    mentor_good.midright = (500, 350)



    screen.draw.text('Cadet X (questionable)', midleft = (0,140), color = BLACK)

    screen.draw.text('Cost = 1 American Burrito/Semester', midleft= (0,200))

    screen.draw.text('LTC Cody (good)', midright = (500,140), color = BLACK)

    screen.draw.text('Cost = $100/Semester', midright = (500,200))



#Procedure: take_cow_loan

#yes or no question

#None -> None 

def take_cow_loan():

    

    screen.clear()

    screen.fill(GRAY)

    yes_take.pos = (150,370)

    yes_take.draw()

    screen.draw.text('Yes', center = (150,370), color = BLACK)

    

    no_take.pos = (350,370)

    no_take.draw()

    screen.draw.text('No', center = (350,370), color = BLACK)

    

    screen.draw.text('Would you like to take the Cow Cash?', center = (250,50), fontsize = 25, color = GOLD)



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



#blake

#Procedure: free_weekend

#Object represets a screen where users can make a decision

# None -> None

def free_weekend():

    """Presents a screen to users asking them how they would spend their free weekend.

    Choices will subtract various amounts of money from users' bank accounts.

    """

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





def money_split():

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

    data = data[:9]

    multiplier = (max(data)-min(data))/len(data)

    return multiplier



def year_ten():

    screen.clear()

    screen.fill(GRAY)

    screen.draw.text("10 Years Later", center = (250, 50), color = GOLD, fontsize = 64)

    

    cadet_life['savings_10'] = interest(cadet_life['savings'], 0.05, 1, 10)

    

    dat = get_stock_data('sandp.txt')

    get_random(dat)

    money_multiplier = get_10_year(dat)

    cadet_life['brokerage_10'] = cadet_life['brokerage']*money_multiplier

    

    screen.draw.text('Savings = ${:.2f}'.format(cadet_life['savings_10']),center = (250, 100),fontsize = 40)

    screen.draw.text('Your savings account has gained \n ${:.2f} \n in 10 years'.format(cadet_life['savings_10']-cadet_life['savings']),center = (250,150), fontsize = 25, color = BLACK)

    screen.draw.text('Brokerage = ${:.2f}'.format(cadet_life['brokerage_10']), center = (250, 300), fontsize = 40)

    screen.draw.text('Your brokerage account has gained \n ${:.2f} \n in 10 years'.format(cadet_life['brokerage_10']-cadet_life['brokerage']),center = (250,350), fontsize = 25, color = BLACK)





def take_quit():

    cadet_life['life'] = False

    screen.clear()

    screen.fill(GRAY)

    take_quit_msg.center = (WIDTH/2, HEIGHT/2)

    take_quit_msg.draw()



def death_screen():

    screen.clear()

    screen.fill(RED)

    

def on_mouse_down(pos, button):

    global cadet_life

    global control

    global gender_female

    global gender_male

    global yes_take

    global no_take

    global mentor_good

    global mentor_x

    global car_cheap

    global car_expensive





    if control['show_main'] == True:

        if button == mouse.LEFT and start.collidepoint(pos):

            control['show_main'] = False

            control['welcome'] = True

            draw()

            

    if control['char_choice'] == True:

        print('char choice')

        if button == mouse.LEFT and gender_female.collidepoint(pos):

            cadet_life['gender'] = 'female'

            control['char_choice'] = False

            control['mentor_choice'] = True

            draw()

            

        if button == mouse.LEFT and gender_male.collidepoint(pos): 

            gender_male = Actor('button_selected')

            cadet_life['gender'] = 'male'

            control['char_choice'] = False

            control['mentor_choice'] = True

            draw()

            