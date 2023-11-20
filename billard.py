import pygame
import sys
import pymunk
import pymunk.pygame_util
pygame.init()

largeur=800
longueur=600
écran=pygame.display.set_mode((largeur,longueur)) #une fenetre pour le jeu avec 800x600 pixels
pygame.display.set_caption('billiard') # titre de la fenetre

espace=pymunk.Space()
draw_options =pymunk.pygame_util.DrawOptions(écran)
def draw_ball(rayon,pos,couleur):
    balle= pymunk.Body()
    balle.position =pos
    forme=pymunk.Circle(balle,rayon)
    forme.mass=5
    
#couleurs
blanc=(255,255,255)
vert=(0,128,0)
noir=(0,0,0)

condition=True   
while condition is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #FONCTION POUR UNE LOUPE CONTINUE SAUF SI ON QUITTE LE JEU
            pygame.quit()
            sys.quit()
            condition=False
    écran.fill(vert)
    espace.debug_draw(draw_options)
    pygame.display.update()

