import sys


dic = {}
l1 = []

def junta(s1,s2):
	if(s1 == ""):
		return s2
	aux = []
	final = ""
	for x in s1:
		aux.append(x)
	#print aux
	for i in range(len(aux)):
		if (aux[i] == '*' and s2[i] != '*'):
			aux[i] = s2[i]
		if(seguidos(s1) < seguidos(s2) and i < seguidos(s2)):
			aux[i] = s2[i]

	for x in aux:
		final+=x
	s1 = final
	return s1


def juntaTodos(l,s):
	for i in range(len(l)):
		s = junta(s,l[i])
	return s

	
def seguidos(s):
	c=0
	anterior = s[0]
	for x in s[1:]:
		if(x == anterior and x== '*'):
			return c
		anterior=x
		c+=1

for s in sys.stdin:
	l = s.split()
	#print l 
	if l[1] in dic:
		dic[l[1]] += [l[0]]
	else:
		dic[l[1]] = [l[0]]
	l1.append([l[0]])


for x in dic:
	s = juntaTodos(dic[x],"")
	print s,x






