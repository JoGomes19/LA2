from __future__ import generators
import sys

resultados=[]
#ref_arquivo = open("H_SuperStrings.txt","r")
for linha in sys.stdin:
	for x in linha.rstrip().split():
		resultados.append(x)
#ref_arquivo.close()
#print resultados

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc
                #print items


def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc
            
def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss

def xpermutations(items):
    return xcombinations(items, len(items))

res=[]

for p in xpermutations(resultados): 
	res.append(''.join(p))

for i in range(len(resultados)):
	for uc in xcombinations(resultados,i): 
		x=''.join(uc)
		res.append(x)

from itertools import groupby

def my_function(s, c):
    return ''.join(c if a==c else ''.join(b) for a,b in groupby(s))
minimo = 0
for item in resultados:
	minimo+=len(item)

#print minimo

for item in res:
	falha = 0
	for x in resultados:
		if x not in item:
			falha = 1
	if falha == 0:
		if len(item)<minimo:
			minimo = len(item)
print minimo


