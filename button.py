import pygame

class Button(pygame.sprite.Sprite):

    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)

        # load image for sprite
        self.image = pygame.image.load(image)

        # create rectangle for button
        self.rect = self.image.get_rect()

        # set position of button
        self.rect.x = x
        self.rect.y = y

    def draw(self,surf):
        surf.blit(self.image,(self.rect.x,self.rect.y))
    
    def clicked(self,event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            #check if click happens on button
            if self.rect.topleft[0] < pygame.mouse.get_pos()[0] < self.rect.bottomright[0] and self.rect.topleft[1] < pygame.mouse.get_pos()[1] < self.rect.bottomright[1]:
                return True
            else: 
                return False
