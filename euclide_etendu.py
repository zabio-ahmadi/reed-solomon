#----------------------------------------------------------------------------
# Created By  : Kurteshi, Ahamdi, Dymarzyck
# Created Date: 06.12.2021
# version ='1.0'
# ---------------------------------------------------------------------------
# Euclide étendu
# ---------------------------------------------------------------------------
# Imports Line 5
# ---------------------------------------------------------------------------
#
import math
def euclide_etendu(dividende, diviseur):
    x = 1
    v = 1
    y = 0
    u = 0
    inverse_modulaire = diviseur
    while diviseur != 0:
        quotient = dividende //diviseur
        reste = dividende % diviseur
        m = u-quotient*x
        n = v-quotient*y
        dividende = diviseur
        diviseur = reste
        u = x
        v = y
        x = m
        y = n
    
    return (u ,v, )

print(euclide_etendu(108, 309))



