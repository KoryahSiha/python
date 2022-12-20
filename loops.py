# while == tant que
while False:
    print('ce message ne sera pas affiché')

# @warning boucle infinie
# while True:
    # print('ce message sera affiché en boucle')

counter = 1

while counter:
    print(f"{counter = }")
    counter -= 1
    # même chose
    # counter = counter - 1

counter = 1 # valeur d'initialisation

# le nombre boucle == valeur limite - la première valeur du compteur (valeur d'initialisation)
while counter < 11: # condition de continuation
    print(f"{counter = }") # corps de la boucle
    counter += 1 # l'incrément
    # même chose
    # counter = counter + 1



# boucle de type for == pour
for counter in range(0, 10):
    print(f'{counter = }')

# le 3ème paramètre de range() permet de spécifier l'incrément
# exemple avec un incrément de 2 (au lieu de 1)
for counter in range(0, 10, 2):
    print(f'{counter = }')

# compte à rebours
for counter in range(10, 0, -1):
    print(f'{counter = }')



fruits = ['abricot', 'baie', 'cerise']

# boucle de type for each == pour chaque
for fruit in enumerate(fruits): # prend un fruit dans la liste de fruits

# reversed renvoie un itérateur et économe en mémoire
    print(reversed(fruits))
    print(fruits[::-1])
 
 # [::1] renvoie une liste dont la taille est égale à la liste originale (peut ne pas être)
for fruit in reversed(fruits):
    print(fruit)


my_list = [123, 2, 42, 3.14, 2, 56, 2]
my_number = 2
counter = 0

for item in my_list:
    if item == 2:
        counter += 1
        #print(item)
print(f'{counter = }')


# faire la somme d'une liste avec une boucle
accumulateur = 0

for item in my_list:
    accumulateur += item

print(f'{accumulateur = }')