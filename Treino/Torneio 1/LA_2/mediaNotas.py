import sys

t = 0.0
n = 0
for s in sys.stdin: # le linha a linha (do ficheiro txt)
	l = s.split(",") # por cada linha, cria uma lista em que l[0] e o que antes do caracter "," 
	                 # e l[1] e o que esta depois do caracter ","
	t += float(l[1]) # como e uma lista com 1 elemento fazemos float(l[1])
	n += 1
print ("%.2f" % (t/n)) # "%.2f" % -> significa que t/n vai ter duas casas decimais


