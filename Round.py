import pygame
import random
import button
import sys



# funtion to draw text on the screen
font_name = pygame.font.match_font('arial')
def draw_text(surf,text,size,x,y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)


# class to create sprites
class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y):
        super().__init__()
        
        # get image for sprite
        self.image = pygame.image.load(image)
        
        # get rectangle for image
        self.rect = self.image.get_rect()
        
        # set coords for rect
        self.rect.x = x
        self.rect.y = y

    def draw(self,surf,x,y):
        surf.blit(self.image,(x,y))




#create parent class for the rounds
class Rounds():
    def __init__(self,bg, player1, player2,playerSprites):
        
        # set random player to go first
        self.turn = random.randint(0,1)

        # set background image
        self.bg = pygame.image.load(bg)

        # create sprite group for the sprites of the round
        self.roundSprites = pygame.sprite.Group()

        # draw submit button on bottom corner of screen
        self.submit = button.Button(850,530,'submit.png')
        self.roundSprites.add(self.submit)

        # set player and player group
        self.player1 = player1
        self.player2 = player2
        self.playerSprites = playerSprites


        # create a ruler for each player 
        self.ruler1 = Sprite('ruler.png',self.player1.rect.centerx - 12, 560)
        self.ruler2 = Sprite('ruler.png',self.player2.rect.centerx - 8,560)

        

    # method to draw all sprites to screen
    def drawSprites(self,surface):
         self.roundSprites.draw(surface)
         

    # method to calculate players score
    def getPlayerScore(self, playerPos, correctPoint):
            return 1000 - abs(correctPoint - playerPos)
    
    # method for the loop of the game
    def roundLoop(self,surface):
        WHITE = (255,255,255)

        running = True
        while running == True:
            for event in pygame.event.get():

                # end program if window is closed
                if event.type == pygame.QUIT:
                    sys.exit()

                # check if submitted 
                submitted = self.submit.clicked(event)
                if submitted == True:
                    # if submit button is pressed, go to other players turn
                    self.turn = (self.turn + 1) % 2
 
            # draw background
            surface.fill((255,255,255))
            surface.blit(self.bg,(0,0))


            if self.turn == 0:
                # draw ruler for player 1 
                self.ruler1.draw(surface,self.player1.rect.centerx - 12, 560)
                # draw text to show distance of ruler
                draw_text(surface,str(self.player1.rect.centerx),15,self.player1.rect.centerx-12,545)

            elif self.turn == 1:
                #draw ruler for player 2
                self.ruler2.draw(surface,self.player2.rect.centerx - 8,560)
                # draw text to show distance of ruler
                draw_text(surface,str(self.player2.rect.centerx),15,self.player2.rect.centerx-8,545)

            # update all layer spries and redraw them 
            self.playerSprites.update(self.turn,600)
            self.playerSprites.draw(surface)

            # draw all other sprites
            self.drawSprites(surface)

            # AFTER drawing everything, flip display
            pygame.display.flip()

        

            


            
        
class asteriodRound(Rounds):

    def __init__(self,surf):
        super().__init__()

        # create asteriod sprite
        asteriod = Sprite('asteriod.png', 0,0)
        
        # add asteriod sprite to sprite group
        self.roundSprites.add(asteriod)


         
         