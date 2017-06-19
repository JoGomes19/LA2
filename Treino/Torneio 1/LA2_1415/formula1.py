import sys


dic = {}
l = []
menor = 0

def maisRapido(l):   # funcao que calcula a volta mais rapida de uma lista de tempos
	m = 1000
	for i in range(0,len(l)-1):
		if l[i+1] - l[i] < m:
			m = l[i+1] - l[i]
	return m



for s in sys.stdin: # preenche um dicionario do tipo: (condutor -> lista de tempos(ordenada!))
	l = s.split()
	if l[1] in dic:
		dic[l[1]].append(int(l[0]))
	else:
		dic[l[1]] = [int(l[0])]

novoDic = dict.fromkeys(dic.keys(),[]) # dicionario do tipo: (condutor -> lista vazia)
#print novoDic

for x in dic:
	novoDic[x] = maisRapido(dic[x]) # daqui sai um dicionario do tipo: (condutor -> melhor tempo desse gajo)

#print novoDic
#print('\n')

#x = maisRapido([20, 50, 60, 100])

l = sorted(novoDic.iteritems(), key=lambda (k, v): (v, k))

menor = l[0][1] # como o dicionario esta ordenado, sabemos que o tempo mais baixo
				# e o primeiro, logo imprimimos todos os gajos que fizerem um tempo igual a esse

for i in l:
	if i[1] == menor:
		print i[0]







