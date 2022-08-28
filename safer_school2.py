# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 21:09:39 2021

@author: apeng
"""


import os

import pygame
from pygame import mixer
import pygame_widgets
from pygame_widgets.button import Button

pygame.font.init()

# define colors
WHITE = (255,255,255)
GREEN = (0,192,0)
LIGHTGREEN = (105,193,126)
YELLOWGREEN = (178,210,102)
BLUE = (0,50,200)
DARKBLUE = [0,0,150]

BLACK = (0,0,0)
GREY = (128,128,128)
SILVER = (192,192,192)
PURPLE = (75,0,130)

RED = [200, 50, 0]
DARKRED = [150, 0, 0]



FPS = 60 # frame per second

# define window properties 
WIDTH, HEIGHT = 800, 800 # screen size
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SaferSchools")
BIN_FONT = pygame.font.SysFont('arial.ttf', 40)
BIN_FONT_BIG = pygame.font.SysFont('arial.ttf', 60)

global background
global earthquake_icon, fire_icon, bully_icon, internet_icon, gunshooting_icon
global earthquake_icon_x, earthquake_icon_y
global fire_icon_x, fire_icon_y
global bully_icon_x, bully_icon_y
global internet_icon_x, internet_icon_y
global gunshooting_icon_x, gunshooting_icon_y

# def set_main_state():
#     ''' set game state to be main so the we can return to the main window '''
#     global game_state
#     game_state = "main"
 
    
# def set_new_question():
#     ''' set new question state '''
#     global new_question
#     new_question = True

def load_sprite(folder_name, image_name, xsize, ysize):
    ''' Load and resize a sprite '''
    
    sprite = pygame.image.load(os.path.join(folder_name, image_name))
    sprite = pygame.transform.scale(sprite, (xsize ,ysize))
    return sprite

def soundEffect(choice):
    ''' make sound '''
    
    if choice:
        mixer.init()
        correct = os.path.join('Assets', 'correct.mp3')
        mixer.music.load(correct)
        mixer.music.set_volume(0.7)
        mixer.music.play()
    else:
        mixer.init()
        wrong = os.path.join('Assets','wrong.mp3')
        mixer.music.load(wrong)
        mixer.music.set_volume(0.7)
        mixer.music.play()

def draw_control_buttons():
    ''' draw control buttons, including ->, <-, and return '''
    
    WIN.blit(prev_question, (prev_question_x, prev_question_y))
    WIN.blit(next_question, (next_question_x, next_question_y))
    WIN.blit(return_to_main, (return_x, return_y))

def draw_answer_buttons(answer1, answer2, answer3, answer4, question_id):
    ''' 
    Draw answer buttons. The texts of the four buttons are specified by 
    answer1, answer2, answer3, answer4
    '''
    
    # create answer buttons
    button_width = 250
    button_height = 80
    button_ori_x = 125
    button_ori_y = 550
    button_step_x = 300
    button_step_y = 100
    
    button_fontsize = 45
    button_margin = 20
    button_radious = 20
    
    button_ans1 = Button(
        # Mandatory Parameters
        WIN,  # Surface to place button on
        button_ori_x,  # X-coordinate of top left corner
        button_ori_y,  # Y-coordinate of top left corner
        button_width,# width
        button_height,  # Height
    
        # Optional Parameters
        text=answer1,  # Text to display
        textColour=WHITE,
        fontSize=button_fontsize,  # Size of font
        margin=button_margin,  # Minimum distance between text/image and edge of button
        inactiveColour=BLUE,  # Colour of button when not being interacted with
        hoverColour=DARKBLUE,  # Colour of button when being hovered over
        pressedColour=GREEN,  # Colour of button when being clicked
        radius=button_radious,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: action(question_id, 1)  # Function to call when clicked on
    )

    button_ans2 = Button(
        # Mandatory Parameters
        WIN,  # Surface to place button on
        button_ori_x + button_step_x,  # X-coordinate of top left corner
        button_ori_y,  # Y-coordinate of top left corner
        button_width,# width
        button_height,  # Height
    
        # Optional Parameters
        text=answer2,  # Text to display
        textColour=WHITE,        
        fontSize=button_fontsize,  # Size of font
        margin=button_margin,  # Minimum distance between text/image and edge of button
        inactiveColour=BLUE,  # Colour of button when not being interacted with
        hoverColour=DARKBLUE,  # Colour of button when being hovered over
        pressedColour=GREEN,  # Colour of button when being clicked
        radius=button_radious,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: action(question_id, 2)  # Function to call when clicked on
    )
    
    button__ans3 = Button(
        # Mandatory Parameters
        WIN,  # Surface to place button on
        button_ori_x,  # X-coordinate of top left corner
        button_ori_y + button_step_y,  # Y-coordinate of top left corner
        button_width,# width
        button_height,  # Height
    
        # Optional Parameters        
        text=answer3,  # Text to display
        textColour=WHITE,        
        fontSize=button_fontsize,  # Size of font
        margin=button_margin,  # Minimum distance between text/image and edge of button
        inactiveColour=BLUE,  # Colour of button when not being interacted with
        hoverColour=DARKBLUE,  # Colour of button when being hovered over
        pressedColour=GREEN,  # Colour of button when being clicked
        radius=button_radious,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: action(question_id, 3)  # Function to call when clicked on
    )

    button__ans4 = Button(
        # Mandatory Parameters
        WIN,  # Surface to place button on
        button_ori_x + button_step_x,  # X-coordinate of top left corner
        button_ori_y + button_step_y,  # Y-coordinate of top left corner
        button_width,# width
        button_height,  # Height
    
        # Optional Parameters
        text=answer4,  # Text to display
        textColour=WHITE,        
        fontSize=button_fontsize,  # Size of font
        margin=button_margin,  # Minimum distance between text/image and edge of button
        inactiveColour=BLUE,  # Colour of button when not being interacted with
        hoverColour=DARKBLUE,  # Colour of button when being hovered over
        pressedColour=GREEN,  # Colour of button when being clicked
        radius=button_radious,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: action(question_id, 4)  # Function to call when clicked on
    )   
    
        
def load_main_window_sprites():
    '''load main window sprites '''
    
    global background
    global earthquake_icon, fire_icon, bully_icon, internet_icon, gunshooting_icon    
    global earthquake_icon_x, earthquake_icon_y
    global fire_icon_x, fire_icon_y
    global bully_icon_x, bully_icon_y
    global internet_icon_x, internet_icon_y
    global gunshooting_icon_x, gunshooting_icon_y
 
    background = load_sprite('Assets','school_background.jpg', WIDTH, int(HEIGHT*0.6))   
    earthquake_icon = load_sprite('Assets','earthquake_icon2.jpg', 110,140)
    fire_icon = load_sprite('Assets','fire.png', 110, 140)
    bully_icon = load_sprite('Assets','bully.png', 110, 140)
    internet_icon = load_sprite('Assets','internet2.jpg', 110,140)
    #gunshooting_icon = load_sprite('Assets','gun_shooting.png', 110,140)
    
    
    earthquake_icon_x = 110
    earthquake_icon_y = 600   
    fire_icon_x = 250
    fire_icon_y = 600
    bully_icon_x = 400
    bully_icon_y = 600     
    internet_icon_x = 550
    internet_icon_y = 600
   # gunshooting_icon_x = 620
   # gunshooting_icon_y = 600    
    
    
def draw_main_window():
    ''' Draw the main window '''

    # draw the background
    WIN.fill(YELLOWGREEN)
    WIN.blit(background, (0,0))

    # define earthquake, fire, bully, internet, gun shooting icons (surface object)
    
    #draw option icons
    WIN.blit(earthquake_icon, (earthquake_icon_x, earthquake_icon_y))
    WIN.blit(fire_icon, (fire_icon_x, fire_icon_y))
    WIN.blit(bully_icon, (bully_icon_x, bully_icon_y))
    WIN.blit(internet_icon, (internet_icon_x, internet_icon_y))
    # WIN.blit(gunshooting_icon, (gunshooting_icon_x, gunshooting_icon_y))

    pygame.display.update()
    
    
def load_control_button_sprites():
    ''' load control button sprites, including ->, <-, and return '''
    
    global prev_question, next_question, return_to_main
    global prev_question_x, prev_question_y
    global next_question_x, next_question_y
    global return_x, return_y
    
    prev_question = load_sprite('Assets','prev_question.png', 50, 50)  
    next_question = load_sprite('Assets', 'next_question.png', 50, 50)
    return_to_main = load_sprite('Assets', 'return_to_main.png', 120, 60)
    
    prev_question_x = 630    
    prev_question_y = 20    
    next_question_x = 700
    next_question_y = 20
    return_x = 50
    return_y = 20


    
def load_bully_window_sprites():
    '''load main window sprites '''
    
    global bully_background
    global bully_assessment_icon, bully_antibullying101_icon   
    global bully_assessment_icon_x, bully_assessment_icon_y
    global bully_antibullying101_icon_x, bully_antibullying101_icon_y
    
    bully_background = load_sprite('Assets','bully_background.jpeg', WIDTH, int(HEIGHT*0.7))   
    bully_assessment_icon = load_sprite('Assets','assessment4.png', 130,130)
    bully_antibullying101_icon = load_sprite('Assets','antibullying101_2.png', 130,130)
    
    
    bully_assessment_icon_x = 200
    bully_assessment_icon_y = 600   
    bully_antibullying101_icon_x = 500
    bully_antibullying101_icon_y = 600
    
    
def draw_bully_window():
    ''' Draw the bully window '''    


    # draw the background
    WIN.fill(WHITE)
    WIN.blit(bully_background, (0,0))
    
    #draw option icons
    WIN.blit(bully_assessment_icon, (bully_assessment_icon_x, bully_assessment_icon_y))
    WIN.blit(bully_antibullying101_icon, (bully_antibullying101_icon_x, bully_antibullying101_icon_y))
    
    question_text = BIN_FONT.render('Assessment', 1, BLACK)
    WIN.blit(question_text, (bully_assessment_icon_x-20, bully_assessment_icon_y+120))
    
    question_text = BIN_FONT.render('Anti-bullying 101', 1, BLACK)
    WIN.blit(question_text, (bully_antibullying101_icon_x-50, bully_assessment_icon_y+120))
    
    # draw return icon
    WIN.blit(return_to_main, (return_x, return_y))    

    pygame.display.update()
    
    
def load_bully_assessment_sprites():
    '''load main window sprites '''
    
    global bully_assessment_background, bully_assessment_happened, bully_assessment_nothappened
    global bully_assessment_happened_x, bully_assessment_happened_y
    global bully_assessment_nothappened_x, bully_assessment_nothappened_y
    
    bully_assessment_background = load_sprite('Assets','bully_assessment_background.png', WIDTH, HEIGHT)   
    bully_assessment_happened = load_sprite('Assets','bully_assessment_sad.png', 130,130)
    bully_assessment_nothappened = load_sprite('Assets','bully_assessment_happy.png', 130,130)
    
    
    bully_assessment_happened_x = 200
    bully_assessment_happened_y = 200   
    bully_assessment_nothappened_x = 500
    bully_assessment_nothappened_y = 200
    
    
def draw_bully_assessment_window(x, y, bully_item, bully_item_label):
    ''' Draw the bully window '''    


    # draw the background
    WIN.fill(GREEN)
    WIN.blit(bully_assessment_background, (0,0))
    
    #draw option icons
    WIN.blit(bully_assessment_happened, (bully_assessment_happened_x, bully_assessment_happened_y))
    WIN.blit(bully_assessment_nothappened, (bully_assessment_nothappened_x, bully_assessment_nothappened_y))
    
    option_text = BIN_FONT.render('Happened', 1, BLACK)
    WIN.blit(option_text, (bully_assessment_happened_x-20, bully_assessment_happened_x-35))
    
    option_text = BIN_FONT.render('Did not happen', 1, BLACK)
    WIN.blit(option_text, (bully_assessment_nothappened_x-50, bully_assessment_nothappened_y-35))
    
    # draw return icon
    WIN.blit(return_to_main, (return_x, return_y))    
    
    # draw bully item
    WIN.blit(bully_item, (x, y))

    # question
    question_text = BIN_FONT.render('Did this happen to you? Drag and drop. ', 1, WHITE)
    WIN.blit(question_text, (150, 550))
    
    #label bully item
    sprite_text = BIN_FONT.render(bully_item_label, 1, PURPLE)
    WIN.blit(sprite_text, (200,650))

    pygame.display.update()

def draw_bully_assessment_result(happened, nothappened):
    ''' Draw the bully window '''    


    # draw the background
    WIN.fill(LIGHTGREEN)
#    WIN.blit(bully_assessment_background, (0,0))
    
    #draw option icons
    WIN.blit(bully_assessment_happened, (200, 200))
    WIN.blit(bully_assessment_nothappened, (500, 200))
    
    option_text = BIN_FONT.render('Happened', 1, BLACK)
    WIN.blit(option_text, (bully_assessment_happened_x-20, bully_assessment_happened_x-35))
    
    option_text = BIN_FONT.render('Did not happen', 1, BLACK)
    WIN.blit(option_text, (bully_assessment_nothappened_x-50, bully_assessment_nothappened_y-35))
    
    # draw return icon
    WIN.blit(return_to_main, (return_x, return_y))    
    
    # display times happened and not happened
    result_text = BIN_FONT_BIG.render(str(happened), 1, RED)
    WIN.blit(result_text, (250, 350))
    
    result_text = BIN_FONT_BIG.render(str(nothappened), 1, RED)
    WIN.blit(result_text, (550, 355))
    

    # Conclusion
    result_text = BIN_FONT.render('Your risk of getting bullied: ', 1, BLACK)
    WIN.blit(result_text, (150, 550))
    
    risk = int(float(happened)/float(happened + nothappened)*100)
    
    result_text = BIN_FONT_BIG.render(str(risk) + '%', 1, RED)
    WIN.blit(result_text, (560, 545))
    pygame.display.update()

    run = True
    
    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()                
                
            elif event.type == pygame.MOUSEBUTTONDOWN: # pick up the trash
                if event.button == 1:
                    mx, my = event.pos
                    
                    if return_to_main.get_rect().collidepoint(mx-return_x, my-return_y):
                        game_state = 'bully' 
                        run = False
                        break
    
    pygame.display.update()
    
        
    
def action_bully_question(evaluation, image, color, x, y):
        
    # draw earthquake background   
    bully_background = load_sprite('Assets', image, WIDTH, int(HEIGHT/2))      
    WIN.fill(SILVER)    
    WIN.blit(bully_background, (0, 0))
   
    question_text = BIN_FONT.render(evaluation, 1, color)
    WIN.blit(question_text, (x, y))
    
    draw_control_buttons() # draw < (previous) and > (next) buttons
    
    
def action(question_id, answer_id):
    if game_state == 'bully_antibully101':
        if question_id == 1:
            image = 'bully.gif'
            if answer_id == 1:
                
                action_bully_question('Right. Seek for help.', image, GREEN, 250, 450)
                soundEffect(True)

            elif answer_id == 2:

                action_bully_question('Bullying is not right!', image, RED, 250, 450)
                soundEffect(False)
                                
            elif answer_id == 3:

                action_bully_question('You will get bullied more.', image, RED, 200, 450)
                soundEffect(False)                
                
            elif answer_id== 4:

                action_bully_question('Escaping will not solve the problem!', image, RED, 100, 450)
                soundEffect(False)                       
                
        elif question_id == 2:
            image = 'bully_question2.jpg'
            if answer_id == 1:
                
                action_bully_question('Physical examples: hitting, kicking, pushing...', image, RED, 50, 450)
                soundEffect(False)                

            elif answer_id == 2:
                action_bully_question('Verbal examples: insults, teasing, intimidation...', image, RED, 30, 450)
                soundEffect(False)                
                
            elif answer_id == 3:
                action_bully_question('Social examples: lying, spreading rumours...', image, GREEN, 50, 450 )
                soundEffect(True)                

            elif answer_id== 4:
                action_bully_question('Cyber examples: hurtful emails or posts.', image, RED, 100, 450)
                soundEffect(False)                
            
        elif question_id == 3:
            image = 'bully_question3.png'
            if answer_id == 1:
                action_bully_question('Correct. Low self esteem is one of the main issues in being bullied', image, GREEN, 30, 450)
                soundEffect(True)                

            elif answer_id == 2:
                action_bully_question('Incorrect. Being happier is not one of the main issues in being bullied', image, RED, 20, 450)
                soundEffect(False)                
                
            elif answer_id == 3:
                action_bully_question('Correct. Depression is one of the main issues in being bullied', image, GREEN, 30, 450 )
                soundEffect(True)                

            elif answer_id== 4:
                action_bully_question('Correct. Being more violent is one of the main issues in being bullied', image, GREEN, 30, 450)
                soundEffect(True)                
                

def first_bully_question():
    ''' Display the first question on bully '''
    
    global new_question
    new_question = False # it will change to True when > button is clicked
    
    # draw earthquake background   
    bully_background = load_sprite('Assets', 'bully.gif', WIDTH, int(HEIGHT/2))      
    WIN.fill(SILVER)    
    WIN.blit(bully_background, (0, 0))
   
    question_text = BIN_FONT.render('What will you do?', 1, BLACK)
    WIN.blit(question_text, (100, 450))
    
    question_id = 1
    draw_answer_buttons('Tell someone', 'Bully back', 'Ignore', 'Change school', question_id)
    draw_control_buttons() # draw < (previous) and > (next) buttons


def second_bully_question():
    ''' Display the second question on bully '''
    
    global new_question
    new_question = False # it will change to True when > button is clicked
    
    # draw earthquake background   
    bully_background = load_sprite('Assets', 'bully_question2.jpg', WIDTH, int(HEIGHT/2))      
    WIN.fill(SILVER)    
    WIN.blit(bully_background, (0, 0))
   
    question_text = BIN_FONT.render('Do you recognize this type of bullying? ', 1, BLACK)
    WIN.blit(question_text, (100, 450))

    question_id = 2
    draw_answer_buttons('Physical', 'Verbal', 'Emotional', 'Cyber', question_id )
    draw_control_buttons() # draw < (previous) and > (next) buttons
    
    
def third_bully_question():
    #Display the second question on bully 
    
    #global new_question
    #new_question = False # it will change to True when > button is clicked
    
    # draw earthquake background   
    bully_background = load_sprite('Assets', 'bully_question3.png', WIDTH, int(HEIGHT/2))      
    WIN.fill(SILVER)    
    WIN.blit(bully_background, (0, 0))
   
    question_text = BIN_FONT.render('Concequenses of getting bullied:  ', 1, BLACK)
    WIN.blit(question_text, (100, 450))

    question_id = 3
    draw_answer_buttons('Low Self Esteem', 'Being Happier', 'Depression', 'More Violent', question_id )
    draw_control_buttons() # draw < (previous) and > (next) buttons



def bully_questions(question_id):
    ''' choose bully quesitons '''
    if question_id == 1:
        first_bully_question()
    elif question_id == 2:
        second_bully_question()
    elif question_id == 3:
        third_bully_question()


   
def bully():
    global game_state
    game_state = "bully"
    
    load_bully_window_sprites() # may not be here, only need to call once
    
    draw_bully_window()


    run = True
    
    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()                
                
            elif event.type == pygame.MOUSEBUTTONDOWN: # pick up the trash
                if event.button == 1:
                    mx, my = event.pos
                    
                    if bully_assessment_icon.get_rect().collidepoint(mx-bully_assessment_icon_x, my-bully_assessment_icon_y):
                        bully_assessment()
                        draw_bully_window()
                        
                    elif bully_antibullying101_icon.get_rect().collidepoint(mx-bully_antibullying101_icon_x, my-bully_antibullying101_icon_y):
                        bully_antibullying101()                       
                        draw_bully_window()
                        
                    elif return_to_main.get_rect().collidepoint(mx-return_x, my-return_y):
                        game_state = 'main' 
                        run = False
                        break

    return
 


def isInBins(bully_sprite, bin_sprite, xdrop, ydrop, x_bin, y_bin):
    ''' check if the trash item has been moved into a bin '''

    # get the bounding box of the trash sprite
    xs_bully, ys_bully, xe_bully, ye_bully = bully_sprite.get_rect() 

    # get the bounding box of the bin sprite    
    xs_bin, ys_bin, xe_bin, ye_bin = bin_sprite.get_rect()

    # check if bully is inside bin along x direction
    xIsIn = (xdrop > x_bin and xdrop < x_bin + xe_bin) or (xdrop + xe_bully > x_bin and xdrop + xe_bully < x_bin + xe_bin)
    
    # check if bully is inside bin along y direction
    yIsIn = (ydrop > y_bin and ydrop < y_bin + ye_bin) or (ydrop + ye_bully > y_bin and ydrop + ye_bully < y_bin + ye_bin)
    if xIsIn and yIsIn:
        return True
    else:
        return False


        
def bully_assessment():
    
    global game_state
    game_state = "bully_assessment"
    
    load_bully_assessment_sprites()    
    
    run = True

    dragging = False
    x = 350
    y = 600
    xdrop_ori = x
    ydrop_ori = y
    xdrop = x
    ydrop = y

    maxcnt = 3
    happened = 0
    nothappened = 0

    bully_item_label_list = ['hitting', 'grabbing', 'teasing']
    bully_item_list = ['bully_assessment_hitting.png', 'bully_assessment_grabbing.png', 'bully_assessment_teasing.png']
    
    cnt = 0
    bully_item = load_sprite('Assets', bully_item_list[0], 120, 120)  
    draw_bully_assessment_window(x, y, bully_item, bully_item_label_list[0])    

    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN: # pick up the trash
                if event.button == 1:
                    mx, my = event.pos
                    
                    if return_to_main.get_rect().collidepoint(mx-return_x, my-return_y):
                        game_state = 'bully' 
                        run = False
                        break
                     
                    xstart, ystart, xend, yend = bully_item.get_rect()
                    
                    if mx < xdrop + xend and mx > xdrop and my < ydrop + yend and my > ydrop: # successfully picked the bully item

                        dragging = True
                        mx, my = event.pos
                        x, y = xdrop, ydrop
                        off_x = x - mx
                        off_y = y - my
                        
            elif event.type == pygame.MOUSEBUTTONUP: # release the bully item
                if event.button == 1:
                    dragging = False
                    xdrop = x
                    ydrop = y

                    # check if bully item is in any one the bins                   
                        
                    isInHappened = isInBins(bully_item, bully_assessment_happened, xdrop, ydrop, bully_assessment_happened_x, bully_assessment_happened_y)
                    isInNotHappened = isInBins(bully_item, bully_assessment_nothappened, xdrop, ydrop, bully_assessment_nothappened_x, bully_assessment_nothappened_y)


                    if isInHappened:
                        happened += 1
                        soundEffect(False)
                        
                    elif isInNotHappened:
                        nothappened += 1
                        soundEffect(True)


                    if isInHappened or isInNotHappened:
                        cnt += 1
                        if cnt < maxcnt:
                            print(cnt, maxcnt)
                            x = xdrop_ori # put the bully item to the same postion to start
                            y = ydrop_ori
                            
                            bully_item = load_sprite('Assets', bully_item_list[cnt], 120, 120)
                            draw_bully_assessment_window(x, y, bully_item, bully_item_label_list[cnt])  
                            
                        else:
                           draw_bully_assessment_result(happened, nothappened)  
                           game_state = 'bully'
                           run = False
                           break

            elif event.type == pygame.MOUSEMOTION: # move the bully item
                if dragging:
                    mx, my = event.pos
                    x = mx + off_x
                    y = my + off_y
                    draw_bully_assessment_window(x, y, bully_item, bully_item_label_list[cnt])    
                    
                                       
    
        
def bully_antibullying101():
    ''' Bully module '''
        
    global game_state
    game_state = "bully_antibully101"
    
    question_number = 4 # total number of questions
    question_id = 1 # 'first question'
    
    bully_questions(question_id)
    run = True     
 
    while run: 

        events = pygame.event.get()       
        for event in events:            
            if event.type == pygame.QUIT:
                run = False            
                pygame.quit() 

            elif event.type == pygame.MOUSEBUTTONDOWN: 
                
                if event.button == 1:
                    mx, my = event.pos
                    
                    if prev_question.get_rect().collidepoint(mx-prev_question_x, my-prev_question_y): # press the <- button
                        if question_id > 1:
                            question_id -= 1 # previous question 
                            
                            bully_questions(question_id)
                    elif next_question.get_rect().collidepoint(mx-next_question_x, my-next_question_y): # press the -> button
                        if question_id < question_number: # not the last question
                            question_id += 1 # next question
                            bully_questions(question_id)
                    elif return_to_main.get_rect().collidepoint(mx-return_x, my-return_y):
                        game_state = 'bully' 
                        run = False
                        break
        
        pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
        pygame.display.update()

                        
    return


def earthquake():
    ''' earthquake module '''
    
    global game_state
    game_state = "earthquake"
        
    # draw earthquake background    
    earthquake_background = load_sprite('Assets', 'earthquake_background2.jpg', WIDTH, HEIGHT)
    WIN.fill(SILVER)       
    WIN.blit(earthquake_background, (0, 0))    
    
    # draw control buttons < and >
    draw_control_buttons()

    run = True        
    while run:
        events = pygame.event.get()       
        for event in events:
            # need to click a return button
            
            if event.type == pygame.QUIT:
                run = False            
                pygame.quit() 
            elif event.type == pygame.MOUSEBUTTONDOWN: # pick up the trash
                if event.button == 1:
                    mx, my = event.pos
                    if return_to_main.get_rect().collidepoint(mx-return_x, my-return_y):
                        game_state = 'main'
                        run = False
                        break
        pygame.display.update()
    
    return
            
    # earthquake test

def fire():
    global game_state
    game_state = "fire"

    # draw earthquake background        
    fire_background = load_sprite('Assets', 'fire_background.jpg', WIDTH, HEIGHT)   
    WIN.fill(SILVER)      
    WIN.blit(fire_background, (0, 0))

    # draw control buttons < and >    
    draw_control_buttons()
    
    run = True        
    while run:
        events = pygame.event.get()       

        for event in events:
            # need to click a return button
            
            if event.type == pygame.QUIT:
                run = False            
                pygame.quit() 
            elif event.type == pygame.MOUSEBUTTONDOWN: # pick up the trash
                if event.button == 1:
                    mx, my = event.pos
                    if return_to_main.get_rect().collidepoint(mx-return_x, my-return_y):
                        game_state = 'main' 
                        run = False
                        break

        pygame.display.update()
    
    return

def internet():
    # draw internet window
    # internet test
    pass

# def gun_shooting():
#     # draw gun_shooting window
#     # gun shooting test
#     pass


def main():
    ''' main function of the game '''
    
    load_main_window_sprites()
    load_control_button_sprites()
    
#    set_main_state()
    global game_state
    game_state = "main"
 
    
    clock = pygame.time.Clock()

    run = True
    
    draw_main_window()
    
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN: # pick up the trash
                if event.button == 1:
                    mx, my = event.pos
                    
                    if earthquake_icon.get_rect().collidepoint(mx-earthquake_icon_x, my-earthquake_icon_y):
                        earthquake()
                        draw_main_window()
                        
                    elif fire_icon.get_rect().collidepoint(mx-fire_icon_x, my-fire_icon_y):
                        fire()                       
                        draw_main_window()
                        
                    elif bully_icon.get_rect().collidepoint(mx-bully_icon_x, my-bully_icon_y):
                        bully()
                        draw_main_window()

                        
                    # elif gunshooting_icon.get_rect().collidepoint(mx-gunshooting_icon_x, my-gunshooting_icon_y):
                    #     gun_shooting()
                    #     draw_main_window()
                        
                    elif internet_icon.get_rect().collidepoint(mx-internet_icon_x, my-internet_icon_y):
                        internet()
                        draw_main_window()
                    

    pygame.quit()
    
    
if __name__ == "__main__":
    main()
    


