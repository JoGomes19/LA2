import sys


dic = {}
somado = {}


for s in sys.stdin:
	l = s.split()
	if l[0] in dic:
		dic[l[0]].append(int(l[1]))
	else:
		dic[l[0]] = [int(l[1])] # daqui sai um dicionario com a lista das notas de cada aluno

for x in dic:
	somado[x] = sum(dic[x]) # somado -> dicionariod o tipo (n aluno -> soma das notas)


for y in sorted(somado.iteritems(), key=lambda (k, v): (-v, k)):
	print "%s %d" % (y[0],y[1])