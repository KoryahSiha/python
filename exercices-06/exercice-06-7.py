# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat

my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7

my_list.pop(2)
my_list.insert(1, 'baz')
print(my_list)