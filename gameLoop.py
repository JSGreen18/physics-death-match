import pygame
import startScreen
import Round
import character

pygame.init()

WIDTH = 1000
HEIGHT =  600
FPS = 60

#set up clock for fps
clock = pygame.time.Clock()

#set window size
surface = pygame.display.set_mode((WIDTH,HEIGHT))  

#set title
pygame.display.set_caption('Physics Death Match')

#initialize colour

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)


#set background colour 
surface.fill(WHITE)
pygame.display.flip()


# run start screen
startScreen.gameStart(surface)

# create player sprite group
playerSprites = pygame.sprite.Group()

# create players and add them to sprite group
player1 = character.Character('player1.png','player1',0)
playerSprites.add(player1)

player2 = character.Character('player2.png','player2',1)
playerSprites.add(player2)
 



# run start screen
startScreen.gameStart(surface)
# run test
testRound = Round.Rounds('asteriodBG.png',player1,player2,playerSprites)
testRound.roundLoop(surface)