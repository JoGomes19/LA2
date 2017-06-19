import sys

x,y = sys.stdin.readline().split()

dimX = int(x)
dimY = int(y)


nTorres = sys.stdin.readline()

torres = []

for s in sys.stdin:
	x,y,alc = s.split()
	torres+=[(int(x),int(y),int(alc))]

def alcanceMin((x,y,r)):
	return (x-r,y-r)

def alcanceMax((x,y,r)):
	return (x+r,y+r)

def areaVigia((xMin,yMin),(xMax,yMax)):
	area = set([(xMin,yMin),(xMax,yMax)])
	for x in range(xMin,xMax):
		for y in range(yMin,yMax):
			area.add((x+1,y))
			area.add((x,y+1))
	return area

def areaTotal(dicTorres):
	mapa = set()
	menorUniao = len(dicTorres)
	visitados = []
	for x in dicTorres:
		aux = dicTorres.pop(x)
		aux1 = aux
		for y in dicTorres:
			aux1 = aux1.union(dicTorres[y])
			print aux1
			visitados+=[y]
			#print y
			if(aux1 == mundo):
				if len(visitados) < menorUniao:
					menorUniao = len(visitados)
					print 'E este',len(aux1)
					#print visitados
				break
		dicTorres[x]=aux
		visitados = []
	return menorUniao






mundo = areaVigia((0,0),(dimX-1,dimY-1))



dicTorres = {}
for torre in torres:
	aMin = alcanceMin(torre)
	aMax = alcanceMax(torre)
	aTorre = areaVigia(aMin,aMax)
	dicTorres[(torre[0],torre[1])] = aTorre


print areaTotal(dicTorres)

