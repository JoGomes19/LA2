import sys

m = 0.0

for s in sys.stdin:
	l = s.split(",") # por cada linha, cria uma lista em que l[0] e o que antes do caracter "," 
	                 # e l[1] e o que esta depois do caracter ","
	n = float(l[1])
	if n > m:
		m = n
		a = l[0] # numero do aluno a que corresponde a melhor nota ate ao momento
print(a)
