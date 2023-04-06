from sys import exit
import pygame
from classes import Sky, Floor, Player

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

    #Pause Game
    game_active = True
    pause_screen = pygame.Surface((1000,600),pygame.SRCALPHA)
    pause_screen.fill((0,0,0,130))
   


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

            #Draw player group in the screen 
            player_group.draw(screen)
            player_group.update()
        else:
            
            pass
           
        pygame.display.update()
        clock.tick(60)
            



if __name__ == "__main__":
    main()

