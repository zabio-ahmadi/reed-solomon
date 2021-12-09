#### Petites fonctions pour manipuler des polynômes (avec coefficients en float ou int).
#### Le polynôme a0 + a1*x + a2*x^2 + ... + an*x^n est supposé codé sous forme de liste [a0,a1,a2,...,an]
#### On ne veut pas avoir de termes égaux à 0 en fin de liste (on suppose que xn != 0, donc)
#### Du coup, le degré d'un polynôme correspond à la longueur de la liste -1.
#### ATTENTION: comme on manipule des float (ou des int si tous les coeffs sont des int), on peut avoir des erreurs
#### d'arrondi, et des coefficients qui ne disparaissent pas... 

#### Addition de deux polynômes:

def addition(a,b):
    m = max(len(a),len(b))
    s0 = [0 for k in range(m)]
    for k in range(m):
        if (k<len(a)):
            s0[k] += a[k]
        if (k<len(b)):
            s0[k] += b[k]
    n = m-1
    while (s0[n] == 0 and n > 0):
        n = n-1
    return s0[0:n+1]

#### Produit de deux polynômes:

def produit(a,b):
    p = [0 for l in range(len(a)+len(b)-1)]
    for k in range(len(a)):
        for l in range(len(b)):
            p[k+l] +=  a[k]*b[l]
    return p

#### Addition de deux polynômes:

def soustraction(a,b):
    return addition( a , produit( b , [-1] ) )

#### Lagrange:

def lagrange( pts_list ):
    L = [0]
    for j,pt0 in enumerate( pts_list ):
        l_j = [1]
        for k, pt in enumerate( pts_list ):
            if k!= j:
                l_j = produit(l_j , [-pt[0] , 1] )
                l_j = produit(l_j , [ 1/(pt0[0]-pt[0]) ] )
        l_j = produit( l_j , [ pt0[1] ] )
        L = addition( L , l_j )
    return L

#### Evaluation d'un polynôme pol en un point a:

def evalp( pol , a ):
    n = len(pol)-1
    v = pol[n]
    for k in range(len(pol)-1,0,-1):
        v = v*a + pol[k-1]
    return v

#### Ecrire un polynôme de manière un peu plus lisible

def writep( pol ):
    s = ''
    for l,k in enumerate(pol):
       if k != 0:
           if l == 0:
               s+= str(k) + ' '
           else:
               s += '+ '
               if k != 1: 
                   s += str(k)+'*'
               if l == 1:
                   s += 'x '
               else:
                   s += 'x^'+str(l) + ' '
    return s  
              










