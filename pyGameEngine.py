import pyglet
import math
#Keyboard Constants
K_UP = pyglet.window.key.UP
K_DOWN = pyglet.window.key.DOWN
K_RIGHT = pyglet.window.key.RIGHT
K_LEFT = pyglet.window.key.LEFT

#Constants
UP=0
DOWN = 1
LEFT = 2
RIGHT = 3

#Boundary Action Constants
WRAP = 0
DIEOFFSCREEN = 1
UNBOUNDED = 2


#The user can create a sprite
class Sprite(pyglet.sprite.Sprite):

    def __init__(self,image,x,y):
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        pyglet.sprite.Sprite.__init__(self,image)
        
        self.x = x
        self.y = y
        self.oldScale = 999
        self.oldRotation = 999
        self.length = image.width
        self.wide = image.height
        self.hide = False
        self.boundaryAction = WRAP
        self.keyHold = [False,False,False,False]


    def hiding(self):
        self.hide = True

    def showing(self):
        self.hide = False

    def visible(self):
        return not self.hide

    #scale the sprite
    def scaling(self, scale):
        if not scale == self.oldScale:
            self.image.width = scale * self.width
            self.image.height = scale * self.height

    #rotate the sprite
    def rotate(self, degree):

        if not degree == self.oldRotation:
            self.rotation = -degree
            rad = -degree * (math.pi/180)
            self.length= math.fabs((self.image.width * math.cos(rad))) + math.fabs((self.image.height * math.sin(rad)))
            self.wide = math.fabs((self.image.width * math.sin(rad))) + math.fabs((self.image.height * math.cos(rad)))
            self.oldRotation = degree


    #translate the sprite
    def translate(self, offx, offy):
        self.x = self.x + offx
        self.y = self.y + offy
        
        
    #set the boundary action
    def setBoundaryAction(self,action):
        self.boundaryAction = action

    #Define the actions that user choose for the boundary
    def boundaryActions(self):
        if self.boundaryAction == WRAP:
            if self.x < 0:
                self.x = 640
            if self.x > 640:
                self.x = 0
            if self.y < 0:
                self.y = 480
            if self.y > 480:
                self.y = 0
        elif self.boundaryAction == DIEOFFSCREEN:
            if self.x < 0 or self.x > 640 or self.y < 0 or self.y > 480:
                self.hide()
        else:
            pass
            
            

    #let the user add implementation to the update function
    def update(self):
        pass

    #let the user add movement to the sprite
    def moveSprite(self):
        pass

    
    #checked to see what keys the user pressed
    def keyPressed(self,keys):
        if keys == K_UP:
            self.keyHold[UP] = True

        if keys == K_DOWN:
            self.keyHold[DOWN] = True

        if keys == K_LEFT:
            self.keyHold[LEFT] = True

        if keys == K_RIGHT:
            self.keyHold[RIGHT] = True
        

    #checked to see what keys the user released
    def keyReleased(self,keys):

        if keys == K_UP:
            self.keyHold[UP] = False

        if keys == K_DOWN:
            self.keyHold[DOWN] = False

        if keys == K_LEFT:
            self.keyHold[LEFT] = False

        if keys == K_RIGHT:
            self.keyHold[RIGHT] = False

    #checks to see if there is collision with the sprite
    def collidesWith(self,otherSprite):

        self.collision = False
        
        if not self.hide:

            if not otherSprite.hide:
                #Assume there is collision
                self.collision = True

                #get the borders of the current sprite
                self.left = self.x - (self.length // 2)
                self.right = self.x + (self.length // 2)
                self.top = self.y + (self.wide // 2)
                self.bottom = self.y - (self.wide // 2)

                #get the borders of the other sprite
                otherSprite.left = otherSprite.x - (otherSprite.length // 2)
                otherSprite.right = otherSprite.x + (otherSprite.length // 2)
                otherSprite.top = otherSprite.y + (otherSprite.wide // 2)
                otherSprite.bottom = otherSprite.y - (otherSprite.wide // 2)

                #There is no collision happening to the sprite
                if (self.bottom > otherSprite.top) or (self.top < otherSprite.bottom) or (self.right < otherSprite.left) or (self.left > otherSprite.right):
                    self.collision = False
                

        return self.collision
        
        
        
#the user can create a display
class Display(pyglet.window.Window):

    def __init__(self):
       pyglet.window.Window.__init__(self)
       self.label = []
       self.sprites = []

    #add the label to the window
    def addLabel(self,label):
        self.label.append(label)

    #add the sprite to the window
    def addSprite(self,sprite):
        self.sprites.append(sprite)
        
    #start the game
    def start(self):
        pyglet.clock.schedule_interval(self.update,1/30.0)
        pyglet.clock.set_fps_limit(30)
        pyglet.app.run()
        

    #this is called to update the screen
    def update(self,*args, **kwargs):
        self.on_draw()

    #user press key on keyboard
    def on_key_press(self, key, modifiers):
        for sprite in self.sprites:
            sprite.keyPressed(key)

    #user let go of key on keyboard
    def on_key_release(self, key, modifiers):
        for sprite in self.sprites:
            sprite.keyReleased(key)
        
    #This is used to draw things on the window  
    def on_draw(self):
        self.clear()
   
        for labels in self.label:
            labels.update()
            labels.label.draw()

        for sprite in self.sprites:
            if not sprite.hide:
                sprite.update()
                sprite.draw()
                sprite.boundaryActions()

                
            
        
class Label(object):
    
    def __init__(self, text = "", name = "Arial", size = 12, labelCoordinateX = 10,labelCoordinateY = 450):
         self.label = pyglet.text.Label(text, font_name = name, font_size = size,x = labelCoordinateX, y =labelCoordinateY)

    def setText(self, texts):
        self.label.text = texts

    def setFont(self, name):
        self.label.font_name = name

    def setSize(self, size):
        self.label.font_size = size

    def setPosition(self,x,y):
        self.label.x = x
        self.label.y = y
        
    #let the user to decide what to do with the label
    def update(self):
        pass
