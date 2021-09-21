import math


def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.

    vitesseIni_en_ms = (vitesseInitiale * 1000) / 3600
    vitesseFinale_en_ms = (vitesseFinale * 1000) /3600
    acceleration = (vitesseFinale_en_ms - vitesseIni_en_ms) / duree

    # TODO calculer la position finale, assigner la valeur à la variable "positionFinale"
    positionFinale = (vitesseIni_en_ms * duree + 1/2 * acceleration * duree**2) + positionInitiale

    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale))
