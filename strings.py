# heredoc

my_text1 = """Texte
multi-ligne
abc
foo
bar"""

print(my_text1)

my_text2 = "Texte\nmulti-ligne\nabc\nfoo\nbar"

print(my_text2)


my_number1 = 123
# interpolation avec une f-string
my_text3 = f"Nombre = {my_number1}"
print(my_text3)

# interpolation avec une heredoc f-string
my_text4 = f"""
Le nombre
est
{my_number1}
foo
"""
print(my_text4)

# afficher des accolades dans une heredoc f-string
my_text5 = f"""
{{
foo
}}
{{bar}}
"""
print(my_text5)


my_number2 = 3.14
# concaténation de chaînes de caractères
my_text6 = "Le nombre PI est " + str(my_number2) + "\nEt le nombre d'or est 1.618"
print(my_text6)

# tronquer un float dans une interpolation
# .4f veut dire 4 chiffres après la virgule
my_number3 = 1 / 3
my_text7 = f"1 / 3 ~= {my_number3:.4f}"
print(my_text7)

# les interpolations acceptent les expressions
my_text8 = f"1 + 1 = {1 + 1}"
print(my_text8)


# définition d'une fonction (fonction utilisateur)
# exemple d'écriture de documentation pur une fonction
def hello(name: str) -> None:
    """Cette fonction dit bonjour à quelqu'un

    name str indique le nom de la personne à saluer
    return None
    """
    print(f"Salut {name}")

# appel d'une fonction
hello('Toto')

# affiche la doc d'une fonction
# help(hello)



my_text9 = "Lorem ipsum, dolor sit ipsum amet consectetur adipisicing elit."
# longueur d'une str (nombre de caractères)
my_number4 = len(my_text9)
print(my_number4)

# trouve la position d'une str dans une autre str
my_number5 = my_text9.find('ipsum')
print(my_number5)

my_number5 = my_text9.find('ipsum', my_number5 + 1)
print(my_number5)

# compte le nombre d'occurence d'une str dans une autre str
my_number6 = my_text9.count('ipsum')
print(my_number6)

# remplacement non permanent, la veleur originale ne change pas
print(my_text9.replace('Lorem', 'Foo'))
# remplacement permanent (il suffit d'écraser la variable avec sa nouvelle valeur)
my_text9 = my_text9.replace('Lorem', 'Foo')
print(my_text9)

# éclate une str en liste en utilisant l'espace comme caractère de séparation des éléments.
my_list1 = my_text9.split()
print(my_list1)
# la fontion len() peut aussi être utilisée avec des listes pour compter le nombre d'lélments
print(len(my_list1))

