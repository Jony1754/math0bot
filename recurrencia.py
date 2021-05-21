from typing import DefaultDict
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['pgf.texsystem'] = 'pdflatex'
plt.rcParams['text.usetex'] = True


def isComplex(vector):
    vector = vector-np.real(vector)
    for i in vector:
        if np.round(i, 4) != np.complex128(0):
            return True
    return False


def solucion2(vector):
    raices = np.roots(vector)
    print(raices)
    if(isComplex(raices)):
        fig = plt.figure()
        fig.text(0.5, 0.5, 'No hay solución en el plano real', horizontalalignment='center',
                 verticalalignment='center', fontsize='xx-large', wrap=True)
        fig.savefig('formula.png')
        return False
    else:
        raices_reales = []
        for i in raices:
            raices_reales.append(np.round(i.real, 4))
        cad = []
        raices_reales = sorted(raices_reales)
        r = 0
        cont_var = 0
        for j in raices_reales:
            if(j != r):
                for k in range(raices_reales.count(j)):
                    cont_var += 1
                    if(k != 0):
                        cad.append('c_'+str(cont_var)+' \cdot '+"n^" +
                                   str(k)+" \cdot "+str(j)+"^n")
                    else:
                        cad.append('c_'+str(cont_var)+" \cdot "+str(j)+"^n ")
            r = j
        fn = ""
        for i in cad:
            fn += i+"+"
        fn = fn[:len(fn)-1]
        fn = '$'+fn+'$'
        print(fn)
        fig = plt.figure(figsize=[((len(fn)/2)*0.15), 1], dpi=200)
        fig.text(0.5, 0.5, str(fn), horizontalalignment='center',
                 verticalalignment='center', fontsize='xx-large', wrap=True)
        fig.savefig('formula.png')
        plt.clf()
        plt.close()
        return True 