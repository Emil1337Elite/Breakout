import pygame

#Define colors of blocks
mint = (0,255,205)
pink = (242,0,210)
brown = (192,135,49)
white = (255,255,255)

#Sets the size of the blocks
block_width = 23
block_height = 15

#This class represents the blocks in the game
class Block(pygame.sprite.Sprite):

#Takes in color and the x and y position
    def __init__(self,color,x,y):
        super().__init__()
        self.image = pygame.Surface([block_width,block_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#Ball class
class Ball(pygame.sprite.Sprite):
    #Properties of the ball
    speed = 8.0
    x = 0.0
    y = 180.0
    direction = 160
    width = 10
    height = 10

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([self.width, self.height])
        #Colors in the ball
        self.image.fill(pink)
        self.rect = self.image.get_rect()
        #Gets the width and height of the screen
        self.screenh = pygame.display.get_surface().get_height()
        self.screenw = pygame.display.get_surface().get_width()

pygame.init()

#Sets size of the game window
screen = pygame.display.set_mode([800, 600])

#Sets name of the game window
pygame.display.set_caption('Breakout!')

#Creates background
bg = pygame.Surface(screen.get_size())

#Sprite lists
balls = pygame.sprite.Group()
blocks = pygame.sprite.Group()
sprites = pygame.sprite.Group()

#Creates the ball sprite
ball = Ball()
sprites.add(ball)
balls.add(ball)

top = 80
blocknumber = 32

#Creates the block rows
for row in range(5):
    #Creates block columns
    for column in range(0,blocknumber):
        #Creates the blocks
        block = Block(brown, column * (block_width + 2) + 1, top)
        blocks.add(block)
        sprites.add(block)
    top += block_height + 2

#Temporary quit
running = True
while running:
    #Color of the background
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    sprites.draw(screen)
    pygame.display.flip()
#Ends the program
pygame.quit()