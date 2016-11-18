## -------------------------------------------------------------------- IMPORTS

import pygame, sys, random
pygame.font.init()

## -------------------------------------------------------------------- CLASSES
## --------- BASIC ---------
class Enemy:
    def __init__(self):
        self.pos = (random.randint(1,760), random.randint(1,560))
        self.speed = (random.randint(-50,50), random.randint(-50,50))
        self.color = (random.randint(50,200),random.randint(50,200),random.randint(50,200))
        self.size = (random.randint(10,35),random.randint(10,35))
        self.current_size = (0,0)
        self.growing = True
        return
    def move(self):
        x = self.pos[0] + (self.speed[0] * timer.get_frame_duration())
        y = self.pos[1] + (self.speed[1] * timer.get_frame_duration())
        self.pos = (x, y)
        self.bounce()      
        gameDisplay.fill(self.color, rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])
        return
    
    def bounce(self):
        if self.pos[0] > (800-self.size[0]) or self.pos[0] < 0:
            self.speed = (self.speed[0]*-1, self.speed[1])
        if self.pos[1] > (600-self.size[1]) or self.pos[1] < 0:
            self.speed = (self.speed[0], self.speed[1]*-1)
        return
        
    def spawn(self):
        if self.current_size > self.size:
            self.growing = False
        else:
            self.current_size = (self.current_size[0]+self.size[0]/100,self.current_size[1]+self.size[1]/100)
        gameDisplay.fill(self.color, rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])
    def __str__(self):
        return '('+str(self.pos)+','+str(self.speed)+','+str(self.color)+','+str(self.size)+')'
    
class Character:
    def __init__(self,pos):
        self.x0=pos[0]
        self.y0=pos[1]
        self.size = (30,30)
       
    def is_Touching(self,pos,height,width):
        x=[self.x0,pos[0]] # character x,  enemy x  Anything 0 is character
        y=[self.y0,pos[1]] # character y,  enemy y  Anything 1 is enemy
        w=[self.size[0],width]
        h=[self.size[1],height]
        
        if (x[1]+w[1]>=x[0]>=x[1]) and (y[1]+h[1]>=y[0]>=y[1]):
            return True
        if (x[0]+w[0]>=x[1]>=x[0]) and (y[1]+h[1]>=y[0]>=y[1]):
            return True
        if (x[0]+w[0]>=x[1]>=x[0]) and (y[0]+h[0]>=y[1]>=y[0]):
            return True
        if (x[1]+w[1]>=x[0]>=x[1]) and (y[0]+h[0]>=y[1]>=y[0]):
            return True 
        return False
        
    def set_Location(self,loc):
        self.x0=loc[0]-15
        self.y0=loc[1]-15    
            
    def render(self):
        gameDisplay.fill((0,0,0),rect=[self.x0,self.y0,self.size[1],self.size[0]])


class Clock:
    def __init__(self):
        self.frame_duration = 0.00
        self.this_frame_time = 0
        self.last_frame_time = 0
        return 
    
    def tick(self):
        self.this_frame_time = self.get_time()
        self.frame_duration = (self.this_frame_time - self.last_frame_time) / 1000.000
        self.last_frame_time = self.this_frame_time
        return
    
    def get_time(self):
        return pygame.time.get_ticks()

    def get_frame_duration(self):
        return self.frame_duration
    
    def begin(self):
        self.last_frame_time = self.get_time()
        return

