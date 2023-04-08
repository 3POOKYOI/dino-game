import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen_width = 1280
clock = pygame.time.Clock()
pygame.display.set_caption("Dino Game")

game_font = pygame.font.Font("assets/assets/PressStart2P-Regular.ttf", 24)
dino1 = pygame.image.load("assets/assets/Dino1.png")
dino2 = pygame.image.load("assets/assets/Dino2.png")
ground = pygame.image.load("assets/assets/ground.png")
cactus1 = pygame.image.load("assets/assets/cacti/cactus1.png")
cactus2 = pygame.image.load("assets/assets/cacti/cactus2.png")
cactus3 = pygame.image.load("assets/assets/cacti/cactus3.png")
ground = pygame.transform.scale(ground, (1280, 20))
#ground_rect = ground.get_rect(center=(640, 480))
x_position = 20
y_position= 380
ground_x = 0
ground_y = 400
cactus1_x = 1400
cactus1_y = 380
cactus2_x =1400
cactus2_y = 380
cactus3_x = 1400
cactus3_y = 380
counter = 0
dino_velocity = 0
dino_gravity = 10
game_state = "play"
score = 0



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_state == "play":
        screen.fill("white")
        ground_x = ground_x - 8
        cactus1_x = cactus1_x - 8
        cactus2_x = cactus2_x - 8
        cactus3_x = cactus3_x - 8
        counter = counter + 1

        score_text = game_font.render("Score: " + str(int(score)), True, (0,0,0))
        screen.blit(score_text, (10, 10))


        if (ground_x==-1280):
            ground_x=0
        screen.blit(ground, (ground_x, ground_y))
        screen.blit(ground, (1280 + ground_x, ground_y))

        if (cactus2_x<0):
            cactus2_x=random.randint(1400,3000)
        screen.blit(cactus2,(cactus2_x, cactus2_y))

        if (cactus1_x<0):
            cactus1_x=random.randint(1400,3000)
        screen.blit(cactus1,(cactus1_x, cactus1_y))

        if (cactus3_x<0):
            cactus3_x=random.randint(1400,3000)
        screen.blit(cactus3,(cactus3_x, cactus3_y))

        if (counter >= 15):
            screen.blit(dino1, (x_position, y_position))

            if counter == 30:
                counter = 0


        else:
            screen.blit(dino2, (x_position, y_position))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:

            dino_velocity = 20
            dino_velocity -= dino_gravity
            y_position -= dino_velocity

            if y_position < 320:
                y_position = 320



        else:

                dino_velocity = 0
                dino_velocity += dino_gravity
                y_position += dino_velocity

        if y_position > 380:
            y_position = 380


        if y_position > cactus1_y - 3 and x_position > cactus1_x or (y_position > cactus2_y - 3 and x_position > cactus2_x) or (y_position > cactus3_y - 3 and x_position > cactus3_x):
            game_state = "gameover"
            print(score)

        score += 0.1






    if game_state == "gameover":

        screen.fill("white")
        game_over_text = game_font.render("Game Over", True, (0, 0, 0))
        screen.blit(game_over_text, (500,300))



    pygame.display.update()
    clock.tick(120)