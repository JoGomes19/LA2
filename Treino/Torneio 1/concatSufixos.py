import sys
import itertools

def junta(s1,s2):
	for i in range(0,len(s1)):
		if (s1[i] == s2[0]):
			del s2[0]
	s1 += s2

	return ''.join(s1)


l = []

for s in sys.stdin:
	x = s.split()
	l += x

l = map(list,l)

#print l
l1 = []
for i in range(0,len(l)-1):
	l1.append((l[i],l[i+1]))
#print l1

l2 = []
for i in l1:
	#print i
	l2.append(junta(i[0],i[1]))
	



print junta(l[0],l[1])



#[(['c', 'a', 'n', 't', 'a', 'r'], ['t', 'a', 'r', 't', 'e']),
# (['t', 'a', 'r', 't', 'e'], ['t', 'e', 'm', 'p', 'o']),
# (['t', 'e', 'm', 'p', 'o'], ['p', 'o', 't', 'e', 'n', 't', 'e'])]


