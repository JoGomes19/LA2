import sys

s = set() # aqui usamos um set, pois um set nao pode ter elementos repetidos,
          # ou seja set.add ou set.update nunca mete no set elementos que ja la estao

for l in sys.stdin:
	s.update(l.split())

ordenado = sorted(s) # aqui, ordenado e uma lista -> print(type(ordenado)) = List
                     # porque sorted so esta definido para listas

for i in ordenado:
	print i 