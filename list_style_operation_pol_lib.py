
# addition of two polynomes 
# on reçoit deux lists de coéficent des polynomes
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


# soustraction of two poylnomes
def soustraction(pol_a, pol_b):

    # we multiply pol_b with -1 
    pol_b = produit(pol_b, [-1])
    # then we add to pol_a 
    result = addition(pol_a, pol_b)
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
 


result = to_readable_polynome([1,2,4,5])


print(result)
