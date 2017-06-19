import sys
from itertools import permutations

w = sys.stdin.readline()

#l = sorted(list(set([''.join(p) for p in permutations(w)])))

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)-n+1):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc

l = sorted(set(xuniqueCombinations(w,len(w))))

if len(l) == 0:
	exit()

else:
	if w == l[-1]:
		print l[0]
		exit()
	else:
		for i in range(len(l)):
			if l[i] == w and i < len(l):
				print l[i+1]
				exit()