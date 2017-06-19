import sys
import warnings

origem = sys.stdin.readline().split()[0]
dist = int(sys.stdin.readline().split()[0])

adj = {}
l = []


	
for s in sys.stdin:
	o,d = s.split()
	if o not in adj:
		adj[o] = set()
	if d not in adj:
		adj[d] = set()
	adj[o].add(d)
	adj[d].add(o)



def bfs(adj,o): # descobrir o caminho mais curto entre dois pontos
	pais = {}
	visitados = set()
	visitados.add(o)
	q = [] # queue
	q.append(o) # enqueue
	while q:
		c = q.pop(0) # pop(0) retira o elemento da posicao 0
		for n in adj[c]: # c = atual
			if n not in visitados:
				visitados.add(n)
				pais[n] = c # descobrimos n a partir de c
				q.append(n)
	return pais



parents = bfs(adj,origem) # dicionario com todos os pais e filhos correspondentes



#def nivel(parent,origem,dist): # c = dist
#	niveis = []
#	c=1
#	#print dist
#	while(c < dist):
#		for filho in parent:
#			if c < dist and parent[filho] == origem:
#				origem = filho
#				#print x
#				c+=1
#				#print c
#	#print origem
#	for filho in parent:
#		if parent[filho] == origem:
#			niveis.append(filho)
#
#	return niveis

final = []
for filho in parents:
	aux = filho
	nivel = 1
	while(parents[filho] != origem and nivel < dist):
		nivel+=1
		filho = parents[filho]
	if (parents[filho] == origem and nivel == dist):
		final.append(aux)

for x in sorted(final):
	print x


#for pais in sorted(nivel(parents,origem,dist)):
#	print pais
#print parents



#{'suica': 'franca', 
# 'holanda': 'belgica', 
# 'franca': 'espanha', 
# 'polonia': 'alemanha', 
# 'italia': 'suica', 
# 'alemanha': 'franca', 
# 'belgica': 'franca', 
# 'espanha': 'portugal'}




'''
{'portugal': set(['espanha']), 
 'suica': set(['franca', 'italia', 'alemanha']), 
 'holanda': set(['belgica']), 
 'franca': set(['suica', 'alemanha', 'belgica', 'espanha']), 
 'polonia': set(['alemanha']), 
 'italia': set(['suica']), 
 'alemanha': set(['suica', 'franca', 'belgica', 'polonia']), 
 'belgica': set(['holanda', 'franca', 'alemanha']), 
 'espanha': set(['franca', 'portugal'])}
'''












