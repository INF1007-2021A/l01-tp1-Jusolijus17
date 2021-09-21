

def pointDeRencontre(v1, v2, distance):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    positionVoiture1 = 0
    positionVoiture2 = distance
    v2_negatif = -v2
    # TODO calculer la position de rencontre, assignez la valeur à la variable "positionRencontre"
    while positionVoiture1 != positionVoiture2 :
        positionVoiture1 += v1
        positionVoiture2 += v2_negatif

    positionRencontre = positionVoiture1

    return positionRencontre

if __name__ == '__main__':
    v1 = int(input("Entrez v1: "))
    v2 = int(input("Entrez v2: "))
    distance = int(input("Entrez la distance: "))
    print(pointDeRencontre(v1, v2, distance))
