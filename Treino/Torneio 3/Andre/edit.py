import sys

def distance(p,q):
	if p =="":
		return len(q)
	if q =="":
		return len(p)
	if q[-1] == p[-1]:
		return distance(p[:-1],q[:-1])
	r = float("inf")
	r = min(r,distance(p[:-1],q[:-1]))
	r = min(r,distance(p[:-1],q))
	r = min(r,distance(p,q[:-1]))
	return r +1

cache = {}
def mdistance(p,q):
	if (p,q) in cache:
		return cache[(p,q)]
	if p =="":
		cache[(p,q)] = len(q)
		return cache[(p,q)]
	if q =="":
		cache[(p,q)] = len(p)
		return cache[(p,q)]
	if q[-1] == p[-1]:
		cache[(p,q)] = mdistance(p[:-1],q[:-1])
		return cache[(p,q)]
	r = float("inf")
	r = min(r,mdistance(p[:-1],q[:-1]))
	r = min(r,mdistance(p[:-1],q))
	r = min(r,mdistance(p,q[:-1]))
	cache[(p,q)] = r+1
	return r +1

cache = {}
def imdistance(p,q,lp,lq):
	if (lp,lq) in cache:  #vemos se ja consideramos os prefixos com este tamanho 
		return cache[(lp,lq)]
	if lp ==0:
		cache[(lp,lq)] = lq
		return lq
	if lq ==0:
		cache[(lp,lq)] = lp
		return lp
	if q[lq-1] == p[lp-1]:
		cache[(lp,lq)] = imdistance(p,q,lp-1,lq-1)
		return cache[(lp,lq)]
	r = float("inf")
	r = min(r,imdistance(p,q,lp-1,lq-1))
	r = min(r,imdistance(p,q,lp-1,lq))
	r = min(r,imdistance(p,q,lp,lq-1))
	cache[(lp,lq)] = r+1
	return r +1

def pddistance(p,q,lp,lq):
	cache = {}
	for i in range(lp+1):
		cache[(i,0)] = i
	for j in range(lq+1):
		cache[(0,j)] = j
	for i in range(1,lp+1):
		for j in range(1,lq+1):
			if p[i-1] == q[j-1]:
				cache[(i,j)] = cache[(i-1,j-1)]
			else:
				r = float("inf")
				r = min(r,cache[(i-1,j-1)])
				r = min(r,cache[(i,j-1)])
				r = min(r,cache[(i-1,j)])
				cache[(i,j)] = r+1
	return cache[(lp,lq)]







p = sys.stdin.readline().rstrip()
q = sys.stdin.readline().rstrip()

print pddistance(p,q,len(p),len(q))