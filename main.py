#----------------------------------------------------------------------------
# Created By  : Kurteshi, Ahamadi, Dymarcyzk
# Created Date: 06.12.2021
# version ='1.0'
# ---------------------------------------------------------------------------
# LIB V.0.0.1 ALPHA
# ---------------------------------------------------------------------------
# 
# ---------------------------------------------------------------------------
#

# from lib import lagrange
from lib import  *
"""
GROUPE 12

Les données du problème 
-----------------------

Le nombre premier              : 337
La longueur du message de base : 31
Le nombre de points ajoutés    : 22
le nombre maximal d'erreurs    : 11
qui sont situées avant l'indice: 24

la liste reçue : 
[231, 97, 38, 100, 233, 99, 111, 121, 101, 32, 145, 233, 154, 271, 114, 146, 80, 151, 151, 110, 115, 95, 99, 170, 32, 103, 114, 111, 117, 112, 101, 246, 42, 223, 132, 270, 304, 146, 149, 234, 187, 250, 62, 146, 25, 192, 273, 142, 2, 218, 193, 202, 222]"""


pt_list = [231, 97, 38, 100, 233, 99, 111, 121, 101, 32, 145, 233, 154, 271, 114, 146, 80, 151, 151, 110, 115, 95, 99, 170, 32, 103, 114, 111, 117, 112, 101, 246, 42, 223, 132, 270, 304, 146, 149, 234, 187, 250, 62, 146, 25, 192, 273, 142, 2, 218, 193, 202, 222]

pt_list = [(index, value) for index, value in enumerate(pt_list) ]

# étape 01 : on crée une list des point erroné 
les_points_erroné  = pt_list[0:23]

# étape 02 : on crée une list des points intacts 
les_pionts_intacts = pt_list[24:len(pt_list)]

import itertools
from collections import Counter

# list de combinaison des point erronés
cobinaison_list = [list(p) for p in itertools.combinations(les_points_erroné, 2)]

nb_premier = 337



def calcul_lagrange_polynomes():
    polynom_list = [] # list des poylnomes


    for i in cobinaison_list:
        # Creer la liste de points de 31 elements
        les_points_corrects = i.copy()
        les_points_corrects.extend(les_pionts_intacts)

        flag_new_poly = True

        # Calcule de lagrange pour les points qui sont correct
        polynome = lagrange(les_points_corrects,nb_premier)


        #Verifi le polynome au tableau pour compter les apparitions
        for r in polynom_list:
            if Counter(polynome) == Counter(r[1]):
                r[0] += 1
                flag_new_poly = False

        if flag_new_poly:
            polynom_list.append([1, polynome])
    
    print("Il y a {} listes de points et {} polynomes de lagrange".format(len(cobinaison_list), len(polynom_list)))

    # Comparre les aparitions pour retourner celle qui apparrait le plus
    tmp = 0
    val = 0
    for pol in polynom_list:
        if tmp < pol[0]:
            tmp = pol[0]
            val = pol[1].copy()
    return val

polynome_trouvé  = calcul_lagrange_polynomes()

print("=============================================================")
print(f'polynome trouvée est :\n{to_readable_polynome(polynome_trouvé)}')
print("=============================================================")

la_taile_de_message_de_base = 31
message = ""

# génère le message 
for i in range(0, la_taile_de_message_de_base):
    ch = round((evaluate_polynome(polynome_trouvé, i) % nb_premier))
    message += chr(ch)


print("\n\n=============================================================")
print(f'le message : {message}')
print("=============================================================\n\n")



