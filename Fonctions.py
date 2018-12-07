import numpy as np
import re
import time


def lecturefichier(f):

    with open(f, "r") as file:


        S = file.readline()
        k = file.readline()

        V = [[0] * k for i in range(S)]

        V[0] = list(map(int, file.readline(k).split()))

    return k,V[0],S

def lecture(f):

    with open(f,"r") as file:

        temp = file.readlines()

    return int(temp[0]), int(temp[1]), list(map(int, temp[2].split())) #s, k et v renvoyés

def genfichieralea(nom, k, pmax, s):
    """
    crée un fichier txt avec :
       ligne 1: valeur s > pmax, plus petite que smax
       ligne 2: valeur k
       ligne 3: tableaux trié des capacités croissantes dont la dernière est inférieure a pmax.
    """

    file = open(nom, "w+")

    #s = np.random.randint()
    #k = np.random.randint(2, high = k)
    v = 1+ np.random.randint(2, high = pmax, size = k-1)
    v.sort()


    file.write(str(s) + "\n")
    file.write(str(k) + "\n")
    file.write(re.sub('[\[\]]','',np.array2string(v)))

    file.close()


def genfichierexpo(nom, s, k, d):

    with open(nom,"w+") as file:
        v = " ".join([str(d**i) for i in range(k)])
        file.write(str(s) + "\n")
        file.write(str(k) + "\n")
        file.write(v)
    return nom



def timerfunc(func):
    """
    A timer decorator
    """

    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "The runtime for {func} took {time} seconds to complete"
        print(msg.format(func=func.__name__,
                         time=runtime))
        return value

    return function_timer

def rechercheexhaustive(k, v, s):

    i, nbcont, x = 1, 0, 0

    if s < 0:

        return float("inf")

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

        return float("inf")

    elif s < 0 and i > 1:

        return float("inf")

    else:

        return min( m(s, i-1, v), m(s-v[i], i, v)+1)


def algoglouton(S,k, v):

    res = 0
    i = k-1
    while S > 0:

        if S < v[i]:

            i-=1

        elif S >= v[i]:

            res += S // v[i]
            S = S - (S // v[i]) * v[i]
            i-=1

    return res


def TestGloutonCompatible(k, v):

    j,S = 0, 0

    if k >= 3:

        for S in range(v[3]+2, v[k-1]+v[k]-1):

            for j in range (1,k):

                if v[j] < S & algoglouton(S) > 1+algoglouton(S-v[j]):

                    return False
    return True