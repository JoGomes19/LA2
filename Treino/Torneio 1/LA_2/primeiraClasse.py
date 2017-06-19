import sys

l = []

for s in sys.stdin:
	x = s.split()
	l += (map(int,x))
	
soma = 0
for i in l:
	soma += i

print soma
