#----------------------------------------------------------------------------
# Created By  : Kurteshi, Ahamadi, Dymarcyzk
# Created Date: 06.12.2021
# version ='1.0'
# ---------------------------------------------------------------------------
# Euclide étendu
# ---------------------------------------------------------------------------
# 
# ---------------------------------------------------------------------------
#
import math
def euclide_etendu(dividende, diviseur):
    #initialisation
    x = 1 #x0
    v = 1 #y1
    y = 0 #y0
    u = 0 #x1
    diviseur_pour_inverse = diviseur #permettra de calculer l'inverse modulaire
    #euclide simple
    while diviseur != 0:
        quotient = dividende //diviseur
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

print(euclide_etendu(414235, 124124))

def mod_inverse(x,m):
    for n in range(m):
        if (x * n) % m == 1:
            return n
            break

        elif n == m - 1:
            return "Null"
        else:
            continue

print(mod_inverse(414235, 124124))




