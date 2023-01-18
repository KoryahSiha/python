# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15

longest_word = ''

for word in my_list:
    if len(word) > len(longest_word):
        longest_word = word

print(my_list.index(longest_word))
print(longest_word)
print(len(longest_word))