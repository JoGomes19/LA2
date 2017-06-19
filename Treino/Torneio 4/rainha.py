import sys

n = int(sys.stdin.readline()) # dimensao do tabuleiro e numero de rainhas

# duas rainhas estao dentro do alcance uma da outr se:
# estao na mesma linha                                -> x0 == x1
# estao na mesma coluna                               -> y0 == y1
# estao na mesma diagonal(inclinada apara a direita)  -> x0+y0 == x1+y1
# estao na mesma diagonal(inclinada apara a esquerda) -> x0-y0 == x1-y1

def valida(pos):
	for i in range(n):
		for j in range(n):
			if i == j:
				continue
			(x0,y0) = pos[i]
			(x1,y1) = pos[j]
			if x0 == x1 or y0 == y1 or x0+y0 == x1+y1 or x0-y0 == x1-y1:
				return False
	return True



def procura(pos,k):
	if k == n:
		return True

	for x in range(n):
			y = k
			ok = True
			for (x1,y1) in pos:
				if x == x1 or x+y == x1+y1 or x-y == x1-y1:
					ok = False
					break
			if not ok:
				continue

			pos.append((x,y))
			if procura(pos,k+1):
				return True
			pos.pop(-1)
	return False





pos = []
print procura(pos,0)



print pos
