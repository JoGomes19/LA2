import sys

resultados=[]
resultados1=[]

for linha in sys.stdin:
	aux=[]
	for x in linha.rstrip().split():
		aux.append(x)
	resultados.append(aux)
	resultados1.append(aux)



res = set()
for item in resultados:
	res.add(item[0])
	for x in resultados:
		if x[0]==item[0] or x[1]==item[0]:
			resultados.remove(x)


lista=[]
lista.append(len(res))

res=set()
for item in resultados1:
	res.add(item[1])
	for x in resultados1:
		if x[0]==item[1] or x[1]==item[1]:
			resultados1.remove(x)

lista.append(len(res))

print l[1]


