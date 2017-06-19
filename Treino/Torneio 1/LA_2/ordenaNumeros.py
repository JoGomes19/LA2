import sys

def getChave(l):
	return l[0]


l = []

for s in sys.stdin:
	x = s.split(",")
	l.append(x)

l = [[int(float(j)) for j in i] for i in l] # converte uma lista de listas de string para lita de lista de ints
l.sort(key = getChave) # ordena uma lista de listas em relacao a chave!

for i in l:
	print(i)

