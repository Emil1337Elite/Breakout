import pygame
from random import randint

#Defines colors to be used
orange = (255,128,0)
white = (255,255,255)
black = (0,0,0)
blue = (0,0,204)

score = 0
life = 1

#Sets the size of the blocks
block_width = 23
block_height = 15

class Block(pygame.sprite.Sprite):

#Constructor, takes in color and the x and y position
    def __init__(self,color,x,y):
        """The constructor block class

        Args:
            color (tuple): The color of the blocks
            x (int): Position on x-axis
            y (int): Position on y-axis
        """
        super().__init__()
        self.image = pygame.Surface([block_width,block_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#Ball class
class Ball(pygame.sprite.Sprite):

    def __init__(self,color,width,height):
        """The constructor ball class

        Args:
            color (tuple): The color of the ball
            width (int): The width of the ball
            height (int): The height of the ball
        """
        super().__init__()
        self.image = pygame.Surface([width, height])
        #Colors in the ball
        self.image.fill(white)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(4,8),randint(1,8)]
        self.rect = self.image.get_rect()
    

    def move(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        """This function makes the ball bounce the other way when a collision is detected
        """
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = - self.velocity[1] + randint(-4,4)

class Platform(pygame.sprite.Sprite):

    def __init__(self):
        """The constructor platform class
        """
        super().__init__()
        self.height = 15
        self.width = 100  
        self.image = pygame.Surface([self.width, self.height])
        self.speed = 10
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.screenh = pygame.display.get_surface().get_height()
        self.screenw = pygame.display.get_surface().get_width()
        self.rect.x = 0
        #Sets platform spawn point
        self.rect.y = self.screenh-self.height

    def movement(self):
        """This function makes the platform follow the mouse
        """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > self.screenw - self.width:
            self.rect.x = self.screenw - self.width

pygame.init()

#Sets size of the game window
screen = pygame.display.set_mode([800, 600])

#Sets name of the game window
pygame.display.set_caption('Breakout!')

#Hides the mouse pointer
pygame.mouse.set_visible(0)

#Creates background
bg = pygame.Surface(screen.get_size())

#Sprite lists
all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()

#Creates platform
platform = Platform()
all_sprites.add(platform)

#Creates the ball sprite
ball = Ball(white,10,10)
ball.rect.x = 345
ball.rect.y = 195
all_sprites.add(ball)

top = 80
blocknumber = 32

"""Creates the blocks as well as placing them in columns and rows
"""
for row in range(5):
    for column in range(0,blocknumber):
        block = Block(orange, column * (block_width + 2) + 1, top)
        blocks.add(block)
        all_sprites.add(block)
    top += block_height + 2

#Loop will keep going until stopped by user
run = True

#Used to control the fps
fps = pygame.time.Clock()

#Reads highscore from file
with open("highscore.txt", "r") as f:
    highscore = int(f.readline().strip())

#Main loop
while run:

    #Color of the background
    screen.fill(blue)

    all_sprites.update()

    platform.movement()
    
    ball.move()
    
    """Detects collision between the ball and the walls and ends the game 
    if the ball hits the bottom wall.
    """
    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
        life -= 1
        if life == 0:
            font = pygame.font.Font(None, 80)
            text = font.render("Game Over!", 1, white)
            screen.blit(text, (245,300))
            pygame.display.flip()
            pygame.time.wait(3500)

            run = False

    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]
    
#Detect collisions between the ball and the platform
    if pygame.sprite.collide_mask(ball, platform):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()

#Removes block if collision with ball is detected
    kill_block = pygame.sprite.spritecollide(ball, blocks, True)

    """Bounces if block is hit and not all are gone. 
    Ends game and shows win screen if all blocks are removed.
    """
    if len(kill_block) > 0:
        ball.bounce()
        score += 1
        if len(blocks) == 0:
            font = pygame.font.Font(None, 80)
            text = font.render("You win!", 1, white)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3500)

            run = False

        """If the score achieved is larger than the current highscore it 
        is written to a file and saved
        """
    for event in pygame.event.get():
        if score >= highscore:
            with open("highscore.txt", "w") as f:
                f.write(str(score))
                
        if event.type == pygame.QUIT:    

            run = False
    
        """Colors the background and draws the line at the top of the screen
        """
    screen.fill(blue)
    pygame.draw.line(screen, white, [0, 38], [800, 38], 2)

#Displays the score and high score
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, white)
    screen.blit(text, (20,10))
    text = font.render("High Score: " + str(highscore), 1, white)
    screen.blit(text, (500, 10))

    """Draws all sprites on screen and displays them
    """
    all_sprites.draw(screen)    
    pygame.display.flip()

#Sets the games fps
    fps.tick(40)

#Ends the program
pygame.quit()