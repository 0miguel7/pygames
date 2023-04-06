import pygame

class Sky(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #Initialize Sky and place it
        self.image = pygame.Surface((1000,500))
        self.image.fill((113, 71, 179))
        self.rect = self.image.get_rect(topleft = (0,0))

class Floor(pygame.sprite.Sprite):
    def __init__(self, ):
        super().__init__()

        #Initialize floor and place it 
        self.image = pygame.image.load("ground.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (0,500))

class Player(pygame.sprite.Sprite):
    def __init__(self, ):
        super().__init__()

        #Initialize player and place it
        self.player_left = pygame.transform.scale(pygame.image.load("boby.png").convert_alpha(),(120,140))
        self.player_right = pygame.transform.scale(pygame.image.load("boby.png").convert_alpha(),(120,140))
        
        self.image = self.player_right
        self.rect = self.image.get_rect(topleft = (0,400))
        self.y_speed = 0

        self.dashing = False
        self.dash_speed = 10
        self.dash_counter = 15
        self.dash_cooldown = 30
        self.start_cooldown = False
      

    def player_input(self,keys):
        
        if keys[pygame.K_UP] and self.rect.bottom == 500  :
            self.y_speed = -17
          
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.dash_speed = -10
            if keys[pygame.K_z] and not self.dashing and self.dash_cooldown == 30:  
                self.start_dash()
                self.start_cooldown = True
            else:
                self.image = self.player_left
                self.rect.x -= 5

        if keys[pygame.K_RIGHT] and self.rect.right < 1000:
            self.dash_speed = 10
            if keys[pygame.K_z] and not self.dashing and self.dash_cooldown == 30:  
                self.start_dash()
                self.start_cooldown = True
            else:
                self.image = self.player_right
                self.rect.x += 5


    def apply_gravity(self):
        if self.rect.bottom < 500:
            self.y_speed += 1
        self.rect.y += self.y_speed

        if self.rect.bottom >= 500: self.rect.bottom = 500


    def move(self):
        self.rect.x += 4
        if self.rect.x > 1000: self.rect.x = -100

    def apply_dash(self):      
        if self.dashing:
                if self.dash_counter > 0:
                    
                    self.dash_counter -= 1
                    self.rect.x += self.dash_speed
                else:
                    self.dash_counter = 15
                    self.dashing = False
        
                      
        
    def start_dash(self):
        self.dashing = True          
        

    def update_cooldown(self):
        if self.start_cooldown:
            if self.dash_cooldown > 0:
                self.dash_cooldown -= 1
            else:
                self.dash_cooldown = 30
                self.start_cooldown = False


    def update(self):   
        keys = pygame.key.get_pressed()
        self.player_input(keys)
        self.apply_gravity()  
        self.update_cooldown()  
        self.apply_dash()
      
            
            

    