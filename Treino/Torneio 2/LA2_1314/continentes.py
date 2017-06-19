import sys


def bfs(adj,o): # devolve o comprimento de um continente
	parent = {}
	discovered = [] 
	q = []
	discovered.append(o)
	q.append(o)
	ordenado = []
	final = []
	while q:
		c = q.pop(0) #tira da posicao 0
		ordenado.append(c)
		if c in adj:
			for n in adj[c]:
				if n not in discovered:
					discovered.append(n)
					parent[n] = c #descobrimos n a partir de c
					q.append(n)
	final.append(sorted(ordenado)[0])
	#print final
	return final



	  
##########################
## inicio - ler o input ##
##########################

adj = {}

adj = dict()
for line in sys.stdin:
    v1, v2 = line.split()
    if not v1 in adj:
        adj[v1] = list()
    adj[v1].append(v2)
    if not v2 in adj:
        adj[v2] = list()
    adj[v2].append(v1)

#######################
## fim - ler o input ##
#######################

#print adj

continentes = []
final = []
if adj:
	for n in adj:
		continentes+=(bfs(adj,n))

continentes = set(continentes)
continentes = list(continentes)



for x in sorted(continentes):
	print x



