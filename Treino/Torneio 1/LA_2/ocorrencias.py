import sys

l = [] # aqui usamos um set, pois um set nao pode ter elementos repetidos,
       # ou seja set.add ou set.update nunca mete no set elementos que ja la estao

for s in sys.stdin:
	x = s.split(",")
	l.append(x)

for i in l:
	print(i)