## --------- MODE 1 ---------
class Box_Laser:
    def __init__(self):
        self.size = (40,40)
        self.pos = possible_pos[random.randint(0,len(possible_pos)-1)]
        possible_pos.remove(self.pos)
        self.color = (175,1,1)
        self.current_color = [5,1,1]
        self.current_size = (0,0)
        self.growing = True 
        self.charging = False
        self.count = 0
        self.gone = False
        self.lasers = False
        self.new_pos = (0,0)
        return
    
    def spawn(self):
        if self.current_size > self.size:
            self.growing = False
        else:
            self.current_size = (self.current_size[0]+self.size[0]/300,self.current_size[1]+self.size[1]/300)
        gameDisplay.fill((5,1,1), rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])  
        
        gameDisplay.fill((5,1,1), rect=[self.pos[0]+10,self.pos[1]-20,self.current_size[0]/2,self.current_size[1]/2]) 
              
        gameDisplay.fill((5,1,1), rect=[self.pos[0]-20,self.pos[1]+10,self.current_size[0]/2,self.current_size[1]/2]) 
       
        gameDisplay.fill((5,1,1), rect=[self.pos[0]+40,self.pos[1]+10,self.current_size[0]/2,self.current_size[1]/2])    
           
        gameDisplay.fill((5,1,1), rect=[self.pos[0]+10,self.pos[1]+40,self.current_size[0]/2,self.current_size[1]/2])      
        return    
    
    def charge(self):
        if self.current_color[0] < 255:
            self.charging = True
            self.current_color[0] += 1
            self.new_pos=self.pos
            gameDisplay.fill(self.current_color, rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])         
            gameDisplay.fill((5,1,1), rect=[self.pos[0]+10,self.pos[1]-20,self.current_size[0]/2,self.current_size[1]/2])
            gameDisplay.fill((5,1,1), rect=[self.pos[0]-20,self.pos[1]+10,self.current_size[0]/2,self.current_size[1]/2])
            gameDisplay.fill((5,1,1), rect=[self.pos[0]+40,self.pos[1]+10,self.current_size[0]/2,self.current_size[1]/2])        
            gameDisplay.fill((5,1,1), rect=[self.pos[0]+10,self.pos[1]+40,self.current_size[0]/2,self.current_size[1]/2])
        elif self.count == 250 and not self.gone:      
            self.color = (self.color[0]+(255-self.color[0])/10,self.color[1]+(255-self.color[1])/10,self.color[2]+(255-self.color[2])/10)
            gameDisplay.fill(self.color, rect=[self.pos[0]+10,0,20,1000])
            gameDisplay.fill(self.color, rect=[0,self.pos[1]+10,1000,20])
            #gameDisplay.fill(self.color, rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])
        else:      
            self.charging = False
            self.lasers = True
            gameDisplay.fill(self.color, rect=[self.pos[0]+10,0,20,1000])
            gameDisplay.fill(self.color, rect=[0,self.pos[1]+10,1000,20])
            #gameDisplay.fill(self.color, rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]]) 
            self.count += 1 
        if self.color[1] > 245:
            self.gone = True
            self.lasers = False
        return


class Chaser_Enemy:
    def __init__(self):
        self.pos = (random.randint(1,760), random.randint(1,560))
        self.color = (random.randint(200,250),random.randint(200,250),random.randint(200,250))
        self.size = (30,30)
        self.current_size = (0,0)
        self.growing = True
        self.speed = random.randint(10,30)
        return
        
    def spawn(self):
        if self.current_size > self.size:
            self.growing = False
        else:
            self.current_size = (self.current_size[0]+self.size[0]/100,self.current_size[1]+self.size[1]/100)
        gameDisplay.fill((random.randint(200,250),random.randint(200,250),random.randint(200,250)), rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])
        return
        
    def chase(self, player):
        x = self.pos[0] + (((player.x0)-self.pos[0]) * timer.get_frame_duration() *1.8 )
        y = self.pos[1] + (((player.y0)-self.pos[1]) * timer.get_frame_duration() *1.8 )
        self.pos = (x,y)
        gameDisplay.fill(self.color, rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])
        return
        
    def __str__(self):
        return '('+str(self.pos)+','+str(self.speed)+','+str(self.color)+','+str(self.size)+')'

## --------- MODE 2 ---------
class Coll:
    def __init__(self):
        self.pos = (random.randint(1,w_board-35), random.randint(1,h_board-35))
        self.color = ( reds[random.randint(0,len(reds)-1)],0,0)
        self.size = (20,20)
        self.current_size = (0,0)
        self.growing = True
        return
    def spawn(self):
        if self.current_size > self.size:
            self.growing = False
        else:
            self.current_size = (self.current_size[0]+self.size[0]/100,self.current_size[1]+self.size[1]/100)
        gameDisplay.fill( (random.randint(c_minred,c_maxred),0,0), \
            rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])        
    def deactivate(self):
        gameDisplay.fill( (224,224,224), \
            rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])         
    def emphasis(self,i):
        ##outside
        out_rect = [self.pos[0]-i,self.pos[1]-i,self.current_size[0]+2*i,self.current_size[1]+2*i]
        gameDisplay.fill( (grays[i],grays[i],grays[i]), \
            rect=out_rect )         
    def render(self,i): 
        ##main
        gameDisplay.fill( (reds[i],0,0), \
            rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]] )
        
    def __str__(self):
        return '('+str(self.pos)+','+str(self.speed)+','+str(self.color)+','+str(self.size)+')' 
    
