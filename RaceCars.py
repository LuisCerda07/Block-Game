import pygame
import random
import sys
import pygame.transform
import Spawn_Cars
import PointsPlayer
pygame.init()


#---Variables---
Ancho = 980
Alto = 720
game_fps = 60
color_fondo = (126, 143, 131)
color_player = (0, 0, 255)
icon_image = pygame.image.load("Assets/Textures/icon.png")
player_image = pygame.image.load("Assets/Textures/car.png")
player_texture = pygame.transform.scale(player_image, (150, 200))
player = pygame.Rect(0, 720, 150, 200) #POS X, Y / Ancho y Alto
paused_image = pygame.image.load("Assets/Textures/paused.png")
paused_texture = pygame.transform.scale(paused_image,(350,100))
paused_in_game = pygame.Rect(585,300, 100, 350)
stopPaused_image = pygame.image.load("Assets/Textures/stop-paused.png")
stopPaused_texture = pygame.transform.scale(stopPaused_image, (350,200))
options_image = pygame.image.load("Assets/Textures/options.png")
options_texture = pygame.transform.scale(options_image, (350,200))
options_in_game = pygame.Rect(0, 520, 200, 350)
points_image = pygame.image.load("Assets/Textures/point-level.png")
points_texture = pygame.transform.scale(points_image, (400, 150))
points_in_game = pygame.Rect(0, 0, 400, 150)
newLevel_image = pygame.image.load("Assets/Textures/new-level.png")
newLevel_texture = pygame.transform.scale(newLevel_image, (350,100))
newLevel_ingame = pygame.Rect(585,300, 100, 350)
border_image = pygame.image.load("Assets/Textures/border.png")
border_texture = pygame.transform.scale(border_image, (417, 720))
border_in_game = pygame.Rect(550, 0, 417, 720)
font = pygame.font.Font('Assets/Font/slkscr.ttf', 30)
clock = pygame.time.Clock()
level = 0
paused = False
show_texture = False
running = True
flag = False
#----------------#

#TRASH CODE
#color_enemigo = (255, 0, 0)
#size_autos = 100
#num_autos = []      #IS IN THE NEW CARS SPAWN CODE!
#eleted_autos = []
#min_distancia = 120 
#---------------#
counter_YU = 0
counter_YD = 0  #Borrar codigo basura (That dont work on the new movement!)
counter_XL = 0
counter_XR = 0
#---------------#
#vel_autos = 1
#points_player = 0 #IS IN THE NEW POINTS PLAYER CODE!
#enemy = 0
#---------------

#---Posicion del cuadrado (Provisional)---
#pos_X = (Ancho - size_cuadrado) // 2
#pos_Y = (Alto - size_cuadrado) // 2

#pos_X = 650 #This two things is on the new Cars Spawn code!
#pos_Y = -50
#-----------------------------------------

ventana_program = pygame.display.set_mode((Ancho, Alto))
pygame.display.set_caption("RacingGame PORT PC")
pygame.display.set_icon(icon_image)


def paused_game():

    global show_texture, paused

    if show_texture == True:
        ventana_program.blit(paused_texture, paused_in_game)
        ventana_program.blit(stopPaused_texture, options_in_game)
        paused = True

def level_texture():

    global flag

    if flag == True:

        ventana_program.blit(newLevel_texture, newLevel_ingame)


    if PointsPlayer.puntos_player in [550, 1550, 2550]:

        flag = True

    elif PointsPlayer.puntos_player in [650, 1700, 2750]:

        flag = False

def level_enemyPOS():

    global level, flag

    Spawn_Cars.generate_autos(ventana_program, player, game_fps)

    if PointsPlayer.puntos_player <= 350:

        Spawn_Cars.auto_appearance = random.choice(["left", "right"])


    #elif (PointsPlayer.puntos_player == 400 or PointsPlayer.puntos_player == 450) or (PointsPlayer.puntos_player == 1400 or PointsPlayer.puntos_player == 1450 or PointsPlayer.puntos_player == 1550):
    
    elif PointsPlayer.puntos_player in [400, 450, 550, 1400, 1450, 1550, 2400, 2450, 2550]:
        #Spawn_Cars.Y_limit = 10

        #if player.x == 1040:

            #Spawn_Cars.auto_appearance = "left"
            #Spawn_Cars.vel_auto = 5
            #print("right")

        #elif player.x == 330:

        Spawn_Cars.auto_appearance = "right"
        #print("WORKING!")
            
            #if PointsPlayer.puntos_player == 500 or PointsPlayer.puntos_player == 1500:
                #Spawn_Cars.vel_auto += 2
                #print(Spawn_Cars.vel_auto)
                #PointsPlayer.puntos_player += 50
            #Spawn_Cars.vel_auto = 5
            #print("left")

        #if PointsPlayer.puntos_player == 500:

            #Spawn_Cars.vel_auto = 5
    #elif PointsPlayer.puntos_player == 500 or PointsPlayer.puntos_player == 1500:
    
    elif PointsPlayer.puntos_player in [500, 1500, 2500]:

        Spawn_Cars.auto_appearance = "right"
        Spawn_Cars.vel_auto += 2
        print(Spawn_Cars.vel_auto)
        level += 1
        print(level)
        PointsPlayer.puntos_player += 50

    #elif PointsPlayer.puntos_player == 500 or PointsPlayer.puntos_player == 1500:

        #Spawn_Cars.vel_auto += 2
        #print(Spawn_Cars.vel_auto)
        #PointsPlayer.puntos_player += 100

    elif ((PointsPlayer.puntos_player  > 600 and PointsPlayer.puntos_player != 650) or 
          (PointsPlayer.puntos_player > 1700 and PointsPlayer.puntos_player != 1750) or 
          (PointsPlayer.puntos_player > 2700 and PointsPlayer.puntos_player != 2750)):

    #elif PointsPlayer.puntos_player in [600, 1600]:
        #print("TEMULIANO")
        Spawn_Cars.auto_appearance = random.choice(["left", "right"])

    

        #if player.x == 1040:

            #Spawn_Cars.auto_appearance = "left"
            #print("right")

        #elif player.x == 330:

            #Spawn_Cars.auto_appearance = "right"
            #print("left")


    #elif PointsPlayer.puntos_player == 1500:

        #Spawn_Cars.vel_auto = 10


    #elif PointsPlayer.puntos_player > 1600 and PointsPlayer.puntos_player != 1650:

        #Spawn_Cars.auto_appearance = random.choice(["left", "right"])

    #Spawn_Cars.vel_auto = 5
    #flag = True
    #print("level 2")
        
        #if timer == 10:

            #Spawn_Cars.vel_auto = 5
            #flag = True
            

