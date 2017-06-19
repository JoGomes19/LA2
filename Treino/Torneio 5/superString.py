import sys
from itertools import permutations


def geraTodas(s):
	ola = []
	for i in range(0, len(s)+1):
	    for subset in permutations(s, i):
	           ola.append(subset)
	return ola



def removeSubStrings(str):
   strlen = len(str)
   for size in range (1, strlen // 2):
      for i in range (0, strlen - 2 * size + 1):
            str1 = str[i:i+size]
            str2 = str[i+size:i+2*size]
            while str1 == str2:
               str = str[:i+size] + str[i+2*size:]
               strlen = len(str)
               if i + 2*size > strlen:
                  break
               str2 = str[i+size:i+2*size]
   return str




def juntaElems(l):
	final = ''
	for x in l:
		final+=x
	return final



l=[]
for s in sys.stdin:
	x = s.split()
	l+=x


aux = geraTodas(l)
aux = map(list,aux)
todas = []
for x in aux:
	if (len(x) == len(l)):
		ola = juntaElems(x)
		todas.append(ola)

menor = max(todas)
string = ""
for x in todas:
	y = removeSubStrings(x)
	if (len(y) < menor):
		menor = len(y)
		string = y


print menor







