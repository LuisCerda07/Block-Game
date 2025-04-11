import pygame
import random
import sys
import pygame.transform
import Spawn_Cars
import PointsPlayer
pygame.init()


#---Variables---#
Ancho = 980
Alto = 720
game_fps = 26
color_fondo = (126, 143, 131)
font = pygame.font.Font('Assets/Font/slkscr.ttf', 30)
font_bigger = pygame.font.Font('Assets/Font/slkscr.ttf', 70)
clock = pygame.time.Clock()
level = 0
paused = False
show_texture = False
running = True
flag = False
max_flag = False
#----------------#

#---Textures---#
icon_image = pygame.image.load("Assets/Textures/icon.png")
player_image = pygame.image.load("Assets/Textures/car.png")
player = pygame.Rect(0, 720, 150, 200) #POS X, Y / Ancho y Alto
paused_image = pygame.image.load("Assets/Textures/paused.png")
paused_in_game = pygame.Rect(585,300, 100, 350)
stopPaused_image = pygame.image.load("Assets/Textures/stop-paused.png")
options_image = pygame.image.load("Assets/Textures/options.png")
options_in_game = pygame.Rect(0, 520, 200, 350)
points_image = pygame.image.load("Assets/Textures/point-level.png")
points_in_game = pygame.Rect(0, 0, 400, 150)
newLevel_image = pygame.image.load("Assets/Textures/new-level.png")
newLevel_ingame = pygame.Rect(585,300, 100, 350)
border_image = pygame.image.load("Assets/Textures/border.png")
border_in_game = pygame.Rect(550, 0, 417, 720)
#--------------#

mainWindow = pygame.display.set_mode((Ancho, Alto))
pygame.display.set_caption("RacingGame PORT PC")
pygame.display.set_icon(icon_image)


def paused_game():

    global show_texture, paused

    if show_texture == True:
        mainWindow.blit(paused_image, paused_in_game)
        mainWindow.blit(stopPaused_image, options_in_game)
        paused = True
    return


def level_texture():

    global flag, max_flag, font_bigger, level

    text_newLvl = font_bigger.render(f'{int(level)}', True, (2, 31, 11))
    text_maxLvl = font.render(f'MAX', True, (2, 31, 11))

    if flag == True:

        mainWindow.blit(newLevel_image, newLevel_ingame)
        mainWindow.blit(text_newLvl, (855,320))

    if max_flag == True:

        mainWindow.blit(newLevel_image, newLevel_ingame)
        mainWindow.blit(text_newLvl, (855,305))
        mainWindow.blit(text_maxLvl, (845,360))


    if PointsPlayer.puntos_player in [550, 1550, 2550, 3550, 4550, 5550, 6550, 7550, 8550, 9550]:

        flag = True

    elif PointsPlayer.puntos_player == 10550:

        max_flag = True

    elif PointsPlayer.puntos_player in [650, 1700, 2750, 3800, 4850, 5900, 6950, 8000, 8850, 9900, 10950]:

        flag = False
        max_flag = False
    return


def level_enemyPOS():

    global level, flag

    Spawn_Cars.generate_autos(mainWindow, player, game_fps)

    if PointsPlayer.puntos_player <= 350:

        Spawn_Cars.auto_appearance = random.choice(["left", "right"])

    elif PointsPlayer.puntos_player in [400, 450, 550, 1400, 1450, 1550, 2400, 2450, 2550, 3400, 3450, 3550, 4400, 4450, 4550,
        5400, 5450, 5550, 6400, 6450, 6550, 7400, 7450, 7550, 8400, 8450, 8550, 9400, 9450, 9550, 10400, 10450, 10550]:

        Spawn_Cars.auto_appearance = "right"

    
    elif PointsPlayer.puntos_player in [500, 1500, 2500, 3500, 4500, 5500, 6500, 7500, 8500, 9500, 1500]:

        Spawn_Cars.auto_appearance = "right"
        Spawn_Cars.vel_auto += 3
        print(Spawn_Cars.vel_auto)
        level += 1
        print(level)
        PointsPlayer.puntos_player += 50


    elif ((PointsPlayer.puntos_player  > 600 and PointsPlayer.puntos_player != 650) or 
          (PointsPlayer.puntos_player > 1700 and PointsPlayer.puntos_player != 1750) or 
          (PointsPlayer.puntos_player > 2700 and PointsPlayer.puntos_player != 2750) or
          (PointsPlayer.puntos_player > 3700 and PointsPlayer.puntos_player != 3750) or
          (PointsPlayer.puntos_player > 4700 and PointsPlayer.puntos_player != 4750) or
          (PointsPlayer.puntos_player > 5700 and PointsPlayer.puntos_player != 5750) or
          (PointsPlayer.puntos_player > 6700 and PointsPlayer.puntos_player != 6750) or
          (PointsPlayer.puntos_player > 7700 and PointsPlayer.puntos_player != 7750) or
          (PointsPlayer.puntos_player > 8700 and PointsPlayer.puntos_player != 8750) or
          (PointsPlayer.puntos_player > 9700 and PointsPlayer.puntos_player != 9750) or
          (PointsPlayer.puntos_player > 10700 and PointsPlayer.puntos_player != 10750)):


        Spawn_Cars.auto_appearance = random.choice(["left", "right"])

    return
            

while running:

    fps = clock.get_fps()
    text_fps = font.render(f'FPS: {int(fps)}', True, (2, 31, 11))
    text_level = font.render(f'Nivel: {level}', True, (2, 31, 11))
    teclas_pressed = pygame.key.get_pressed()

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            running = False


    if teclas_pressed[pygame.K_RIGHT]:

        if player.x + player.width < Ancho:

            player.x += 250

    if teclas_pressed[pygame.K_LEFT]:

        if player.x > 0:

            player.x -= 250


    if teclas_pressed[pygame.K_q]:

        pygame.quit()

    if teclas_pressed[pygame.K_p]:

        show_texture = True
        print("Game Paused")

    if teclas_pressed[pygame.K_o]:

        show_texture = False
        paused = False

    #if teclas_pressed[pygame.K_v]:

        #Spawn_Cars.vel_auto += 10

    if paused == True:
        continue
    #---------------------


    #---Limites de la pantalla---
    if player.left > 790: 

        player.left = 790 #AJUSTA LOS LIMITES DE LA PANTALLA DESDE ADENTRO


    if player.right < 730:

        player.right = 730 #AJUSTA LOS LIMITES DE LA PANTALLA DESDE ADENTRO


    if player.bottom > Alto:

        player.bottom = 680


    if player.top < 0:

        player.top = 0
    #----------------------------


    #---Controlador de "PERDER"---
    if Spawn_Cars.stop_game == 10:
        
        #RELLENAR CON UN BOTON DE CONTINUAR PARA PODER JUGAR EL JUEGO DE NUEVO
        print("You Lose!")
        continue
    #-----------------------------

    mainWindow.fill(color_fondo)
    mainWindow.blit(points_image, points_in_game)
    PointsPlayer.points_player(mainWindow)
    level_enemyPOS()
    mainWindow.blit(border_image, border_in_game)
    mainWindow.blit(options_image, options_in_game)
    mainWindow.blit(player_image, player)
    paused_game()
    level_texture()
    mainWindow.blit(text_fps,(20, 20))
    mainWindow.blit(text_level,(20,80))
    pygame.display.flip()

    #Regulador de FPS
    clock.tick(game_fps)
pygame.quit()
sys.exit()