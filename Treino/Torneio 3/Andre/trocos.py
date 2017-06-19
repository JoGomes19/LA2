import sys


def pdtroca(v):
	cache = {}
	cache[0] = 0
	for i in range(1,v+1):
		r = float("inf") # calcular o minimo de todas as hip.
		for m in moedas:
			if i >= m:
				r = min(r,cache[i-m])
		cache[i] = r+1
	return cache[v]




valor = int(sys.stdin.readline())

moedas = []
for l in sys.stdin:
	moedas.append(int(l))

print pdtroca(valor)


