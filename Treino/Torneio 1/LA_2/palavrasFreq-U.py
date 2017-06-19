import sys



def ocorrencias(l):
	l1 = []
	for i in range(0,len(l)):
		l1 += [(l[i],l.count(l[i]))]
	return l1


l = []
l2 = []
palavra = []
ocorrencia = []

for s in sys.stdin:
	x = s.split()
	l = l+x

# ocorrencias(l) = [('ola', 2),('mundo', 3),('esta', 2),('tudo', 2),('fixe', 2),('mundo', 3),('mundo', 3),('esta', 2),('fixe', 2),('ola', 2),('tudo', 2)]
l2 = sorted(list(set(ocorrencias(l))), key=lambda tup: (-tup[1], tup[0])) # ordena em relacao aos dois elementos do
                                                                          # tuplo, mas a prioridade e o primeiro

# print(l2)
palavra = [x[0] for x in l2]
ocorrencia = [x[1] for x in l2]

for i in range(0,len(l2)):
	print(palavra[i] + ": " + str(ocorrencia[i]))




