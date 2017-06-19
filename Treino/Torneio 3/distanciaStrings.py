import sys

def muda(s1,s2):
	c=0
	aux = []
	if len(s1) > len(s2):
		for i in xrange(0,len(s1)):
			if s1[i] != s2[i]:
				c+=1
				s1[i] = s2[i]
	return s1,c





l = []
for s in sys.stdin:
	x = s.split()
	print x
print l
#print muda(l[0],l[1])

