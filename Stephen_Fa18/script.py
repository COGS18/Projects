#!/usr/bin/env python
# coding: utf-8

# # Final Project: Sprite Animation

# ## Objective: 
# Using the module pygame, the objective of this project is to animate an RPG character's movement across a background. 
# 
# 
# A window is created as a display, with the background image uploaded to the display. The window's dimensions are created to fit the dimensions of the background image.
# 
# The window is constantly redrawn (updated) to delete old frames and create new ones.
# 
# The program draws in our player, and listens for key inputs (up, down, left, right) and responds by changing directional booleans to True or False, and moving our player in that direction. The booleans listen for key inputs, as they are later used to animate our player.
# 
# This is accomplished by loading in 8 images for each direction (left, right,up and down) into a list and loading through the images throughout the duration of each boolean.
# 
# The player can not walk off of the screen, as conditionals for movement create artificial borders by taking the size of the player, their steplength, and the size of the window into account.
# 
# The FPS is set as 32, a multiple of 8 in order to match the number of images that loop. Each image should be displayed for 4 frames.
# 
# ## Controls:
# 
# Control your player by using the up, down, left and right arrows!
# 
# Thank you for a great quarter.

# In[16]:


import pygame
from my_module import functions as fn


# In[17]:


pygame.init()                                               # Initializes pygame
pygame.display.set_caption("Sprite Run")                    # This sets the title of our window to "Sprite Run"

image_dir = 'images/rpg_character/'               # The pathway for our character image, so that it is convenient
                                                            # to load in our character images.

bg = pygame.image.load('images/background.png')   # Uses a method which loads an image from our directory, and sets
                                                            # the image equal to a variable, in this case bg.

image_size = bg.get_rect()                                  # This gets the size of our image (bg) and provides the rectangular
w_center = image_size.center[1]                             # dimensions of our image. Center gives us the middle of the image.
h_center = image_size.center[0]    
dw = image_size[2]                                          # We use the image dimensions to fit our screen to. (width)                                  
dh = image_size[3]                                          # We use the image dimensions to fit our screen to. (height)

dw_half = dw/2                                              # Half of the size of the screen
dh_half = dh/2 
win  = pygame.display.set_mode((dw,dh))                     # Creates a window (pop-up) with the dimensions dw,dh (x,y).
clock = pygame.time.Clock()                                 # Defines clock in order to set a framerate later.


char = pygame.image.load(image_dir+'tile000.png')           # Loads the image for our character when he is not moving.



# Below, we use the pygame.image.load method to load in a sequence of images from our directory.
# Each direction is walkright, walkleft, walkup and walkdown hold a list of 8 images, which are saved in the order of
# each animation and looped through later for us to animate our sprite's movement.

#################################################################################################

walkright = [pygame.image.load(image_dir+'tile024.png'),pygame.image.load(image_dir+'tile025.png'),  
             pygame.image.load(image_dir+'tile026.png'),pygame.image.load(image_dir+'tile027.png'),  
             pygame.image.load(image_dir+'tile028.png'),pygame.image.load(image_dir+'tile029.png'), 
             pygame.image.load(image_dir+'tile030.png'),pygame.image.load(image_dir+'tile031.png')] 

walkleft =[pygame.image.load(image_dir+ 'tile016.png'),pygame.image.load(image_dir+'tile017.png'),  
           pygame.image.load(image_dir+'tile018.png'),pygame.image.load(image_dir+'tile019.png'),    
           pygame.image.load(image_dir+'tile020.png'),pygame.image.load(image_dir+'tile021.png'),
           pygame.image.load(image_dir+'tile022.png'),pygame.image.load(image_dir+'tile023.png')] 

walkup = [pygame.image.load(image_dir+'tile008.png'),pygame.image.load(image_dir+'tile009.png'),
          pygame.image.load(image_dir+'tile010.png'),pygame.image.load(image_dir+'tile011.png'),
          pygame.image.load(image_dir+'tile012.png'),pygame.image.load(image_dir+'tile013.png'),
          pygame.image.load(image_dir+'tile014.png'),pygame.image.load(image_dir+'tile015.png')] 

walkdown = [pygame.image.load(image_dir+'tile000.png'),pygame.image.load(image_dir+'tile001.png'),
            pygame.image.load(image_dir+'tile002.png'),pygame.image.load(image_dir+'tile003.png'),
            pygame.image.load(image_dir+'tile004.png'),pygame.image.load(image_dir+'tile005.png'),
            pygame.image.load(image_dir+'tile006.png'),pygame.image.load(image_dir+'tile007.png')]         
        
#################################################################################################
        
man = fn.Player(dw_half,dh_half,20,30, 2.75)      # Initialize our character, named 'man', at the center of the screen 
                                                # (dw_half, dh_half), with a size of width=20 and height=30 and velocity (vel)  
                                                # at 2.5. The size of our character is necessary to detect collisions with the  
                                                # border of our game-window.
        
run = True                                      # Boolean to run our main-game loop.
while run:                                      # While run is true, run the main game loop repetitively.
    
    
    keys = pygame.key.get_pressed()             # A pygame function that listens for keypresses (live inputs from the user).
                                                # Keys is defined as a tuple filled with 0's. When a key press is initiated, a
                                                # new tuple is made with a value of 1 at the corresponding entry, to show that
                                                # a key press has been made.
    
    clock.tick(32)                              # The framerate of our program, the number of frames or iterations of our code 
                                                # that are run each second.
    

    
    for event in pygame.event.get():            # This gets events from the queue, commanded by the user. 
        if event.type == pygame.QUIT:           # If the user clicks exit (the red X at the top-right of a window)
            run = False                         # run is set to False. This will end our game loop.
    
    
    man.move(keys, dw, dh)                      # Calls to our move function, inputting our keys tuple and screen dimensions.
    
    man.draw(win, char, walkright,              # Calls to our animation function, inputting our window and lists of character
             walkleft, walkup, walkdown)        # images to sequence.
        
    fn.redraw_game_window(win, bg, dw_half,     # Calls our function for updating the game window, inputting the window,
                         w_center, h_center, dh_half)   # background image, image_size, and halved screen dimensions for use.
    
pygame.quit()                                   # Once the game loop is done, exit the window.


# In[ ]:





# In[ ]:




