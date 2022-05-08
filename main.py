import pygame
from random import randint

#Define colors of blocks
mint = (0,255,205)
pink = (242,0,210)
brown = (192,135,49)
white = (255,255,255)
black = (0,0,0)

#Sets the size of the blocks
block_width = 23
block_height = 15

#This class represents the blocks in the game
class Block(pygame.sprite.Sprite):

#Constructor, takes in color and the x and y position
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
    # speed = 8.0
    # x = 0.0
    # y = 180.0
    # direction = 160
    # width = 10
    # height = 10

    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        #Colors in the ball
        self.image.fill(pink)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(4,8),randint(-8,8)]
        self.rect = self.image.get_rect()
    
    def move(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

#Class of the player platform   
class Platform(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        #Properties of platform
        self.height = 15
        self.width = 70  
        self.image = pygame.Surface([self.width, self.height])
        self.speed = 10
        #Color of platform
        self.image.fill(black)
        #Sets position where ball comes from
        self.rect = self.image.get_rect()
        self.screenh = pygame.display.get_surface().get_height()
        self.screenw = pygame.display.get_surface().get_width()
        self.rect.x = 0
        self.rect.y = self.screenh-self.height

    def movement(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > self.screenw - self.width:
            self.rect.x = self.screenw - self.width

pygame.init()

#Sets size of the game window
screen = pygame.display.set_mode([800, 600])

#Sets name of the game window
pygame.display.set_caption('Breakout!')

#Creates background
bg = pygame.Surface(screen.get_size())

#Sprite list
all_sprites = pygame.sprite.Group()

#Creates platform
platform = Platform()
all_sprites.add(platform)

#Creates the ball sprite
ball = Ball(pink,10,10)
ball.rect.x = 345
ball.rect.y = 195
all_sprites.add(ball)

top = 80
blocknumber = 32

#Creates the block rows
for row in range(5):
    #Creates block columns
    for column in range(0,blocknumber):
        #Creates the blocks
        block = Block(brown, column * (block_width + 2) + 1, top)
        all_sprites.add(block)
    top += block_height + 2

#Loop will keep going until stopped by user
run = True

#Used to control the fps
fps = pygame.time.Clock()

#Main loop
while run:
    #Color of the background
    screen.fill(mint)

    all_sprites.update()

    platform.movement()
    ball.move()

    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]
    
#Detect collisions between the ball and the platform
    if pygame.sprite.collide_mask(ball, platform):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    all_sprites.draw(screen)
    
    pygame.display.flip()

    fps.tick(60)
#Ends the program
pygame.quit()