## --------- DISPLAY -------
class Button:
    def __init__(self,size_w, size_h, pos_w, pos_h, fr_w, fr_act, fill_color, accent_color, selection_color, text=None, txt_style=pygame.font.SysFont('consolas',42) ):
        '''
        ( size , position , frame width, is fr active? (bool) , all collors are (R,G,B) tuple,
          (text can be string, not needed & defaults to None) )
        '''
        self.size = (size_w,size_h)
        self.pos = (pos_w,pos_h)
        self.fr = {'act': fr_act, 'w': fr_w, 'size':(self.size[0]+2*fr_w, self.size[1]+2*fr_w), 'pos':(self.pos[0]-fr_w,self.pos[1]-fr_w)}
        self.color = {'fill': fill_color, 'acc': accent_color, 'sel': selection_color, 'text': accent_color}
        self.text = text
        self.active = False
        self.txtstyle = txt_style
    
    def render(self):
        ## rendering active colored frame if button active
        if self.active == True:
            gameDisplay.fill(  self.color['sel'], rect=[  \
                self.pos[0]-self.fr['w'],  self.pos[1]-self.fr['w'], \
                self.size[0]+self.fr['w'], self.size[1]+self.fr['w']  ]   )
        ## rendering button frame if frame active
        elif self.fr['act'] == True:
            gameDisplay.fill(  self.color['acc'], rect=[  \
                self.fr['pos'][0],  self.fr['pos'][1],    \
                self.fr['size'][0], self.fr['size'][1]]   )
        ## rendering button fill
        gameDisplay.fill(  self.color['fill'], rect=[self.pos[0], self.pos[1], self.size[0], self.size[1]]  ) 
        ## rendering button text, if any
        if self.text != None:
            text_size = self.txtstyle.size(self.text)
            loc_t = relative_center(self.size, text_size)
            button_text = self.txtstyle.render(self.text,1,self.color['text'])
            gameDisplay.blit( button_text, (self.pos[0]+loc_t[0], self.pos[1]+loc_t[1]) ) ## displaying text in center of button
class Textbox:
    def __init__(self,size_w, size_h, pos_w, pos_h, text, txt_color,txt_style=pygame.font.SysFont('consolas',42)):
        self.size = (size_w, size_h)
        self.pos = (pos_w, pos_h)
        self.text = text
        self.color = txt_color
        self.txtstyle = txt_style
    
    def render(self):
        text_size = self.txtstyle.size(self.text)
        loc_t = relative_center(self.size, text_size)
        box_text = self.txtstyle.render(self.text,1,self.color)
        gameDisplay.blit( box_text, (self.pos[0]+loc_t[0], self.pos[1]+loc_t[1]) ) ## displaying text in center of box    
    
'''
        
class Menu:
    def __init__(cd):
        if cd == 'main':
            self.color = (light_blue,white,teal) #(background color, accent color -- buttons, font, frame, etc, selection color)
        elif cd == 'exit':
            self.color = (black,white,black) #(background color, accent color -- buttons, font, frame, etc, selection color)
        else:
            self.color = (white,black,red) #(background color, accent color -- buttons, font, frame, etc, selection color
'''

## --------- MISC  ---------
def circle_freeze():
    pygame.draw.circle(gameDisplay,red,( char.x0+15,char.y0+15 ),40,2)
    pygame.display.update()
    pygame.time.delay(1250)

def hover(cursor_loc, button_size, button_pos):
    if (cursor_loc[0] in range(button_pos[0],button_pos[0]+button_size[0])) and \
       (cursor_loc[1] in range(button_pos[1],button_pos[1]+button_size[1])):
        return True
    return False
    
