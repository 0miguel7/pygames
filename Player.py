import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, ):
        super().__init__()

        #sounds
        self.jump_sound = pygame.mixer.Sound("assets/jump.mp3")
        self.jump_sound.set_volume(0.4)
        self.hit_sound = pygame.mixer.Sound("assets/hit.mp3")
        self.hit_sound.set_volume(0.1)

        #dino normal
        self.player_left = pygame.transform.scale(pygame.image.load("assets/dino2_left.png").convert_alpha(),(77,100))
        self.player_right = pygame.transform.scale(pygame.image.load("assets/dino2_right.png").convert_alpha(),(77,100))

        #dino atacking
        self.sword_left = pygame.transform.scale(pygame.image.load("assets/dino_sword_left.png").convert_alpha(),(156,100))
        self.sword_right = pygame.transform.scale(pygame.image.load("assets/dino_sword_right.png").convert_alpha(),(156,100))


        self.image = self.player_right
        self.rect = self.image.get_rect(topleft = (0,400))
        self.y_speed = 0


        #Dashing variables
        self.dashing = False
        self.dash_speed = 10
        self.dash_counter = 15
        self.dash_cooldown = 30
        self.start_cooldown = False

        #Attacking variables
        self.attack_status = False
        self.attack_duration = 20
        self.orientation = "R" 
        self.attack_cooldown = 40
        self.start_attack_cooldown = False

      

    def player_input(self,keys):
        
        #UP
        if keys[pygame.K_c] and self.rect.bottom == 500  :
            self.y_speed = -22
            self.jump_sound.play()
        
        #LEFT
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.orientation = "L"
            self.dash_speed = -10
            if keys[pygame.K_z] and not self.dashing and self.dash_cooldown == 30:  
                self.start_dash()
                self.start_cooldown = True
            else:
                #Normal movement
                sprite_x,sprite_y = self.rect.topright
                if not self.attack_status:    
                    self.image = self.player_left
                    self.rect = self.image.get_rect(topright = (sprite_x,sprite_y))
                self.rect.x -= 5

        #RIGHT
        if keys[pygame.K_RIGHT] and self.rect.right < 1000:
            self.orientation = "R"
            self.dash_speed = 10
            if keys[pygame.K_z] and not self.dashing and self.dash_cooldown == 30:  
                self.start_dash()
                self.start_cooldown = True
            else:
                #Normal movement
                sprite_x,sprite_y = self.rect.topleft
                if not self.attack_status:
                    self.image = self.player_right
                    self.rect = self.image.get_rect(topleft = (sprite_x,sprite_y))
                self.rect.x += 5

        #Attack
        if keys[pygame.K_x] and not self.attack_status and self.attack_cooldown == 40:
            self.start_attack()
            self.start_attack_cooldown = True   
            self.hit_sound.play()
            if self.orientation == "R":
                sprite_x,sprite_y = self.rect.topleft
                self.image = self.sword_right
                self.rect = self.image.get_rect(topleft=(sprite_x,sprite_y))
                
            elif self.orientation == "L":
                sprite_x,sprite_y = self.rect.topright
                self.image = self.sword_left
                self.rect = self.image.get_rect(topright=(sprite_x,sprite_y))



    def apply_gravity(self):
        if self.rect.bottom < 500:
            self.y_speed += 1
        self.rect.y += self.y_speed

        if self.rect.bottom >= 500: 
            self.rect.bottom = 500
            self.y_speed = 0
    
    

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

    def apply_atack(self):
        if self.attack_status: 
            if self.attack_duration > 0:
                self.attack_duration -= 1
            else:
                self.attack_duration = 20
                self.attack_status = False
                if self.orientation == "R":
                    sprite_x,sprite_y = self.rect.topleft
                    self.image = self.player_right
                    self.rect = self.image.get_rect(topleft=(sprite_x,sprite_y))
                else:
                    sprite_x,sprite_y = self.rect.topright
                    self.image = self.player_left
                    self.rect = self.image.get_rect(topright=(sprite_x,sprite_y))

    def start_attack(self):
        self.attack_status = True

    def update_attack_cooldown(self):
        if self.start_attack_cooldown:
            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1
            else:
                self.attack_cooldown = 40
                self.start_attack_cooldown = False
              

            

    def start_dash(self):
        self.dashing = True          
        

    def update_cooldown(self):
        if self.start_cooldown:
            if self.dash_cooldown > 0:
                self.dash_cooldown -= 1
            else:
                self.dash_cooldown = 30
                self.start_cooldown = False

    def reset_position(self):
        self.rect.bottomleft = (0,200)  
        self.y_speed = 0 


    def update(self):  
        keys = pygame.key.get_pressed()
        self.player_input(keys)
        self.apply_gravity()  
        self.update_cooldown()  
        self.update_attack_cooldown()
        self.apply_dash()
        self.apply_atack()
