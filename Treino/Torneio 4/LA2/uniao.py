import sys 


conjuntos = []
l = []


for s in sys.stdin:
	x = s.split()
	l.append(x)


for x in l:
	z = set(map(int,x))
	conjuntos.append(z)
	


universo = set().union(*conjuntos)



def valida(s):
	l = []
	for x in s:
		l.append(conjuntos[x])

	if set().union(*l) != universo:
		return False
	return True


def procura(sol,k): #tamanho que quero obter
	if len(sol) == k:
		return valida(sol)

	for x in xrange(len(conjuntos)):
		sol.append(x)
		if procura(sol,k):
			#print sol
			return True
		sol.pop(-1)
	return False



solucao = []

for x in range(len(universo)):
	if procura(solucao,x):
		print x
		exit()



