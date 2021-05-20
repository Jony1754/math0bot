import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['pgf.texsystem'] = 'pdflatex'
plt.rcParams['text.usetex'] = True
# vector=[1,-1,-3,5,-2]
vector=[1, -1,-1]


def isComplex(vector):
  vector=vector-np.real(vector)
  for i in vector:
    if np.round(i,4)!=np.complex128(0):
      return True
  return False

def solucion2(vector):
  listafea=np.roots(vector)
  print(listafea)
  if(isComplex(listafea)):
    fig = plt.figure()  
    fig.text(0.5, 0.5, 'No hay solución en el plano real', horizontalalignment='center', verticalalignment='center', fontsize='xx-large',wrap=True)
    fig.savefig('formula.png')
  else:
    listabonita=[]
    for i in listafea:
      listabonita.append(np.round(i.real,4))
    cad=[]
    listabonita=sorted(listabonita)
    nu=len(listabonita)
    print(listabonita)
    r=0
    var=0
    for j in listabonita:
      if(j!=r):
        for k in range(listabonita.count(j)):
          var+=1
          if(k!=0):
           cad.append('c_'+str(var)+' \cdot '+"n^"+str(k)+" \cdot "+str(j)+"^n")
          else:
            cad.append('c_'+str(var)+" \cdot "+str(j)+"^n ")
      r=j
    fn=""
    for i in cad:
      fn+=i+"+"
    fn=fn[:len(fn)-1]
    fn='$'+fn+'$'
    print(fn)
    fig = plt.figure(figsize=[((len(fn)/2)*0.15),1],dpi=200)  
    fig.text(0.5, 0.5, str(fn), horizontalalignment='center', verticalalignment='center', fontsize='xx-large',wrap=True)
    fig.savefig('formula.png')


solucion2(vector)
# vector=np.roots(vector)
# print(isComplex(vector))