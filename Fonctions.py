import math


def rechercheexhaustive(k, v, s):
    i, nbcont, x = 1, 0, 0

    if s < 0:

        return math.inf

    else:

        if s == 0:

            return 0

        else:

            nbcont = s

            for i in range(1, k):

                x = rechercheexhaustive(k, v, s-v[i])

                if x+1 < nbcont:

                    nbcont = x+1

        return nbcont

def algoprogdyn(k, v, s, res):

    # tab est une matrice de taille S*k

    for i in range(1, k):

        res[s][i] = m(s, i, v)

    return res[s][k]

def m(s, i, v):

    if s == 0:

        return 0

    elif i == 0 and s >= 1:

        return math.inf

    elif s < 0 and i > 1:

        return math.inf

    else:

        return min( m(s, i-1, v), m(s-v[i], i, v)+1)