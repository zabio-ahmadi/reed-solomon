#----------------------------------------------------------------------------
# Created By  : Kurteshi, Ahamadi, Dymarcyzk
# Created Date: 06.12.2021
# finisehd Date : 22.12.2021
# version ='1.0'
# ---------------------------------------------------------------------------
# LIB V.0.0.1 ALPHA
# ---------------------------------------------------------------------------
# addition of two polynomes 
# on reçoit deux lists de coéficent des polynomes
# on addtion coef par ceof sil exists 
# addtion([2, 1, 3], [4, 3, 1])
def addition(pol_a, pol_b):
    
    if len(pol_a) > len(pol_b):
        pol_max = pol_a
        pol_min = pol_b
    else: 
        pol_max = pol_b
        pol_min = pol_a
    
    result = list()
    for i in range(len(pol_max)):
        
        if i < len(pol_min):
            result.append(pol_max[i] + pol_min[i])
        
        else: 
            result.append(pol_max[i])

    return result

def produit_nb_premier(pol_a, pol_b, nb_premier):
    result = [0] * (len(pol_a) + len(pol_b) - 1)

    for i in range(0, len(pol_a)):

        for j in range(0, len(pol_b)):
            # multiplication avec le même exposant
            result[i + j] += (pol_a[i] * pol_b[j]) % nb_premier
            
    return result

#image du polynom
def evaluate_polynome(pol, point):
    result = 0
    # boucle qui parcours le tableau de polynome en partant de la fin 
    for i in range(len(pol) -1, 0, -1):
         result += point ** i * pol[i] # point puissance i(degré) * polynome 
    result += pol[0]
    return result

#### Lagrange:
# on retourne la poylnome de lagrange:
# notre poylnome de lagrange est de degrée 2 
def lagrange(pts_list, nb_premier):
    polynomes = []
    for i, y in enumerate(pts_list):
        monom = [1] # on calcul a,b,c -> : ax^2 + bx + c 
        for j, x in enumerate(pts_list):
            if j != i:
                # pour chaque probable poylnome on a besoin de deux point
                # ce qui on trouve ici 
                monom = produit_nb_premier(monom , [-x[0] , 1], nb_premier)
                # dénominateur de l'agrange (1-2)(1-3)
                denuminateur = (y[0] - x[0])
                # produit de notre monom avec l'inverse modulaire de notre dénominateur par nb_premier est stoquer dans notre variable monom 
                monom = produit_nb_premier(monom, [mod_inverse(denuminateur, nb_premier)], nb_premier)
        
        monom = produit_nb_premier(monom , [ y[1] ], nb_premier)
        polynomes = addition(polynomes , monom)
    return polynomes


#pt_list = [231, 97, 38, 100, 233, 99, 111, 121, 101, 32, 145, 233, 154, 271, 114, 146, 80, 151, 151, 110, 115, 95, 99, 170, 32, 103, 114, 111, 117, 112, 101, 246, 42, 223, 132, 270, 304, 146, 149, 234, 187, 250, 62, 146, 25, 192, 273, 142, 2, 218, 193, 202, 222]
#print(lagrange(pt_list, 337))

#inverse modulaire par euclide etendu 
def euclide_etendu(dividende, diviseur):
    #initialisation
    x = 1 #x0
    v = 1 #y1
    y = 0 #y0
    u = 0 #x1
    diviseur_pour_inverse = diviseur #permettra de calculer l'inverse modulaire
    #euclide simple
    while diviseur != 0:
        quotient = dividende // diviseur # // : floor division 
        reste = dividende % diviseur
        dividende = diviseur
        diviseur = reste
    #-----------------------------------
    #euclide etendu
        m = u-quotient*x
        n = v-quotient*y
        u = x
        v = y
        x = m
        y = n
    #------------------------------------
    
    # return inverse modulaire
    if diviseur != 0:
        return (v ,u, "NULL")
    else:
        return (v ,u, v % diviseur_pour_inverse)

def combinaison_points(lst_pt):
    result = []

    for i, pt0 in enumerate(lst_pt):
        for j in range(i+1, len(lst_pt)):
            result.append([pt0, lst_pt[j]])
        
    return result
    
# inverse modulaire par method euclid etendu 
def mod_inverse(a, nb_premier):
    return euclide_etendu(a, nb_premier)[2] #récupère inverse qui est le 3ème élément retourner par euclide etendu
