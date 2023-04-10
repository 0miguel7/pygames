import pygame

class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #244 200
        self.image = pygame.transform.scale(pygame.image.load("assets/bowser.png").convert_alpha(),(300,200)) 
        self.rect = self.image.get_rect(midbottom = (500,550))
