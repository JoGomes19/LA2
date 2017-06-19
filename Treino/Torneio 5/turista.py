import sys

l = []
for s in sys.stdin:
	x = s.split()
	l+=x


if l == []:
	print 0
	exit()

def procura(l,id):
	visitados=[]

	dias = 0
	while(id < len(l)-1):
		if l[id] not in visitados:
			visitados.append(l[id])
			dias+=1
			id+=1
			#if l[id] in visitados:
				#print 'ola'
		if l[id] in visitados:
			break
	if l[id] not in visitados:
		visitados.append(l[id])
		dias+=1

	return len(visitados),visitados

maior = 0

id = 0

while(id < len(l)):
	dias,indice = procura(l,id)
	if(dias > maior):
		maior = dias
	id = indice


print maior




