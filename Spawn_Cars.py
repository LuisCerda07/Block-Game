import random
import pygame

Y_limit = 720
X1_limit = 580 #Original value: 650
X2_limit = 790 #Original value: 880
auto_enemyCol = (255, 0, 0)
size_auto = 100
x = 0
y = 0
stop_game = 0
player_image = pygame.image.load("C:/Users/luiss/Downloads/car.png")
player_texture = pygame.transform.scale(player_image, (150, 200))
auto_appearance = random.choice(["left", "right"])
#points = 0
#min_distance_X = 120 #PLS DELETE THIS SHIT XD
#min_distance_Y = 520
vel_auto = 3
autos = []
autos_delete = []

#def player_lose():

    #print("Perdiste pedazo de mierda")

def generate_pos():

    global auto_appearance
    
    if auto_appearance == "left":

        position = X1_limit

    elif auto_appearance == "right":

        position = X2_limit

    return position



def generate_autos(pantalla, player, game_fps):

    global x, y, stop_game

    if len(autos) == 0:

        x = generate_pos()
        y = 0 #Original value: -50

        autos.append([x, y, vel_auto])

    if len(autos) == 1:

        x1, y1, vel1 = autos[0]

        if y1 >= 450: #Original value: 350

            while True:
                
                x2 = generate_pos()

                if abs(x2 - x1) >= 0:

                    break
            autos.append([x2, 0, vel_auto])

    for i in range(len(autos)):

        x, y , vel = autos[i]

        y += vel

        if y > Y_limit:

            autos_delete.append(i)
            #points += 50 AND DELETE THIS

        else:
            
            auto_enemy = pygame.Rect(x, y, 150, 200)
            #pygame.draw.rect(pantalla, auto_enemyCol, auto_enemy)
            pantalla.blit(player_texture, auto_enemy)
            autos[i][1] = y

            if auto_enemy.colliderect(player): #LOSE COLIDER, IF PLAYER TOUCH A ENEMY, LOSE THE GAME

                print("YOU LOSE!")
                stop_game = 10


    for i in reversed(autos_delete):

        del autos[i]

    autos_delete.clear()

    #font = pygame.font.SysFont('Segoe Script', 30)
    #puntuacion = font.render(f'Puntuación: {points}', True, (0, 0, 0))
    #pantalla.blit(puntuacion,(10,50))
    return