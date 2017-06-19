import sys


g = {} # grafo do input
novoGrafo = {} # grafo final, para onde vamos copiar tudo
l = [] # lista dos nodos (sem repeticoes)


for s in sys.stdin:
	l = s.split()
	if l[0] in g:
		g[l[0]].append(l[1])
	else:
		g[l[0]] = [l[1]]
	if l[1] in g:
		g[l[1]].append(l[0])
	else:
		g[l[1]] = [l[0]]

l = sorted(list(g))
novoGrafo = dict.fromkeys(g.keys(),[]) # grafo igual ao g, mas com as listas vazias. Apenas com as chaves
print g
for x in g:       
	#print('\n')
	#print g
	for i in l:
		#print(l)
		if i not in g[x] and i not in novoGrafo[x] and i != x: # daqui sai o grafo complementar ao recebido(mas nao orientado)
			novoGrafo[x] = novoGrafo[x] + [i]



#print(novoGrafo)		
	
l1 = [] # lista nova que vai conter os pares de caminhos
for newaresta in sorted(novoGrafo):
	#print newaresta,
	for elem in sorted(novoGrafo[newaresta]):
		l1 += [(newaresta,elem)]

for i in l1:    #remove caminhos repetidos(inversos)
	if (i[1],i[0]) in l1:
		l1.remove((i[1],i[0]))

for i in l1:
	print "%s %s" % (i[0],i[1])




