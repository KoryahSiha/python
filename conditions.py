import random

if True:
    print("La condition est vraie")
    print("Ce code est exécuté")

if False:
    print("La condition est fausse")
    print("Ce code n'est pas exécuté")

conditions_vente = True

# meilleure écriture pour vérifier s'il a accepté
if conditions_vente:
    print("L'utilisateur a accepté les conditions de vente")
else:
    print("L'utilisateur n'a pas accepté les conditions de vente")

# meilleure écriture pour vérifier s'il n'a accepté

if not conditions_vente:
    print("L'utilisateur n'a pas accepté les conditions de vente")
else:
    print("L'utilisateur a accepté les conditions de vente")


emails = random.randint(0, 3)
print(emails)

# elif c'est la même chose que else if

if emails == 1:
    print("Vous avez un nouveau mail")
elif emails > 1:
    print(f"Vous avez {emails} nouveaux mails")
else:
    print("Vous n'avez pas de nouveaux mails")



windows_closed = bool(random.randint(0, 1))
electricity_off = bool(random.randint(0, 1))

print(f'{windows_closed = }')
print(f'{electricity_off = }')


if windows_closed and electricity_off:
    print("Les fenêtres sont fermées")
    print("L'électricité est coupée")
elif not windows_closed and electricity_off:
    print("Les fenêtres ne sont pas fermées")
    print("L'électricité est coupée")
elif windows_closed and not electricity_off:
    print("Les fenêtres sont fermées")
    print("L'électricité n'est pas coupée")
else:
    print("Les fenêtres ne sont pas fermées")
    print("L'électricité n'est pas coupée")


bank_card = True
cash = True
print(f'{bank_card = }')
print(f'{cash = }')

if bank_card or cash:
    print("On a un moyen de paiement")
else:
    print("On n'a aucun moyen de paiement")


ticket = bool(random.randint(0, 1))
vip = bool(random.randint(0, 1))
registration = bool(random.randint(0, 1))

print(f'{ticket = }')
print(f'{vip = }')
print(f'{registration = }')

# Quand on mélange or et and, il faut toujours utilsier les paranthèses
if (ticket or vip) and registration:
    print("Access authorized")
else:
    print("Access not authorized")


product_count = random.randint(0, 50)
print(f'{product_count =}')

if product_count > 20:
    print("Il y a plus de 20 articles")
    print("RAS")
elif 5 < product_count <= 20:
    print("Il y a plus de 5 articles")
    print("Alert approvisionnement")
elif 0 < product_count <= 5:
    print("Il y a plus de 0 articles")
    print("Alerte rupture imminente")
else:
    print("Il n'y a plus d'articles")
    print("Alerte rupture")



product_count = 6

# équivalent d'un encadrement python
if product_count > 5 and product_count <= 20:
    print("Il y a plus de 5 articles")
    print("Il y a 20 ou moins d'articles")