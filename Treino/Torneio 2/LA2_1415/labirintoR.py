import sys




inf = float('inf')
# decobrir o caminho mais curto entre (0,0) (n-1,n-1)


##########################
## inicio - ler o input ##
##########################

n = map(int,sys.stdin.readline().split())[0]


destinos = []
l = []
adj={}

for s in sys.stdin:
	l.append(s)

############
## Origem ##
############

for x in l:
	for i in x:
		if i == 'R':
			origem = (l.index(x),x.index(i))

############
############
############


for x in range(int(n)):
	for y in range(int(n)):
		if l[x][y] == ' ' or l[x][y] == 'R': # aqui insere a posicao inicial tambem
			adj[(x,y)] = set()



			
for (x,y) in adj:
	if (x-1,y) in adj and l[x-1][y] == ' ':
		adj[(x,y)].add((x-1,y))
		adj[(x-1,y)].add((x,y))
	if (x+1,y) in adj and l[x+1][y] == ' ':
		adj[(x,y)].add((x+1,y))
		adj[(x+1,y)].add((x,y))
	if (x,y+1) in adj and l[x][y+1] == ' ':
		adj[(x,y)].add((x,y+1))
		adj[(x,y+1)].add((x,y))
	if(x,y-1) in adj and l[x][y-1] == ' ':
		adj[(x,y)].add((x,y-1))
		adj[(x,y-1)].add((x,y))

#print adj
#######################
## fim - ler o input ##
#######################



def bfs(adj,o): # descobrir o caminho mais curto entre dois pontos
	pais = {}
	final = []
	visitados = set()
	visitados.add(o)
	q = [] # queue
	q.append(o) # enqueue
	while q:
		c = q.pop(0) # pop(0) retira o elemento da posicao 0
		#print c
		final.append(c)
		for n in adj[c]: # c = atual
			if n not in visitados:
				visitados.add(n)
				pais[n] = c # descobrimos n a partir de c
				q.append(n)
		#final.append(c)
	return final,pais


ces = bfs(adj,origem) # dicionario com todos os pais e filhos correspondentes(so os que sao == ' ')


#print parent

####################
## Lista Destinos ##
####################


for x in range(n-1):
	if l[0][x] == ' ' or l[0][x] == 'R':
		destinos.append((0,x))
	if l[x][0] == ' ' or l[x][0] == 'R':
		destinos.append((x,0))
	if l[n-1][x] == ' ' or l[n-1][x] == 'R':
		destinos.append((n-1,x))
	if l[x][n-1] == ' ' or l[x][n-1] == 'R':
		destinos.append((x,n-1))

####################
####################
####################




for primeiro in ces[0]:
	if primeiro in destinos:
		break

#print type(ces[1])
path=[]
path.append(primeiro) #inicializamos o caminho com o destino

while primeiro in ces[1]:
	primeiro = ces[1][primeiro]
	path.insert(0,primeiro)

print len(path)-1





'''
{(1, 3): set([(2, 3)]), 
(5, 6): set([(5, 7), (5, 5)]), 
(2, 8): set([(3, 8), (1, 8)]), 
(9, 8): set([(8, 8)]), 
(2, 1): set([(3, 1), (1, 1)]), 
(6, 2): set([(6, 3), (6, 1)]), 
(1, 6): set([(1, 5), (1, 7)]), 
(3, 7): set([(3, 8), (3, 6)]), 
(5, 1): set([(6, 1), (4, 1)]), 
(8, 5): set([(8, 6), (7, 5), (8, 4)]), 
(5, 8): set([(5, 7), (6, 8)]), 
(6, 7): set([(5, 7), (6, 8)]), 
(3, 3): set([(3, 4), (2, 3), (4, 3)]), 
(8, 1): set([(8, 2)]), 
(6, 3): set([(6, 2), (5, 3)]), 
(1, 5): set([(1, 6)]), 
(3, 6): set([(3, 7), (3, 5)]), 
(5, 7): set([(5, 6), (6, 7), (5, 8)]), 
(8, 6): set([(8, 5), (8, 7)]), 
(3, 5): set([(4, 5), (3, 4), (3, 6)]), 
(4, 1): set([(5, 1), (3, 1)]), 
(1, 1): set([(0, 1), (2, 1)]), 
(8, 2): set([(8, 1), (8, 3)]), 
(4, 5): set([(5, 5), (3, 5)]), 
(5, 5): set([(5, 6), (4, 5), (6, 5)]), 
(7, 5): set([(8, 5), (6, 5)]), 
(2, 3): set([(1, 3), (3, 3)]), 
(8, 7): set([(8, 6), (8, 8)]), 
(6, 5): set([(7, 5), (5, 5)]), 
(5, 3): set([(6, 3), (4, 3)]), 
(0, 1): set([(1, 1)]), 
(8, 3): set([(8, 2), (8, 4)]), 
(6, 8): set([(6, 7), (5, 8)]), 
(6, 1): set([(5, 1), (6, 2)]), 
(3, 1): set([(4, 1), (2, 1)]), 
(3, 8): set([(2, 8), (3, 7)]), 
(1, 8): set([(2, 8), (1, 7)]), 
(8, 8): set([(9, 8), (8, 7)]), 
(4, 3): set([(3, 3), (5, 3)]), 
(1, 7): set([(1, 8), (1, 6)]), 
(3, 4): set([(3, 3), (3, 5)]), 
(8, 4): set([(8, 3), (8, 5)])}
'''


