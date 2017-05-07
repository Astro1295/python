import random
def operation(nb,nb1, op):
    i = 0
    max =10
    if op == 1:
        while i < max:
            print(i + 1, "*", nb, "=", (i + 1) * nb)
            print(">>>>>>>>",i + 1, "*", nb1, "=", (i + 1) * nb1)
            i += 1
    elif op == 2:
        print ("La somme des deux nombre est :", nb+nb1)
    elif op == 3:
        try:

            resultat = nb / nb1

        except NameError:

            print("La variable numerateur ou denominateur n'a pas été définie.")

        except TypeError:

            print("La variable numerateur ou denominateur possède un type incompatible avec la division.")

        except ZeroDivisionError:

            print("La variable denominateur est égale à 0.")


def random_number(nb):
    y = random.randint(0, nb)
    print("Valeur du nomre aléatoire est:",y)
    return y


# vérification des randomes si pair ou impair
def pair_impair(nb,nb1):
    A = nb % 2
    B = nb1 % 2

    A = int(A)
    B = int(B)

    if A == 0:
        if B == 0:
            return True

        else:
            return Falseyou
    elif A != 0:
        if B == 0:
            return False
        else:
            return True

def Casino (Somme, demande):
    X = random_number(49)
    if X == demande:
        print("Bravo vous avez gagné")
        Somme = Somme * 3
        print(Somme)
        return Somme
    else:
        if pair_impair(demande, X):
            Somme = Somme + (Somme / 2)
            print("Les chiffres sont pas de meme valeur mais du meme groupe ")
            print(Somme)
            return Somme
        else:
            print("Les chiffre sont différents et non du meme groupe*** ARGENT PERDU***")
            Somme = 0
            print(Somme)








