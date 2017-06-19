import sys
import math

def norma(t): # funcao que calcula a norma de um vetor, vetor esse representado como uma lista
	raiz = 0
	quadrados = 0
	for i in t:
		quadrados += i**2 # i**2 = i^2
	raiz = math.sqrt(quadrados)
	return raiz


l = []
l1 = []
l2 = []
i = 0

for s in sys.stdin:    
	x = s.split()
	l.append(map(int,x)) 

for x in l:   # calcula a norma de cada vetor da lista e poe a respectiva norma como elemtno do tuplo
	x = (x,norma(x)) # ficamos com uma lista em que cada elemento e da forma:
	l1.append(x)     # (lista, norma(lista))
 
#print l1

for x in l1: # adiciona etiqueta, para se saber a ordem de entrada na lista
	x = list(x) # ficamos com uma lista em que cada elemento e da forma:
	x += [i]    # (lista, norma(lista), indice de entrada na lista)
	x = tuple(x)
	i += 1
	l2 += [x]

l2 = sorted(l2, key = lambda x: (x[1],-x[2])) 


l = []
for x in l2:
	l.append(x[0])


for x in range(0,len(l)): # acresceta um \n ao fim de cada sublista
	l[x].append('\n')

for x in l:
  sys.stdout.write(' '.join(map(str,x))) # imprime apenas o conteudo de cada sublista
  										 # isto e, nao acrescenta \n












