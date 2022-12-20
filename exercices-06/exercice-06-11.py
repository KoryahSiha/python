# exo 6.11
# Trouvez l'index de la valeur `3.14` dans la liste et affichez le résultat
# Note : faites une boucle et n'utilisez pas la méthode `index()`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.11

index = []

for element in range(len(my_list)):
    if my_list[element] == 3.14:
        index.append(element)
print(index)