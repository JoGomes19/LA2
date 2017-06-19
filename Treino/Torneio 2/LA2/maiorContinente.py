import sys


def breathFirst(adj,o): # devolve o comprimento de um continente
	parent = {}
	discovered = [] 
	q = []
	discovered.append(o)
	q.append(o)
	final = []
	while q:
		c = q.pop(0) #tira da posicao 0
		if c in adj:
			for n in adj[c]:
				if n not in discovered:
					discovered.append(n)
					parent[n] = c #descobrimos n a partir de c
					q.append(n)
	#print parent
	for n in parent:
		#print n
		final.append(n)
	final.append(parent[n]) #lista dos paises que fazem parte do mesmo continente que o origem
	#print final
	return len(set(final))


	  
##########################
## inicio - ler o input ##
##########################

adj = {}
l = []
for s in sys.stdin:
	x = s.split()
	l.append(x)
for x in l:
	for i in range(1,len(x)):
		if (x[0] in adj):
			if (x[i] not in adj[x[0]]):
				adj[x[0]] += [x[i]]
		else:
			adj[x[0]] = [x[i]]

#######################
## fim - ler o input ##
#######################

#adj = {'colombia': ['equador', 'peru'], 'franca': ['belgica', 'alemanha', 'suica', 'italia'], 'espanha': ['franca'], 'brasil': ['uruguai', 'paraguai', 'peru', 'colombia', 'venezuela'], 'portugal': ['espanha'], 'suica': ['austria', 'italia'], 'belgica': ['holanda', 'alemanha'], 'inglaterra': ['irelanda'], 'alemanha': ['polonia']}
#print adj
continentes = [] #lista com todos os comprimentos encontrados na funcao breathFirst
if adj:
	for n in adj:
		continentes.append(breathFirst(adj,n))
else: print(0)

print max(continentes)

