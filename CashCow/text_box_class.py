'''
Name: Blake Havern
File: text_box_class.py
'''
import pygame as pg
pg.init()
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None,32)
BLACK = (0,0,0)

class InputBoxZero:
    def __init__(self,x,y,w,h,text = ''):
        self.rect = pg.Rect((x, y), (w, h))
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
    
    #if user clicks box
    def on_mouse_down(self,pos,button):
        if self.rect.collidepoint(pos):
            #toggle active
            self.active = not self.active
        else:
            self.active = False
        
    def on_key_down(self,key):
        if self.active:
            if key == K_RETURN:
                print(self.text)
            elif key == K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += unicode
            #recreate text
            self.txt_surface = FONT.render(self.text, True, self.color)
            
    def update(self):
        width = max(200,self.txt_surface.get_width()+10)
        self.rect.w = width
    
    def drawInput(self,screen):
        screen.draw.text('Enter your name:', center = (350,263), color = BLACK, fontsize = 15)
        screen.draw.rect(self.rect,self.color)    



COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None,32)

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
    
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
            self.txt_surface = FONT.render(self.text, True, self.color)
    
    def update(self):
        width = max(200,self.txt_surface.get_width()+10)
        self.rect.w = width
    
    def drawInput(self,screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen,self.color,self.rect,2)
                
                
                
                