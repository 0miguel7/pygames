from sys import exit
import pygame
from classes import Sky, Floor, Player, Enemy

def main():

    #Initialize Window
    pygame.init()
    screen = pygame.display.set_mode((1000,600),flags=pygame.SRCALPHA)
    pygame.display.set_caption("Simple Game")
    clock = pygame.time.Clock()

    sky_group = pygame.sprite.Group()
    sky_group.add(Sky())

    floor_group = pygame.sprite.Group()
    floor_group.add(Floor())

   
    player_group = pygame.sprite.GroupSingle()
    player_group.add(Player())

    enemy_group = pygame.sprite.Group()
    enemy_sprite = Enemy()
    enemy_group.add(enemy_sprite)

    #Pause Game
    game_active = True
    pause_screen = pygame.Surface((1000,600),pygame.SRCALPHA)
    pause_screen.fill((0,0,0,130))
   

    def collision_sprite():
        enemys = pygame.sprite.spritecollide(player_group.sprite,enemy_group,False) #list
        if enemys: 
            for case in enemys:
                if case == enemy_sprite:
                    player_group.sprite.reset_position()
                    case.direction = not enemy_sprite.direction
                    case.decrease_life()
                    
      

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = not game_active 
                screen.blit(pause_screen, (0,0))
            # if event.type == pygame.KEYUP and event.key == pygame.K_z:
            #     player_group.sprite.start_dash()
                


        if game_active:
            #Draw background
            sky_group.draw(screen)
            floor_group.draw(screen)
            
            collision_sprite()
                

            #Draw player group in the screen 
            player_group.draw(screen)
            player_group.update()

            #Draw enemy group in the screen
            enemy_group.draw(screen)
            enemy_group.update()
            
        else:
            
            pass
           
        pygame.display.update()
        clock.tick(60)
            


if __name__ == "__main__":
    main()

