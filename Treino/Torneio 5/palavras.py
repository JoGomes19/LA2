import sys

l=[]
for s in sys.stdin:
	x = s.split()
	l+=x


def dup(s):
	if (s[0] == s[-1]):
		
		for i in range(1,len(s)):
			s+=s[i]
	else:
		for x in s:
			s+=x
	return s


for x in l:
	print dup(x)

