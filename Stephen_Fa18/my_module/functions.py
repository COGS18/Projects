import pygame

def redraw_game_window(win,bg, w_center, h_center, dw_half, dh_half):
    """Updates the game window several times each second by using the blit method from pygame. 
    ***Without this function, our character would remain printed everywhere they walk, leaving tracers across the screen.***
    
    Parameters
    ----------
    win : pygame.Surface
        Our game window
    
    bg : pygame.Surface
        Our background image
    
    w_center : int or float
        The center x co-ordinate of our image according to width.
        
    h_center : int or float
        The center y co-ordinate of our image according to height.
        
    dw_half : int or float
        Half the width of our window
        
    dh_half : int or float
        Half the height of our window
 
        
    Returns
    -------
    This function does not return any values. Instead, it uses the method blit to update our game window for 
    animation and any changes that occur.
    """
 
    win.blit(bg, (dw_half - w_center, dh_half - h_center))   # Utilizes the blit method to update the background,
                                                             # image centered and updated with following the  
                                                             # format of (image, (x,y)).

    
    


class Player():
    
    def __init__(self, x, y, width, height, vel = 2, walkcount = 0, left = False, right = False, up = False, down = False):
        """Initializes our character.
    
            Parameters
            ----------
            x : int or float
                The x co-ordinate to spawn the character at. 
                
            y : int or float
                The y co-ordinate to spawn the character at.
                
            width : int or float
                Width of the character's hitbox/collision.
                
            height : int or float
                Height of the character's hitbox/collision.
                
            vel : int or float
                Velocity, or length of each step the character takes.
                
            walkcount : int or float
                Counts the steps of the character in order to animate accordingly.
      
            left : boolean
                Checks if the character is moving left. Default is False
                
            right : boolean
                Checks if the character is moving right. Default is False

            up : boolean
                Checks if the character is moving up. Default is False
                
            down : boolean
                Checks if the character is moving left. Default is False
                
             
            Returns
            -------
            The character has been initialized and we can now manipulate its object.
            """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.walkcount = walkcount
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        
   
    def draw(self, win, char,walkright,walkleft,walkup,walkdown):
        """Animates our character.
    
        Parameters
        ----------
        win : pygame.Surface
            Our game window
            
        char : pygame.Surface
            Image of our character standing still
            
        walkright : list
            A list of 8 images loaded for animating the character as they walk right.
            
        walkleft :list
            A list of 8 images loaded for animating the character as they walk left.
            
        walkup : list
            A list of 8 images loaded for animating the character as they walk up.
            
        walkdown : list
            A list of 8 images loaded for animating the character as they walk down.
            

        Returns
        -------
        This function does not return any values. Instead, it uses the method blit to update the screen with the animations of our character's movement.
        """

        
        if self.walkcount +1 >= 14:   # If walkcount exceeds 14, reset it to 0. We use walkcount//2 to loop through images.
             self.walkcount =0
                
        if self.right:                                               # If our character is moving right, loop across the list of images.
            win.blit(walkright[self.walkcount//2], (self.x,self.y))  # After selecting an image, print it at the character's current x and 
            self.walkcount+=1                                        # y co-ordinate. Increment walkcount, and blit and image again while
                                                                     # right is true.
            
        elif self.left:                                              # Follows the same procedure, but for the left boolean.
            win.blit(walkleft[self.walkcount//2], (self.x,self.y))
            self.walkcount +=1
            
        elif self.up and not self.right and not self.left:           # Follows the same procedure, but for the up boolean. However, this
            win.blit(walkup[self.walkcount//2], (self.x,self.y))     # restricts character animation to its direction. This may seem
            self.walkcount+=1                                        # like overkill, because we have an if, elif, else conditional, but
                                                                     # bugs arise without this as players often input more than one key at
                                                                     # a time. This adjusts to that bug.
            
        elif self.down and not self.right and not self.left:         # Follows the same procedure as up, but for the down boolean.
            win.blit(walkdown[self.walkcount//2], (self.x,self.y))
            self.walkcount+=1
            
        else:                                                        # If up down left and right are False, then blit our character
            win.blit(char, (self.x,self.y))                          # standing still.

        pygame.display.update()
    
    def move(self, keys, dw, dh):
        """Moves our character along the x and y axis.

        Parameters
        ----------
        keys : tuple
            A tuple of our key inputs. A new tuple called 'keys' is made several times a second. 
        dw : int or float
            The width of the screen
        dh : int or float
            The height of the screen

        Returns
        -------
        This function does not return any values. Instead it updates the x and y position of our object Player (our character).
        """
        if  keys[pygame.K_RIGHT] and self.x < dw-self.width-self.vel:                 # If you press/hold the right arrow and your x
            self.x += self.vel                                                        # co-ordinate is less than the boundary of the screen
            self.left = False                                                         # minus the size and stepdistance of your player,
            self.right = True                                                         # set the condition of right as True, and increment
            self.up = False                                                           # the x co-ordinate based on their vel (stepsize).
            self.down = False

        elif keys[pygame.K_LEFT] and self.x > self.vel:                               # Same procedures as above, but the x direction
            self.x -= self.vel                                                        # is subtracted and the x must be greater than 
            self.left = True                                                          # the vel (stepsize) to move. This is because at
            self.right = False                                                        # the left boundary of the screen x == 0.
            self.up = False
            self.down = False
            
        elif keys[pygame.K_UP] and self.y > self.vel:                                 # Same procedures as above, but in the y direction.
            self.y -= self.vel
            self.up = True
            self.down = False
            self.left = False
            self.right = False

        elif keys[pygame.K_DOWN] and self.y  < dh - self.height - self.vel*2:         # Perfecting the bottom boundary was difficult, and
            self.y += self.vel                                                        # it required the height of the screen minus the
            self.down = True                                                          # the character height and double the stepsize.
            self.up = False
            self.left = False
            self.right = False

        else:                                                                         # If none of these keys are pressed, the character
            self.up = False                                                           # will not move, the walkcount is reset to 0, and
            self.down = False                                                         # all booleans are set to False.
            self.left = False
            self.right = False
            self.walkcount = 0
        