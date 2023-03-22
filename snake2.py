import pygame, sys
# import random

#lancer tout les modules
pygame.init()

#créer la map on lui donnant des valeurs
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock() #initialisation de la du compteur pour les images par secondes
# test_surface = pygame.Surface((50,200)) #création d'une surface
# test_rect = test_surface.get_rect(center = (300,250)) #indique que les surface doit être placé par rapport a son centre relativement au coordonées

#créer une boucle infinis d'affichage et de mise a jour des éléments
while True:
    for event in pygame.event.get(): #création d'une boucle qui check pour les events
        if event == pygame.QUIT:
            pygame.quit()   
            sys.exit() #fermeture de tout programme lancer

    screen.fill((175,215,70)) #change le background color du display screen
    # test_surface.fill((135,206,235))
    # screen.blit(test_surface,test_rect) #permet d'afficher test_surface les arguments ce refère a la position
    pygame.display.update() 
    clock.tick(60) #limiter les frames par secondes a 60


