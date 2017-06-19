import sys

l = []

for s in sys.stdin:
	x = s.split(",")
	l.append(x)

l = [[int(float(j)) for j in i] for i in l] # converte uma lista de listas de string para lita de lista de ints
l.sort(key = lambda x: float(x[1])) # ordena uma lista de listas em relacao a chave!

for i in l:
	print(i)