import sys




def iniciais(l):
	lis = []
	for i in l:
		# if (i[0] != i[-1]): nao precisa desta condicao,
		# pois basta ter esta condicao na funcao finais ou nesta.
		# escolhi ter na funcao finais
		lis += i[0]
		#print(i[0])
	return lis
	#for j in lis:
	#	print(j)

def finais(l):
	lfi = []
	for i in l:
		if (i[0] != i[-1]):
			lfi += i[-1]
		#print(i[-1])
	return lfi
	#for j in lfi:
	#	print(j)

def ocorrencias(l):
	l1 = []
	for i in range(0,len(l)):
		l1 += [(l[i],l.count(l[i]))]
	return l1


l = []
final = []
cruzamento = []
criticidade = []

for s in sys.stdin:
	x = s.split()
	l += x

infin = iniciais(l) + finais(l)

lpares = ocorrencias(infin)

final = sorted(set(lpares), key = lambda x: (x[1], x[0])) # ordena em relacao aos dois elementos de cada par,
                                                          # dando prioridade ao primeiro

cruzamento = [x[0] for x in final] # lista cruzamento que pega no primeiro elemento de cada par da lista final
criticidade = [x[1] for x in final] # lista criticidade que pega no segundo elemento de cada par da lista final

for i in range(0,len(final)):
	print(cruzamento[i] + " " + str(criticidade[i]))









