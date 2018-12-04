import timeit
import time
from Fonctions import *



def question12():
    """
    trace les courbes de temps d'execution en fonction de s et k en les faisant varier
    """
    #crée fichier pour le graphique

    fileS1 = open("q12graphiqueS1.txt", "w")
    fileS2 = open("q12graphiqueS2.txt", "w")
    fileS3 = open("q12graphiqueS3.txt", "w")

    filek1 = open("q12graphiquek1.txt", "w")
    filek2 = open("q12graphiquek2.txt", "w")
    filek3 = open("q12graphiquek3.txt", "w")

    #boucles pour benchmark
    #cree fichier bonne taille
    #ajoute aux fichiers le temps en fonction du paramètre

    for s in range(25, 75):

        f = genfichierexpo("f.txt", s, 10, 2)
        s, k, v = lecture(f)

        start = time.time()
        rechercheexhaustive(k, v, s)
        #algoglouton(s, k, v)
        end = time.time()
        elapsed = str(end-start)



        fileS1.write(str(s) + " " + elapsed + '\n' )
        #fileS2.write( s + " " + str(timeit.timeit(algoprogdyn(k,v,s,res))))
        #fileS3.write( str(s) + " " + elapsed2 +'\n')

    for k in range(2, 15):

        f = genfichierexpo("f.txt", 2000,k, 2)
        s, k, v = lecture(f)

        start = time.time()
        # rechercheexhaustive(k, v, s)
        algoglouton(s, k, v)
        end = time.time()
        elapsed = str(end - start)

        filek1.write(str(s) + " " + elapsed + '\n' )
        #fileS2.write( s + " " + str(timeit.timeit(algoprogdyn(k,v,s,res))))
        filek3.write(str(s) + " " + elapsed + '\n')



def question13():
    """


    """
    nbCompatibles = 0
    nbtotal = 10000

    for i in range(nbtotal):

        genfichieralea("falea.txt", 5, 5000, 100000)
        s, k, v = lecture("falea.txt")

        if TestGloutonCompatible(k, v):

            nbCompatibles += 1

    return nbCompatibles/nbtotal


def question14():
    """


    """

question12()
#question13()
