import pyGameEngine
from pyGameEngine import*
from random import randrange



class Net(pyGameEngine.Sprite):

    def __init__(self,image,x,y):
        pyGameEngine.Sprite.__init__(self,image, x,y)

    def moveSprite(self):  
        if self.keyHold[LEFT]:
            self.x -= 5

        if self.keyHold[RIGHT]:
            self.x += 5
            
    def update(self):
        self.moveSprite()
        
  
        
class Squirrel(pyGameEngine.Sprite):

    def __init__(self,image,x,y):
        pyGameEngine.Sprite.__init__(self,image,x,y)
        self.degree = 0

    
    def moveSprite(self):
        self.y -= 3
        
    def RandomX(self):
        return randrange(640)
    
    def update(self):
        self.moveSprite()
        self.rotate(self.degree)
        collisions()
        self.degree+=5

        if not self.visible():
            self.y = 480
            self.x = self.RandomX()
            squirrel.showing()
            
class Label(pyGameEngine.Label):

    def __init__(self):
        pyGameEngine.Label.__init__(self)
        

    def update(self):
        self.setText("Catch All The Squirrels!!")
        
def collisions():
    if net.collidesWith(squirrel):
        squirrel.hiding()
        



if  __name__ == "__main__":
    screen = pyGameEngine.Display()
    label = Label()
    

    image = pyglet.image.load('net.png')
    image2 = pyglet.image.load('squirrel.png')
    net = Net(image,300,10)
    squirrel = Squirrel(image2,400, 400)

    
    screen.addSprite(net)
    screen.addSprite(squirrel)
    screen.addLabel(label)
    screen.start()

  



