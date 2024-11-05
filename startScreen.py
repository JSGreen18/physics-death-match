import pygame
import button


pygame.init()

WIDTH = 1000
HEIGHT =  600


WHITE = (255,255,255)


# get background images
bg = pygame.image.load('startBackground.png')
 
                    
# set up sprite group and button sprite
startSprites = pygame.sprite.Group()

# create start button and add it to sprite group
startButton = button.Button(WIDTH/2 - 50,HEIGHT/2,'startButton.png')
startSprites.add(startButton)


# function to run the intro screen
def gameStart(surface):
    
    running = True
    while running == True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # update sprites
            start = startButton.clicked(event)
            if start == True:
                running = False
        

        # draw / render
        surface.fill(WHITE)
        surface.blit(bg, (0,0))
        
        #draw title image onto screen
        title = pygame.image.load('title.png')
        title_rect = title.get_rect()
        title_rect.x = 200
        title_rect.y = 150
        surface.blit(title, (title_rect.x,title_rect.y)) 
        
        # draw all sprites need on start screen
        startSprites.draw(surface)


        #AFTER drawing everything, flip display
        pygame.display.flip()












