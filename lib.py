#----------------------------------------------------------------------------
# Created By  : Kurteshi, Ahamadi, Dymarcyzk
# Created Date: 06.12.2021
# version ='1.0'
# ---------------------------------------------------------------------------
# LIB V.0.0.1 ALPHA
# ---------------------------------------------------------------------------
# 
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
    
#multiplication of two polynomes 
def produit(pol_a, pol_b):

    # creating a list with a fixed size  [1,2] * [1,3,4] => [1, 3, 4, 2, 6, 8] : length = 2 * 3 = 6 or [0 until 5 ] == 6 element 
    result = [0] * (len(pol_a) + len(pol_b) - 1)

    for i in range(0, len(pol_a)):

        for j in range(0, len(pol_b)):
            # multiply the coeficents and addition the cofecient which has the same exponent 
            result[i + j] += pol_a[i] * pol_b[j]
            
    return result




#multiplication of two polynomes modulo nombre premier 
def produit_nb_premier(pol_a, pol_b, nb_premier):

    # creating a list with a fixed size  [1,2] * [1,3,4] => [1, 3, 4, 2, 6, 8] : length = 2 * 3 = 6 or [0 until 5 ] == 6 element 
    result = [0] * (len(pol_a) + len(pol_b) - 1)

    for i in range(0, len(pol_a)):

        for j in range(0, len(pol_b)):
            # multiply the coeficents and addition the cofecient which has the same exponent 
            result[i + j] += (pol_a[i] * pol_b[j]) % nb_premier
            
    return result



# soustraction of two poylnomes
def soustraction(pol_a, pol_b):

    # we multiply pol_b with -1 
    pol_b = produit(pol_b, [-1])
    # then we add to pol_a 
    result = addition(pol_a, pol_b)
    return result 

# soustraction of two poylnomes modulo premier 
def soustraction_nb_premier(pol_a, pol_b, nb_premier):
    # then we add to pol_a 
    result = addition(pol_a, produit_nb_premier(pol_b, [-1], nb_premier))
    return result 

    

# finds the image of a polynome 
def evaluate_polynome(pol, point):

    result = 0
    # loop in reversed mood for (int i = size; i >0; i--)
    for i in range(len(pol) -1, 0, -1):
         result += point ** i * pol[i] # image of a polynome on x 
    
    # add the free term ax^2 + 3x + 2 = here add the 2 to our polynome  
    result += pol[0] 
    return result


# on retourne la poylnome de lagrange:
def lagrange(pts_list, nb_premier):
    result = []

    for i, pt0 in enumerate(pts_list):
        pol_lag = [1] # Polynome de lagrane 
        for j, pt in enumerate(pts_list):
            if j != i:
                pol_lag = produit_nb_premier(pol_lag , [-pt[0] , 1], nb_premier)
                x = (pt0[0] - pt[0])
                pol_lag = produit_nb_premier(pol_lag, [mod_inverse(x, nb_premier)], nb_premier)
        pol_lag = produit_nb_premier(pol_lag , [ pt0[1] ], nb_premier)
        result = addition(result , pol_lag)
    return result

# convert list style polynome to string style polynome like (anx^n + an-1x^n-1 + ... a0)
def to_readable_polynome(pol):

    result = ''
    if len(pol) > 1:
        result += str(pol[0]) + ' + '
        for i in range(1, len(pol), 1):
            if i == 1:
                result += str(pol[i])+'x'
            else :
                if i == len(pol) -1:
                    result += ' + ' + str(pol[i])+'x^' + str(i)
                else : 
                    result += ' + ' +  str(pol[i])+'x^' + str(i)
    else :
        if len(pol) == 1:
            result = pol[0]


    return result
 



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



# inverse modulaire par method euclid etendu 
def mod_inverse(a, nb_premier):
    return euclide_etendu(a, nb_premier)[0]


# inverse modulaire par brutforce 
def mod_inverse_brutforce(x,nb_premier):
    for n in range(nb_premier):
        if (x * n) % nb_premier == 1:
            return n
            break

        elif n == nb_premier - 1:
            return "Null"
        else:
            continue


def combinaison_point(lst_pt):
    result = []

    for i, pt0 in enumerate(lst_pt):
        for j in range(i + 1, len(lst_pt)):
            result.append([pt0, lst_pt[j]])
    
    return result