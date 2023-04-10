import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()

        #initialize 
        self.image = pygame.transform.scale(pygame.image.load("assets/bowser.png").convert_alpha(),(200,200))      
        self.rect = self.image.get_rect(midbottom = (700,530))

        #state
        self.direction = False
        self.speed = 7
        self.life = 5

        self.life_cd = 30
        self.cd_status = False

    def movement(self):
        if self.direction == False:
            self.rect.x -= self.speed    
        else:
            self.rect.x += self.speed 

    def update_direction(self):
        if self.rect.left <= 0:
            self.direction = True
        
        if self.rect.right >= 1000:
            self.direction = False

    def decrease_life(self):
        if self.life >= 1 and self.life_cd == 30:
            self.life -= 1
            self.cd_status = True
    
    def update_cd(self):
        if self.cd_status == True:
            if self.life_cd > 0:
                self.life_cd -= 1
            else:
                self.life_cd = 30
                self.cd_status = False
    
    def update(self):
        self.update_direction()
        self.movement()
        self.update_cd()


    