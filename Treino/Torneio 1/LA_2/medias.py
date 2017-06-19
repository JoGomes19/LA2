import sys

t = 0.0
n = 0
for s in sys.stdin: # le linha a linha (do ficheiro txt)
	t += float(s) # soma cada string de cada linha (depois de tansformar para float)
	n += 1
print ("%.2f" % (t/n)) # "%.2f" % -> significa que t/n vai ter duas casas decimais



