import sys

i = 0
nomes={}
for s in sys.stdin:
	x = s.split()
	nomes[i] = []
	for j in x:
		nomes[i].append(j)
	i+=1

x = sorted(nomes.items(), key=lambda x: (len(x[1]),x[1])) # adiciona espacos nos nomes do meio
for i in range(len(x)):
	for j in range(len(x[i][1])-1):
		x[i][1][j]+=' '

l = len(x)
for y in x:
	xx = y[1]
	for i in range(len(xx)):
		sys.stdout.write(xx[i])
	print

	
	
	
	
	
	
	
