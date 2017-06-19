import sys,itertools


N = int(sys.stdin.readline())

D = int(sys.stdin.readline())

if N==0: 
	print 0
	exit()

conta=0

for x in itertools.permutations(range(1,N+1),N):
	i =int(''.join(map(str,x)))
	if i%D==0:
		conta+=1



print(conta)