import sys
import itertools


s = int(sys.stdin.readline())

l=[]
ll=[]

def is_prime(a):
    return all(a % i for i in xrange(2, a))


def valida(p):
	# print i
	aux = []
	j = 0
	#print len(p)
	while(j < len(p)-1):
		#print j,j+1,'ola2'
		aux.append( (p[j],p[j+1]) )
		j+=1
	#print j,j+1,'ola'
	aux.append((p[j],p[0]))
	#print aux
	for i in aux:
		if not is_prime(i[0]+i[1]):
			return False
	return True


def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                	yield [items[i]]+cc           


def xpermutations(items):
    return xcombinations(items, len(items))


ll = xpermutations(range(1,s+1))
#print list(ll)
#ll = list(itertools.permutations(range(1,s+1)))
#print list(ll)

for p in ll:
	if valida(p):
		print ' '.join(str(x) for x in p)
		exit()









