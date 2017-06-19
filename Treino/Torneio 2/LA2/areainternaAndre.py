import sys

def dfs(adj,o):
	s=[]
	discovered = set() #se precisassemos de saber a ordem tinha de ser uma lista
	s.append(o)
	while s:
		v = s.pop()
		if v not in discovered:
			discovered.add(v)
			for w in adj[v]:
				s.append(w)
	return discovered

x,y = sys.stdin.readline().split()
origem = (int(x),int(y))
lista = []

for s in sys.stdin:
	lista.append(s)
print lista 

adj= {}
adj[origem] = []

if lista[origem[1]-1][origem[0]] == ' ':
		adj[origem].append((origem[0],origem[1]-1))
if lista[origem[1]][origem[0]-1] == ' ':
		adj[origem].append((origem[0]-1,origem[1]))
if lista[origem[1]][origem[0]+1] == ' ':
		adj[origem].append((origem[0]+1,origem[1]))
if lista[origem[1]+1][origem[0]] == ' ':
		adj[origem].append((origem[0],origem[1]+1))


#print adj
#print dfs(adj,origem)
#print parent 
#print
#print dfs(adj,origem)








