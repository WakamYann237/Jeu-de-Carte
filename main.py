import os
import random
import time
import pygame

#Coleur
green_color = (0, 100, 0)
white_color = (255, 255, 255)
red_color = (255, 0, 0)
pygame.init()
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jeu de cartes - KYB-DEV")

DOSSIERS_CARTES = "/home/yan/PycharmProjects/Jeu-de-Carte/Cartes"
cartes = {}

for fichier in os.listdir(DOSSIERS_CARTES):  #os.listdir(DOSSIERS_CARTES): os est un module, listdir recupere la liste des fichiers et dossiers dans le repertoire sous forme de tableau
    if fichier.endswith(".png"):  #Verifie si l element courant se termine par .png
        nom_carte = fichier.replace(".png", "")
        chemin = os.path.join(DOSSIERS_CARTES, fichier)
        cartes[nom_carte] = pygame.image.load(chemin)

couleurs = {
    "C" : pygame.image.load("/home/yan/PycharmProjects/Jeu-de-Carte/couleurs/coeur.png"),
    "F": pygame.image.load("/home/yan/PycharmProjects/Jeu-de-Carte/couleurs/fcarreau.png"),
    "P": pygame.image.load("/home/yan/PycharmProjects/Jeu-de-Carte/couleurs/pique.png"),
    "T": pygame.image.load("/home/yan/PycharmProjects/Jeu-de-Carte/couleurs/trefle.png")
}

class Joueur:
    def __init__(self):
        self.cartes_joueur = []
        self.photo_carte = []
        main = random.sample(list(cartes.keys()), 4)
        for carte in main:
            self.cartes_joueur.append(carte)
            self.photo_carte.append(cartes[carte])

    def verification(self, carte_jeu,carte_du_joueur):
        cle_carte_du_jeu = ""
        for cle, val in cartes.items():
            if carte_jeu == val:
                cle_carte_du_jeu = cle
        couleur_du_jeu = cle_carte_du_jeu[1]
        c = cle_carte_du_jeu[0]
        cle_du_joueur = ""
        for jo_cle, jo_val in cartes.items():
            if carte_du_joueur == jo_val:
                cle_du_joueur = jo_cle
        couleur_du_joueur = cle_du_joueur[1]
        jocker = cle_du_joueur[0]
        if couleur_du_joueur == couleur_du_jeu:
            return True
        elif (couleur_du_jeu == "A" or couleur_du_jeu == "P") and jocker == "N":
            return True
        elif (couleur_du_jeu == "B" or couleur_du_jeu == "C") and jocker == "R":
            return True
        elif c == "N" and (couleur_du_joueur == "A" or couleur_du_joueur == "P"):
            return True
        elif c == "R" and (couleur_du_joueur == "B" or couleur_du_joueur == "C"):
            return True
        elif c == jocker:
            return True
        else:
            return False

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
couleur_coeur = couleurs["C"]
rect_coeur = couleur_coeur.get_rect(topleft=(150, 30))
couleur_trefle = couleurs["T"]
rect_trefle = couleur_trefle.get_rect(topleft=(160, 30))
couleur_pique = couleurs["P"]
rect_pique = couleur_pique.get_rect(topleft = (170, 30))
couleur_carreau = couleurs["F"]
rect_carreau = couleur_carreau.get_rect(topleft = (180, 30))
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
texte_joueur_ia = texte.render("Reflexion de l' IA", True, white_color, red_color)

carte_du_jeu = carte()
t= 0
joueur = Joueur()
joueur_ia = JoueurIA()
total_carte = joueur.carte_total()
cartes_rects = []
pos_x, pos_y = 50, 400
decalage_x = 200
tour = "joueur"
message = ""

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

        if tour == "joueur":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if carte_rect.collidepoint(event.pos):
                    joueur.ajouter_carte(total_carte)
                    tour = "IA"
                for rect, idx in cartes_rects:
                    if rect.collidepoint(event.pos):
                        if joueur.verification(carte_du_jeu, total_carte[idx]):
                            carte_du_jeu = total_carte[idx]
                            tour = "IA"

    for img in total_carte:
        i = len(total_carte)
        while i > -1:
            rect = img.get_rect(topleft=(pos_x + i * decalage_x, pos_y))
            cartes_rects.append((rect, i))  # on garde l’index pour retrouver la carte
            i -= 1
    surface.fill(green_color)
    surface.blit(Carte, carte_rect)
    surface.blit(carte_du_jeu, (330, 30))
    tmp = 0
    for i in range(len(total_carte)):
        if i > 8:
            decalage_y = 0
            pos_x, pos_y = 50, 800
            surface.blit(total_carte[i], (pos_x + tmp * decalage_x, pos_y + tmp * decalage_y))
            tmp += 1
        else:
            x, y = 50, 400
            decalage_x = 200
            decalage_y = 0
            surface.blit(total_carte[i], (x + i * decalage_x, y + i * decalage_y))
    for img in total_carte:
        if carte_du_jeu == img:
            total_carte.remove(img)
    if tour == "IA":
        surface.blit(texte_joueur_ia, (150, 30))
        pygame.display.update()
        time.sleep(1)
        tour = "joueur"

    pygame.display.flip()