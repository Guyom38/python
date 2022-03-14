# --- importation des librairies Pygame 
import pygame
from pygame.locals import *

# --- initialisation du moteur Pygame
pygame.init()

# --- création de la fenetre
fenetre = pygame.display.set_mode((1024, 768), pygame.DOUBLEBUF, 32)
pygame.display.set_caption("Mon prog Pygame")

# --- création d'un horloge pour limiter le raffraichissement
horloge = pygame.time.Clock()

boucle = True
while boucle:
    # --- récupére l'ensemble des évènements
    for event in pygame.event.get():        
        # --- si l'utilisateur clic sur la croix, ou appuie sur la touche ESCAPE
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            boucle = False

        # --- si l'utilisateur presse l'une des fleches de direction
        if event.type == KEYDOWN:  
            if event.key == K_LEFT: print("la touche gauche")
            if event.key == K_RIGHT: print("la touche droite")
            if event.key == K_UP: print("la touche haut")
            if event.key == K_DOWN: print("la touche bas")

    # --- remplissage de la fenetre avec une couleur proche du noir
    fenetre.fill((16,16,16))

    # --- affiche le message Hello World
    ecriture = pygame.font.SysFont('arial', 40) 
    image_texte = ecriture.render("Hello world", True, (255,0,0)) 
    fenetre.blit(image_texte, (150, 150))

    # --- afficher le résultat
    pygame.display.update()

    # --- limite la fréquence de raffraichissement a 25 images seconde
    horloge.tick(25)

# --- en sortie de boucle, quitte le programme
pygame.quit() 