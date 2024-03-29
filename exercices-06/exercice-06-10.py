# exo 6.10
# Calculez la moyenne des nombres de la liste et affichez le résultat

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.10

def average(numbers: list) -> float:
    """
    Cette fonction permet de calculer la moyenne des nombres d'une liste.
    numbers est la liste des nombres.
    return la moyenne obtenue en divisant la somme des nombres par la longueur de la liste.
    """
    somme = 0

    for number in numbers:
        somme += number

    result = somme / len(my_list)

    return result

result = average(my_list)
print(result)