def relative_center(coord_out, coord_in):
    c_o = (coord_out[0]//2, coord_out[1]//2) ## coord of center point of outside (relative to itself)
    c_i = (coord_in[0]//2,  coord_in[1]//2) ## coord of center point of inside (relative to itself)
    rel_center = (c_o[0]-c_i[0],c_o[1]-c_i[1]) ## coord of loc of inside so it is centered with respect to outside
    return rel_center
        

## ---------------------------------------------------------------- PYGAME.INIT

## -------------------------------------------------------------------- GLOBALS
## COLORS
black,white,red, = (0,0,0),(255,255,255),(255,0,0)
light_blue,teal = (0,255,255),(0,200,200)

col=[255,0]

## bright red to maroony red
c_minred = 150
c_maxred = 235
reds = list(range(c_minred,c_maxred,3))+[c_maxred]+list(range(c_maxred,c_minred,-3))
c_maxgray = 254
c_mingray = c_maxgray-(len(reds)-1)//2
grays = list(range(c_maxgray,c_mingray,-1))+[c_mingray]+list(range(c_mingray,c_maxgray,1))

## FONTS
'''
font=pygame.font.SysFont('consolas',48)
font2=pygame.font.SysFont('consolas',28)
'''

heading1=pygame.font.SysFont('consolas',52)
heading2=pygame.font.SysFont('consolas',42)
body1=pygame.font.SysFont('consolas',32)
body2=pygame.font.SysFont('consolas',28)
body3=pygame.font.SysFont('consolas',22)
mini1=pygame.font.SysFont('consolas',18)



## --------------------------------------------------------------- INITIALIZING

## OBJECT LISTS (keep track of which objects are present in the board)
box_laser_list = []
chaser_list = [] 
enemy_list = []
coll_list = []

##POSSIBLE POSITION
possible_pos = [(380,280),(100,100),(100,460),(660,100),(660,460)]

## TIMER SETUP
timer = Clock()
timer.begin()

tick_interval = 1.00
tick_time = 0

delay_duration = 5

## SURFACE SETUP (what goes inside is tuple of parameters, don't forget double parenthesis)
w_board = 800 ## board width
h_board = 600 ## board height
gameDisplay = pygame.display.set_mode( (w_board,h_board) )


## DISPLAY SETUP

pygame.display.set_caption("Pyxel")     ## window title

## ENEMY SETUP
enemy = Enemy()
enemy_list.append(enemy)

## CHARACTER SETUP
char = Character((400,300))

## COLL SETUP
ct_collected = 0     ## number of collected coll in mode 2
rd = 0              ## counts how many enemy spawns since last collectible
every_rd = 3        ## new collectible every 3 enemy spawn
red_ind = 0 ## counts index of reds list (color of colls)
red_interval = 2 ## how many cycles before red color increases
round_ct = 0 ## counts cycles since last red change


## LOGIC
sequence=True
gameExit=False
menuState=True
gameState=False
exitState=False

hasClick=False
mode1=False
mode2=False


## BUTTONS and TEXTBOXES
b = 30 ## buffer around edge (10 px)
p = 15 ## padding around button (for text)

## buttons_init
## top
button_t_fr = 10
button_t_size = (180,80)

button_tL = Button(button_t_size[0], button_t_size[1], \
                   b+button_t_fr, b+button_t_fr, \
                   button_t_fr, False, white, light_blue, teal, 'Mode 1')

button_tR = Button(button_t_size[0], button_t_size[1], \
                   w_board-button_t_size[0]-button_t_fr-b, b+button_t_fr, \
                   button_t_fr, False, white, light_blue, teal, 'Mode 2')
## center button
button_c_fr = 10
button_c_size = (360,110)
button_c_loc = relative_center((w_board,h_board),(button_c_size))

button_c = Button(button_c_size[0], button_c_size[1], \
                           button_c_loc[0], button_c_loc[1], \
                           button_c_fr, True, light_blue, white, red, 'Play Mode', heading1)

## center txtbox
txtbox_c_size = (360,110)
txtbox_c_loc = relative_center((w_board,h_board),(txtbox_c_size))
txtbox_c = Textbox(txtbox_c_size[0], txtbox_c_size[1], \
                   txtbox_c_loc[0], txtbox_c_loc[1]//2, \
                   'Game Over', white, heading1)
txtbox_d_size = (360,110)
txtbox_d_loc = relative_center((w_board,h_board),(txtbox_d_size))
txtbox_d = Textbox(txtbox_d_size[0], txtbox_d_size[1], \
                   txtbox_d_loc[0], txtbox_d_loc[1], \
                   '', white, heading2)

txtbox_cred_size = (460,110)
txtbox_cred_loc = relative_center((w_board,h_board),(txtbox_d_size))
txtbox_cred = Textbox(txtbox_d_size[0], txtbox_d_size[1], \
                   txtbox_d_loc[0], txtbox_d_loc[1]+250, \
                   'A game by Won Jong Lee, Dylan Moody and Herta Calvo-Faugier', white, mini1)

## gameinfo textbox
txtbox_g_size = (w_board-2,150)
txtbox_g_loc = relative_center((w_board,h_board),(txtbox_g_size))
txtbox_g_loc = (txtbox_g_loc[0], txtbox_g_loc[1] + 110)
txtbox_g = Textbox(txtbox_g_size[0], txtbox_g_size[1], \
                   txtbox_g_loc[0], txtbox_g_loc[1], \
                   'BANANA', white, body2)

## bottom buttons
button_b_fr = 10
button_b_size = (180,80)

button_bL = Button(button_b_size[0], button_b_size[1], \
                   b+button_b_fr, h_board-b-button_b_fr-button_b_size[1], \
                   button_b_fr, False, white, black, teal, 'Exit')

button_bR = Button(button_b_size[0], button_b_size[1], \
                   w_board-button_b_size[0]-button_b_fr-b, h_board-b-button_b_fr-button_b_size[1], \
                   button_t_fr, False, white, black, teal, 'Menu')




## --------------------------------------------------------------- GAME LOOP

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True  
        if exitState and event.type == pygame.MOUSEBUTTONDOWN:
            if hover(cursor_pos, button_bR.size, button_bR.pos):
                ct_collected = 0
                exitState=False
                menuState=True
                mode1=False
                mode2=False   #Reseting everything when menu is clicked
                sequence=True
                button_tR.color['text'] = button_tR.color['acc']
                button_tL.color['text'] = button_tL.color['acc']
                hasClick = False
                button_tR.active = False
                button_tL.active = False
                chaser_list = [] 
                enemy_list = []
                coll_list=[]
                box_laser_list = []
                enemy_list = []                
                col=[255,0,255]
                tick_interval = 1.0
                txtbox_d.text = ''
            elif hover(cursor_pos, button_bL.size, button_bL.pos):
                exitState=False  #if exit, then leaves the loop
                gameExit = True
        if menuState and event.type == pygame.MOUSEBUTTONDOWN: 
            if hover(cursor_pos, button_tL.size, button_tL.pos):
                mode1=True  #Mode 1: Runaway mode
                mode2=False   
                button_tL.active = True
                button_tR.active = False
                hasClick = True
                button_tL.color['text'] = button_tL.color['sel']
                button_tR.color['text'] = button_tR.color['acc']
            if hover(cursor_pos, button_tR.size, button_tR.pos):
                mode1=False
                mode2=True  #Mode 2: Collector's Mode  
                button_tR.active = True
                button_tL.active = False
                hasClick = True
                button_tL.color['text'] = button_tL.color['acc']
                button_tR.color['text'] = button_tR.color['sel']
            if hover(cursor_pos, button_c.size, button_c.pos):
                if mode1 or mode2:
                    hasClick=True
                    menuState=False
                    gameState=True
                else:
                    hasClick=False #if no mode, then passes boolean to menustate if statement                
                          
            
    if menuState: ## --------------------------------------------- menuState --
        gameDisplay.fill((0,255,255)) #blue background
        if mode1:
            button_tL.fr['act'] = True
            button_tR.fr['act'] = False
            button_tL.render()
        if mode2:
            button_tL.fr['act'] = False
            button_tR.fr['act'] = True
            button_tR.render()
            
              
        ## buttons_display  
        button_c.render()
        button_tL.render()
        button_tR.render()
        txtbox_cred.render()
        
        cursor_pos=pygame.mouse.get_pos()        
        
        ## check_if_user_has_clicked
        if ((hasClick == False) and hover(cursor_pos,button_c.size, button_c.pos)): #This part sends a message to user that they need to pick
            txtbox_g.text = 'Please select a game mode (1 or 2)'
            txtbox_g.txtstyle = body2            
            txtbox_g.render()
 
        elif((hasClick == True) and hover(cursor_pos,button_c.size, button_c.pos)):
            txtbox_g.text = 'START GAME'
            txtbox_g.txtstyle = body2            
            txtbox_g.render()            
        
        if hover(cursor_pos, button_tL.size, button_tL.pos): #mouseover instructions
            txtbox_g.text = 'Play Runaway mode: Dodge enemies for as long as you can!'
            txtbox_g.txtstyle = body3
            txtbox_g.render()

        
        if hover(cursor_pos, button_tR.size, button_tR.pos): #mouseover instructions
            txtbox_g.text = 'Play Collector\'s mode: Dodge enemies and collect pulsing boxes!'
            txtbox_g.txtstyle = body3            
            txtbox_g.render()            
                     
        
    if gameState: ## --------------------------------------------  gameState --
        ## ----------------------------------------------- mode1 --------------
        if mode1:
            tick_time += timer.get_frame_duration()
            if tick_time > tick_interval:
                tick_time = 0
                enemy = Enemy()
                enemy_list.append(enemy)  
                if len(enemy_list) / 5 == 1:
                    chaser = Chaser_Enemy()
                    chaser_list.append(chaser)
                if len(enemy_list) % 10 == 0:
                    possible_pos = [(380,280),(100,100),(100,460),(660,100),(660,460)]
                    for i in range(len(enemy_list)//10):
                        box_laser = Box_Laser()
                        box_laser_list.append(box_laser)
            
                    
            ## DISPLAYING EVERYTHING
            gameDisplay.fill(white)   #white clears what was behind it
    
            ## Char location
            char.set_Location(pygame.mouse.get_pos())
            char.render()
            
            ## Box lasers
            for box_laser in box_laser_list:
                if box_laser.growing:
                    box_laser.spawn()
                elif not box_laser.gone:
                    box_laser.charge()
                ## if box_laser is charging and char.is_touching box or lasers  
                if box_laser.charging and (     char.is_Touching(box_laser.pos,40,40) or \
                    char.is_Touching((box_laser.pos[0]-20,box_laser.pos[1]+10),20,20) or \
                    char.is_Touching((box_laser.pos[0]+10,box_laser.pos[1]-20),20,20) or \
                    char.is_Touching((box_laser.pos[0]+40,box_laser.pos[1]+10),20,20) or \
                    char.is_Touching((box_laser.pos[0]+10,box_laser.pos[1]+40),20,20)    ): 
                    ## gamestate to exitstate
                    gameState=False
                    exitState=True
                    txtbox_d.text = 'Score: '+ str(len(enemy_list))
                    ## circle around frozen gameplay
                    circle_freeze()
                    break
                
                ## if box_laser is grown and on screen and char.is_touching box or lasers
                if box_laser.lasers and (not box_laser.gone) and (\
                    char.is_Touching((0,box_laser.pos[1]+10),20,1000) or \
                    char.is_Touching((box_laser.pos[0]+10,0),1000,20) \
                    ):
                    ## gamestate to exitstate
                    gameState=False
                    exitState=True
                    txtbox_d.text = 'Score: '+ str(len(enemy_list))
                    ## circle around frozen gameplay
                    circle_freeze()
                    break  
        
            ## Chasers
            for chaser in chaser_list:
                ## if character is touching chaser and enemy isn't growing, game over
                if char.is_Touching(chaser.pos,chaser.size[0],chaser.size[1]) and not chaser.growing:
                    ## gamestate to exitstate
                    gameState=False
                    exitState=True
                    txtbox_d.text = 'Score: '+ str(len(enemy_list))
                    ## circle around frozen gameplay
                    circle_freeze()
                    break
                ## if chaser is growing, no game over if char.is_touching chaser
                if chaser.growing:
                    chaser.spawn()        
                else:
                    chaser.chase(char)            
            
            ## Enemies
            for enemy in enemy_list:
                ## if character is touching enemy and enemy isn't growing, game over
                if char.is_Touching(enemy.pos,enemy.size[1],enemy.size[0]) and not enemy.growing:
                    ## gamestate to exitstate
                    gameState=False
                    exitState=True
                    txtbox_d.text = 'Score: '+ str(len(enemy_list))
                    ## circle around frozen gameplay
                    circle_freeze()
                    break
                ## if enemy is growing, no game over if char.is_touching enemy
                if enemy.growing:
                    enemy.spawn()
                else:
                    enemy.move()
        
        ## ----------------------------------------------- mode2 --------------
        if mode2:
            tick_interval = 0.5
            tick_time += timer.get_frame_duration()
            
            round_ct +=1 ## counts cycles since last red color change
            ## changes red color for pulsing col
            if round_ct>red_interval:
                round_ct = 0
                red_ind += 1
                if red_ind >= len(reds):
                    red_ind = 0  
                    
            ## spawns ENEMIES
            if tick_time > tick_interval:
                tick_time = 0
                enemy = Enemy()
                enemy_list.append(enemy)
                
                rd +=1 ## rounds since last coll spawn    
            
            ## spawns COL 
            if rd > every_rd:
                coll = Coll()
                coll_list.append(coll)
                rd = 0            

            ## DISPLAYING EVERYTHING
            gameDisplay.fill(white)   #white clears what was behind it
            
            ## Coll emphasis (behind everything else)
            for coll in coll_list:
                if not coll.growing:
                    coll.emphasis(red_ind)            
    
            ## Char location
            char.set_Location(pygame.mouse.get_pos())
            char.render()
            
            ## Coll
            for coll in coll_list:
                ## setting color for uniform flicker
                coll.color = (reds[red_ind],0,0)
                ## if char.is_touching coll, collect item, even if growing
                if char.is_Touching(coll.pos,20,20):
                    coll.deactivate()
                    ct_collected +=1
                    coll_list.pop(coll_list.index(coll))
                ## if not char.is_touching coll, coll is growing continue growing
                elif coll.growing:
                    coll.spawn()
                else:
                    coll.render(red_ind)            
             
            ## Enemies
            for enemy in enemy_list:
                ## if character is touching enemy and enemy isn't growing, game over
                if char.is_Touching(enemy.pos,enemy.size[1],enemy.size[0]) and not enemy.growing:
                    ## gamestate to exitstate
                    gameState=False
                    exitState=True
                    txtbox_d.text = 'Collectables: '+ str(ct_collected)
                    ## circle around frozen gameplay
                    circle_freeze()
                    break
                ## if enemy is growing, no game over if char.is_touching enemy
                if enemy.growing:
                    enemy.spawn()
                else:
                    enemy.move()
            

    if exitState: ## --------------------------------------------- exitState --
        cursor_pos=pygame.mouse.get_pos()
        if col[0]>0 and sequence: ##column is list of [255,255,255] outside while loops for color manipulation
            gameDisplay.fill((col[0],col[0],col[0])) 
            col[0]-=1
        if col[0]==0: ## delaying for fade effect
            sequence = False
            pygame.time.delay(500)
        if not sequence and col[0]<=255: ##fading in game over text
            txtbox_c.color = (col[0], col[0], col[0])
            txtbox_c.render()
            txtbox_d.color = (col[0], col[0], col[0])
            txtbox_d.render() 
            col[0]+=1
        elif not sequence and col[1]<=255: ## exit and menu buttons fade in
            button_bL.color['fill'] = (col[1],col[1],col[1])
            button_bR.color['fill'] = (col[1],col[1],col[1])
            button_bL.render()
            button_bR.render()
            col[1]+=1    
        
    ##artificial delay
    pygame.time.delay(delay_duration)
    
    pygame.display.update()
    timer.tick()
#only updates specific area mentioned, but if no parameters its like flip,update is more versatile
#pygame.display.update()

#unitializing everything
pygame.quit()