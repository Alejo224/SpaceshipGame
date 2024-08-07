import pygame 
import random
from tkinter import messagebox


pygame.init()


#Configurar la pantalla
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lluvia Espacial")

#colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)

#jugador
player_width = 70 #ancho del jugador
player_height = 70 #largo del jugador
player = pygame.Rect(WIDTH // 2 - player_width // 2, HEIGHT - player_height - 10 , player_width, player_height)

#cargar imágenes
player_img = pygame.image.load("nave.png").convert_alpha()
meteor_img = pygame.image.load("meteorito.png").convert_alpha()
background_img = pygame.image.load("espacio.png").convert_alpha()

#define las nuevas dimenciones
player_size = (80,80)   #nuevo tamaño para la imagen del jugador
meteor_size = (70,70)   #nuevo tamaño para la imagen del meteorito

#redimensiona las imagenes
player_img = pygame.transform.scale(player_img, player_size)
meteor_img = pygame.transform.scale(meteor_img, meteor_size)




#meteoritos
meteor_width = 30   #ancho del meteorito
meteor_height = 30   #largo del meteorito
meteors = []
#diccionario meteoritos con distintas velocidad
FastMeteors = {1 : 4, 2 : 6, 3 : 8, 4 : 10,}

#puntuacion
score = 0
font = pygame.font.Font(None, 36)

#reloj para controlar FPS
clock = pygame.time.Clock()



#Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #CREACION del keys de teclas a presionar
    keys = pygame.key.get_pressed()
    #movimientos horizontales
    if keys[pygame.K_LEFT] and player.left > 0: #Hacia la izquierda
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < WIDTH: #hacia la derecha
        player.x += 5
    
    #movimientos horizontales
    if keys[pygame.K_UP] and player.top > 0:    
        player.y -= 5                           #hacia arriba
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += 5                                   #hacia abajo

    #generar meteoritos
    if len(meteors) < 7:
        meteor = pygame.Rect(random.randint(0, WIDTH - meteor_width ), 0, meteor_width, meteor_height)
        #agregar a la lista el metorio que se ha creado de forma aleatoria
        meteors.append(meteor)

    #MOVER METEORITOS
    for meteor in meteors:
        meteor.y += random.randint(FastMeteors[1],FastMeteors[4])
        if meteor.top > HEIGHT:
            (meteors.remove(meteor)) 
            score +=1


    #Dectetor colisiones
    for meteor in meteors:
        if player.colliderect(meteor):
            running = False
            messagebox.showinfo(message=f"Has chocado \nPuntaje: {score}", title="Gamae over")

    
    screen.fill(BLACK)      #FONDO DE LA PANTALLA

    screen.blit(background_img, (0, 0))

    #pygame.draw.rect(screen, WHITE, player)     #dibujar el jugador
    screen.blit(player_img, player)

    for meteor in meteors:                          #dibujar meteoritos
        #pygame.draw.rect(screen, ORANGE, meteor)
        screen.blit(meteor_img, meteor)

    #mostrar puntuacion
    score_text = font.render(f"Puntuación: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
     
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
