import sys



l = []
xMin = 0
yMin = 0
xMax = 0
yMax = 0

for s in sys.stdin:
	l.append((s.split()))


#print(l)

if (l != []):
	xMax = l[-1][-2]
	yMax = l[-1][-1]
	M =[[' ' for x in xrange(int(xMax) + 1)] for x in xrange(int(yMax) + 1)] # constroi matriz de dimensao (xMax+1,yMax+1)
	for i in l:
		xMin = i[0]
		yMin = i[1]
		xMax = i[2]
		yMax = i[3]
		for linhas in range(int(yMin),int(yMax)+1):
			for colunas in range(int(xMin),int(xMax)+1):
				M[linhas][colunas] = '#'
				#print(M)
	#print '\n'.join(''.join(str(cell) for cell in row) for row in M)
	salta = 0
	for i in M:
		if (salta == 1):
			print
		for q in i:
			salta = 1
			sys.stdout.write(q)
			#print(q) nao pode ser print(q) pq o print q mete '\n' ao fim 
	print

else: exit()


