import pygame

class Sky(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        self.image = pygame.transform.scale(pygame.image.load("assets/fondo.png").convert_alpha(),(1000,500))
        self.rect = self.image.get_rect(topleft = (0,0))

class Floor(pygame.sprite.Sprite):
    def __init__(self, ):
        super().__init__()

        #Initialize floor and place it 
        self.image = pygame.image.load("assets/ground1.png").convert_alpha()
        self.rect = self.image.get_rect(bottomleft = (0,600))

