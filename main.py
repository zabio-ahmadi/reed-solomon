#----------------------------------------------------------------------------
# Created By  : Kurteshi, Ahamadi, Dymarczyk
# Created Date: 06.12.2021
# finisehd Date : 22.12.2021
# version ='1.0'
# ---------------------------------------------------------------------------
# MAIN
from lib import  *
#librairie calculant le nombre de points équivalents
from collections import Counter
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

pt_list = [(index, value) for index, value in enumerate(pt_list)]

# étape 01 : on crée une list des point erroné 
points_erreur  = pt_list[0:23] #récuère les 23 premiers points de la liste

# étape 02 : on crée une list des points intacts 
points_correct = pt_list[24:len(pt_list)] #récupère les derniers points de la liste à partir du 24 ème

# list de combinaison des point erronés
combinaison_list = combinaison_points(points_erreur)
#print(combinaison_list)
nb_premier = 337

def calcul_lagrange_polynomes():
    polynom_list = [] # création liste de polynome
    for i in combinaison_list:
        # liste longeur message
        lst_point = i.copy()
        lst_point.extend(points_correct)
        
        polynome = lagrange(lst_point,nb_premier)
        
        polynom_list.append([1, polynome])
        for p in polynom_list:
            if Counter(polynome) == Counter(p[1]):
                p[0] +=1
    

    # le + de apparitions
    tmp = 0
    polynomes_occurance_max = 0
    for pol in polynom_list:
        if tmp < pol[0]: # frequence de la polynomes
            tmp = pol[0]
            polynomes_occurance_max = pol[1].copy()
    return polynomes_occurance_max

polynome_trouve  = calcul_lagrange_polynomes()

la_taile_de_message_de_base = 31
message = ""

# génère le message 
for i in range(0, la_taile_de_message_de_base):
    caractere_unicode = evaluate_polynome(polynome_trouve, i) % nb_premier
    message += chr(caractere_unicode) #retourne le charactère correspondant à son unicode qu'on met dans un string

print("\n\n=============================================================")
print(f'le message : {message}')
print("=============================================================\n\n")
