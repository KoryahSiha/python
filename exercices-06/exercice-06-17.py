# exo 6.17
# Affichez la valeur qui se trouve à la colonne 4, ligne 3
# ATTENTION : il faut faire `- 1` pour obtenir les index correspondant

import random

size = 5
matrix = []

for _ in range(0, size):
    row = [random.randint(40, 100) for _ in range(0, size)]
    matrix.append(row)

print(matrix)

# réponse 6.17
# 64 donc index 3 2

for line in range(0, size):
    for col in line:
        
        print(matrix[3:2])


# [
#     [55, 66, 49, 43, 92],
#     [93, 52, 82, 42, 99],
#     [99, 72, 91, 66, 76],
#     [96, 100, 57, 85, 54],
#     [81, 85, 64, 99, 93]
# ]


# #Si accès uniquement aux éléments
# for line in matrice:
#     for col in line:
#         #Traitement avec les éléments


# y = len(M[0])
# for i in range(0,y):
#     for j in range(0,y):
#         matriceval[i,j]= M[i,j] - (M[i,j]+M[j,i]+M[n-1-i,j]+M[j,n-1-i]+M[n-1-i,n-1-j]+M[n-1-j,n-1-i]+M[n-1-j,i]+M[i,n-1-j])/8