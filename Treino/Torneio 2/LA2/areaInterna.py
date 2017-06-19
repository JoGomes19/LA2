import sys


##########################
## inicio - ler o input ##
##########################

x,y = sys.stdin.readline().split()
o = (int(x),int(y))
l = []

for s in sys.stdin:
	l.append(s)

def adj(o): # calcula os adjacentes do ponto dado (em forma de +)
	a = set()
	if l[o[1]-1][o[0]] == ' ':
		a.add((o[0],o[1]-1))

	if l[o[1]][o[0]-1] == ' ':
		a.add((o[0]-1,o[1]))

	if l[o[1]][o[0]+1] == ' ':
		a.add((o[0]+1,o[1]))

	if l[o[1]+1][o[0]] == ' ':
		a.add((o[0],o[1]+1))

	return a

#######################
## fim - ler o input ##
#######################


#visitados = adj(o)
#visitados.add(o)
#adjAux = visitados
#x = (2,2)




def dfs(o): # da todos os pontos acessiveis
	visitados = set() #se fosse importante a ordem utilizariamos listas e nao conjuntos
	orla = []
	orla.append(o)
	while orla:
		v = orla.pop()
		if v not in visitados:
			visitados.add(v)
			for w in adj(v): # usa a funcao adj
				orla.append(w)
	return visitados



print adj(o)
#print len(dfs(o))





