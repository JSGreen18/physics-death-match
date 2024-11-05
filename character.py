import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, image, name,turn):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.name = name

        # which turn they move on
        self.turn = turn

        # initial position of player is top left corner
        self.rect.x = 0
        self.rect.y = 0

    def update(self, turn,height):
        #print(pygame.mouse.get_pressed()[0],turn, self.turn)
        # set initial postion of sprite
        if pygame.mouse.get_pressed()[0] == True and turn == self.turn:
            
            # get x and y position of mouse 
            self.rect.y = pygame.mouse.get_pos()[1]
            self.rect.x = pygame.mouse.get_pos()[0]



        elif pygame.mouse.get_pressed()[0] == False and self.turn == turn:
            
            # checks if players feet is on the floor
            if self.rect.y >= height - (100+113) and self.rect.y >= height - (100+113) - 4 :
                pass
            
            else:
                # adds 4 to y coordinate of rect to move character down
                self.rect.y += 4


        
            


        


