from sys import exit
import pygame
from classes import Sky, Floor
from Player import Player
from Enemy import Enemy
from Dragon import Dragon

def main():

    #Initialize Window
    pygame.init()
    screen = pygame.display.set_mode((1000,600),flags=pygame.SRCALPHA)
    pygame.display.set_caption("Simple Game")
    clock = pygame.time.Clock()

    font = pygame.font.Font("assets/Pixeltype.ttf",110)
    bg_music = pygame.mixer.Sound("assets/music.mp3")
    bg_music.set_volume(0.15)
    bg_music.play(loops=-1)

    sky_group = pygame.sprite.Group()
    sky_group.add(Sky())

    floor_group = pygame.sprite.Group()
    floor_group.add(Floor())

   
    player_group = pygame.sprite.GroupSingle()
    player_group.add(Player())

    enemy_group = pygame.sprite.Group()
    enemy_sprite = Enemy()
    enemy_group.add(enemy_sprite)

    dragon_sprite = Dragon()

    #Pause Game
    game_active = True
    pause_screen = pygame.Surface((1000,600),pygame.SRCALPHA)
    pause_screen.fill((0,0,0,130))
    


    def collision_sprite():
        enemys = pygame.sprite.spritecollide(player_group.sprite,enemy_group,False) #list
        
        if enemys:
            for case in enemys:
                if case == enemy_sprite:
                    if player_group.sprite.attack_status == True:
                        enemy_sprite.decrease_life()
                    else:
                        player_group.sprite.reset_position()
                        enemy_sprite.life = 5
                        enemy_sprite.direction = not enemy_sprite.direction


        if enemy_sprite.life == 0: 
            enemy_sprite.kill()
        

    def display_enemy_life():

        surf = font.render(str(enemy_sprite.life),True,(60,60,60))
        rect = surf.get_rect(center = (800,100))
        screen.blit(surf,rect)
      

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = not game_active 
                screen.blit(pause_screen, (0,0))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.time.wait(200)
                if enemy_sprite.life == 0:
                    enemy_group.add(enemy_sprite)
                    
                player_group.sprite.reset_position()
                enemy_sprite.rect.midbottom = (700,530)
                enemy_sprite.life = 5

            # if event.type == pygame.KEYUP and event.key == pygame.K_z:
            #     player_group.sprite.start_dash()
                


        if game_active:
            bg_music.set_volume(0.15)
            #Draw background
            sky_group.draw(screen)
            floor_group.draw(screen)
            
            display_enemy_life()

            collision_sprite()
                

            #Draw player group in the screen 
            player_group.draw(screen)
            player_group.update()

            #Draw enemy group in the screen
            enemy_group.draw(screen)
            enemy_group.update()

            
            
        else:
            bg_music.set_volume(0.05)
            
           
        pygame.display.update()
        clock.tick(60)
            


if __name__ == "__main__":
    main()

