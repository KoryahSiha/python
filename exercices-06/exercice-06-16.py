# exo 6.16
# Ici le but est d'intervertir les éléments de la liste deux à deux
# Liste initiale :
#
#   my_list = [2.71, 42, 123, 2, 3.14, 1.61]
#
# Résultat attendu :
#
#   my_list = [42, 2.71, 2, 123, 1.61, 3.14]

my_list = [2.71, 42, 123, 2, 3.14, 1.61]
      #     0    1    2   3    4     5
      #    -6   -5   -4  -3   -2    -1            
# réponse 6.16

for i in range(0, len(my_list), 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
