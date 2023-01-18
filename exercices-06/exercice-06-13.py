# exo 6.13
# Multipliez chacun des nombres dans la liste par 100, réaffactez le résultat à la place de la valeur originelle puis affichez le résultat

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.13

new_list = []

for i in range(0,len(my_list)):
      new_list.append(my_list[i]*100)  

my_list = new_list
print(my_list)