while running:

    #counter_Y += 1
    #points_player = 9999                                                       #Shitty Old give-to-player points test!
    #puntuacion = font.render(f'Puntuación: {SpawnInGame}', True, (0, 0, 0))
    fps = clock.get_fps()
    text_fps = font.render(f'FPS: {int(fps)}', True, (2, 31, 11))
    text_level = font.render(f'Nivel: {level}', True, (2, 31, 11))
    teclas_pressed = pygame.key.get_pressed()

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            running = False

    #if player.colliderect(Spawn_Cars.auto_enemy):

        #print("TEMULIANO")


    #---Player movement---
    #if teclas_pressed[pygame.K_UP]:

        #counter_YU += 50
        #print("PRESSED UP!")

    #if teclas_pressed[pygame.K_DOWN]:

        #counter_YD += 50s
        #print("PRESSED DOWN!")

    if teclas_pressed[pygame.K_RIGHT]:

        if player.x + player.width < Ancho:

            player.x += 250
            #print(player.x)
            #counter_XR += 5
            #print("PRESSED RIGHT!")

    if teclas_pressed[pygame.K_LEFT]:

        if player.x > 0:

            player.x -= 250
            #print(player.x)
            #counter_XL += 5
            #print("PRESSED LEFT!")

    if teclas_pressed[pygame.K_q]:

        pygame.quit()

    if teclas_pressed[pygame.K_p]:

        show_texture = True
        print("Game Paused")

    if teclas_pressed[pygame.K_o]:

        show_texture = False
        paused = False

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


    #---Nuevo Controlador de los counters (X,Y)---
    
    #Controlador counter UP
    if counter_YU >= 500:

        print(counter_YU)
        player.y -= 12
        counter_YU = 0
    
    #Controlador counter DOWN
    if counter_YD >= 500:

        print(counter_YD)
        player.y += 12
        counter_YD = 0

    #Controlador counter RIGHT
    if counter_XR >= 500:

        player.x += 12
        counter_XR = 0
    
    #Controlador counter LEFT
    if counter_XL >= 500:

        player.x -= 12
        counter_XL = 0
    #---------------------------------------------


    #---Controlador de "PERDER"---
    if Spawn_Cars.stop_game == 10:
        
        #RELLENAR CON UN BOTON DE CONTINUAR PARA PODER JUGAR EL JUEGO DE NUEVO
        print("You Lose!")
        continue
    #-----------------------------



    
    #if teclas_pressed[pygame.K_p]:

        #pygame.draw.rect(ventana_program, color_player, paused)
        #paused_game()
        #continue

    #---Bots Cars---
    #pos_Y += 5 #DONT WORK ANYMORE
    #---------------

    ventana_program.fill(color_fondo)
    ventana_program.blit(border_texture, border_in_game)
    ventana_program.blit(points_texture, points_in_game)
    #ventana_program.blit(paused_texture, paused)
    PointsPlayer.points_player(ventana_program)
    #Spawn_Cars.generate_autos(ventana_program, player, game_fps)
    level_enemyPOS()
    ventana_program.blit(border_texture, border_in_game)
    ventana_program.blit(options_texture, options_in_game)
    #pygame.draw.rect(ventana_program, color_enemigo, (pos_X, pos_Y, size_autos, size_autos))
    #pygame.draw.rect(ventana_program, color_player, player)
    ventana_program.blit(player_texture, player)
    paused_game()
    level_texture()
    #pygame.draw.rect(ventana_program, color_enemigo, auto_test)
    ventana_program.blit(text_fps,(20, 20))
    ventana_program.blit(text_level,(20,80))
    #ventana_program.blit(puntuacion,(10,50))
    pygame.display.flip()

    #Regulador de FPS
    clock.tick(game_fps)
pygame.quit()
sys.exit()