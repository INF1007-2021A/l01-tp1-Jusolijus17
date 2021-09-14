def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat
    fizz = 0
    buzz = 0
    reste = n % 3
    resultat = n

    if reste == 0 :
        resultat = "fizz"
        fizz = 1

    reste = n % 5

    if reste == 0 :
        resultat = "buzz"
        buzz = 1

    if fizz and buzz == 1 :
        resultat = "fizzbuzz"

    return resultat

if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))
