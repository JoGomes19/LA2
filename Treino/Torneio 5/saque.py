import sys


n = int(sys.stdin.readline().split()[0])

origem = (0,0)
destino = (n-1,n-1)


l = []
adj={}

for s in sys.stdin:
	l.append(s)

brindes =[]

for i in range(len(l)):
	for j in range(len(l[i])):
		if(l[i][j] in ['1','2','3','4','5','6','7','8','9']):
			brindes.append((i,j,int(l[i][j])))
#print brindes




for x in range(int(n)):
	for y in range(int(n)):
		if l[x][y] != '#':
			adj[(x,y)] = set()


			
for (x,y) in adj:
	if (x+1,y) in adj and l[x+1][y] != '#':
		if l[x+1][y] == '.' and l[x][y] == '.':
			adj[(x,y)].add((x+1,y,0))
			adj[(x+1,y)].add((x,y,0))

		if l[x+1][y] != '.' and l[x][y] != '.':
			adj[(x,y)].add((x+1,y,int(l[x+1][y])))
			adj[(x+1,y)].add((x,y,int(l[x+1][y])))

		if l[x+1][y] != '.' and l[x][y] == '.':
			adj[(x,y)].add((x+1,y,int(l[x+1][y])))
			adj[(x+1,y)].add((x,y,0))

		if l[x+1][y] == '.' and l[x][y] != '.':
			adj[(x,y)].add((x+1,y,0))
			adj[(x+1,y)].add((x,y,int(l[x][y])))

	if(x,y-1) in adj and l[x][y-1] != '#':

		if l[x][y-1] == '.' and l[x][y] == '.':
			adj[(x,y)].add((x,y-1,0))
			adj[(x,y-1)].add((x,y,0))

		if l[x][y-1] != '.' and l[x][y] != '.':
			adj[(x,y)].add((x,y-1,int(l[x][y-1])))
			adj[(x,y-1)].add((x,y,int(l[x][y])))

		if l[x][y-1] != '.' and l[x][y] == '.':
			adj[(x,y)].add((x,y-1,int(l[x][y-1])))
			adj[(x,y-1)].add((x,y,0))

		if l[x][y-1] == '.' and l[x][y] != '.':
			adj[(x,y)].add((x,y-1,0))
			adj[(x,y-1)].add((x,y,int(l[x][y])))


#######################
## fim - ler o input ##
#######################


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


print bfs(adj,origem)



