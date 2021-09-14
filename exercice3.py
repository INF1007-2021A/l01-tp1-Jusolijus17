
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = secondes/60/60/24/365

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = (annees - int(annees)) * 52

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = (semaines - int(semaines)) * 7

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = (jours - int(jours)) * 24

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = (heures - int(heures)) * 60

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = (minutes - int(minutes)) * 60

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (int(annees) ,int(semaines) ,int(jours) ,int(heures) ,int(minutes) ,int(secondes))

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
