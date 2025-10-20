import os
import random

import pygame

#Coleur
green_color = (0, 100, 0)
white_color = (255, 255, 255)
red_color = (255, 0, 0)
pygame.init()
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

surface = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Jeu de cartes - KYB-DEV")

DOSSIERS_CARTES = "/home/yan/PycharmProjects/Jeu de Carte/Cartes"
cartes = {}

for fichier in os.listdir(
        DOSSIERS_CARTES):  #os.listdir(DOSSIERS_CARTES): os est un module, listdir recupere la liste des fichiers et dossiers dans le repertoire sous forme de tableau
    if fichier.endswith(".png"):  #Verifie si l element courant se termine par .png
        nom_carte = fichier.replace(".png", "")
        chemin = os.path.join(DOSSIERS_CARTES, fichier)
        cartes[nom_carte] = pygame.image.load(chemin)


class Joueur:
    def __init__(self):
        self.cartes_joueur = []
        self.photo_carte = []
        main = random.sample(list(cartes.keys()), 4)
        for carte in main:
            self.cartes_joueur.append(carte)
            self.photo_carte.append(cartes[carte])


    def jouer(self, carte_jeu):
        couleur = carte_jeu[1]
        numero = carte_jeu[0]
        indices = ["2", "7", "N", "R"]
        for carte in self.cartes_joueur:
            if couleur in carte and numero not in indices:
                self.cartes_joueur.remove(carte)
                self.photo_carte.remove(cartes[carte])
                return cartes[carte]
            elif carte[0] == "2":
                self.cartes_joueur.remove(carte)
                self.photo_carte.remove(cartes[carte])
                return None
            elif numero == "7" or numero == "N" or numero == "R":
                self.faire_piocher(numero)
                return None
        self.piocher()
        return None

    def piocher(self):

        indice = random.choice(list(cartes.keys()))
        self.cartes_joueur.append(indice)
        self.photo_carte.append(cartes[indice])
        return self.photo_carte

    def faire_piocher(self, numero):
        if numero == "7":
            i = 0
            while i != 2:
                self.piocher()
                i = i + 1
        elif numero == "R" or numero == "N":
            i = 0
            while i != 4:
                self.piocher()
                i += 1

    def carte_total(self):

        return self.photo_carte

    def tour(self, mon_tour, carte_du_plateau):
        if mon_tour == 0:
            mon_tour = 1
            return self.jouer(carte_du_plateau)
        else:
            mon_tour = 0
            return JoueurIA().jouer_ia(carte_du_plateau)

        return mon_tour
    def ajouter_carte(self, carte_complet):
        nouvelle = random.choice(list(cartes.values()))
        if nouvelle not in carte_complet:
            carte_complet.append(nouvelle)
        return carte_complet


class JoueurIA:
    def __init__(self):
        self.cartes_joueur = []
        main = random.sample(list(cartes.keys()), 4)
        for carte in main:
            self.cartes_joueur = carte


    def jouer_ia(self, carte_jeu):
        couleur = carte_jeu[1]
        indices = ["2", "7", "N", "R", "A"]
        for carte in self.cartes_joueur:
            numero = carte[0]
            if couleur in carte and numero not in indices:
                return carte
            elif numero == "2":
                self.cartes_joueur.remove(carte)
                return None
            elif numero == "7" or numero == "N" or numero == "R":
                self.faire_piocher(numero)
                return None
            elif numero == "A":
                self.remplacer_carte(carte)
        self.piocher()
        return None

    def piocher(self):

        indice = random.choice(list(cartes.keys()))
        self.cartes_joueur.append(indice)
        del cartes[indice]

    def faire_piocher(self, numero):
        if numero == "7":
            i = 0
            while i != 2:
                self.piocher()
                i = i + 1
        elif numero == "R" or numero == "N":
            i = 0
            while i != 4:
                self.piocher()
                i += 1

    def remplacer_carte(self, carte):
        pass


Carte = pygame.image.load("./recto.png")
Carte.convert_alpha()
carte_rect = Carte.get_rect(topleft=(50, 30))
pioche = Joueur()
pioche.piocher()


def carte():
    c_jeu = random.choice(list(cartes.keys()))
    indices = ["2", "7", "N", "R", "J", "A"]
    c = c_jeu[0]
    if c not in indices:
        carte_jeu = cartes[c_jeu]  # renvoi une image deja charger
        if carte_jeu in Joueur().carte_total():
            return carte_jeu
    return carte()


texte = pygame.font.SysFont("arial", 50, True, False)
star_time = pygame.time.get_ticks()
texte_joueur = texte.render("C' est votre tour", True, white_color, red_color)
texte_joueur_ia = texte.render("C' est le tour du JOUEUR IA", True, white_color, red_color)

carte_du_jeu = carte()
for cle, val in cartes.items():
    if carte_du_jeu == val:
        cle_carte_du_jeu = cle
t= 0
joueur = Joueur()
total_carte = joueur.carte_total()
cartes_rects = []
pos_x, pos_y = 50, 400
decalage_x = 200

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if carte_rect.collidepoint(event.pos):
                joueur.ajouter_carte(total_carte)
            for rect, idx in cartes_rects:
                if rect.collidepoint(event.pos):
                    carte_du_jeu = total_carte[idx]


    for img in total_carte:
        i = len(total_carte)
        while i > -1:
            rect = img.get_rect(topleft=(pos_x + i * decalage_x, pos_y))
            cartes_rects.append((rect, i))  # on garde l’index pour retrouver la carte
            i -= 1
    ecrouler = (pygame.time.get_ticks() - star_time) / 1000  #Seconde
    surface.fill(green_color)
    #if ecrouler < 5:
        #if Joueur().tour(1) == 0:
         #   surface.blit(texte_joueur, (60, 350))
        #else:
         #   surface.blit(texte_joueur_ia, (60, 350))

    surface.blit(Carte, carte_rect)
    surface.blit(carte_du_jeu, (330, 30))
    for img in range(len(total_carte)):
        x, y = 50, 400
        decalage_x = 200
        decalage_y = 0
        surface.blit(total_carte[img], (x + img * decalage_x, y + img * decalage_y))

    pygame.display.flip()