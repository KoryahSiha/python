# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat

my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7

my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)