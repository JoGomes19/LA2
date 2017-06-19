import sys

def  imprimeMelhor(l):
	for i in l:
		print i
		for x in i[1:]:
			print x
			r = float("inf")
    		u = int(x[0])
    		m=0
    		for x in i[1:]:
      			# print x
      			print r
      			print u
      			# m=x-u
      			# u= x
      			# r = min (r,m)
     			


dic={}
for i in sys.stdin:
	(at,b)=i.split()
	a = int (at)
	if b in dic:
		dic[b]=dic[b]+[a]
	else:dic[b]=[a]

l=[]
#for k in dic:
#	imprimeMelhor(k)
print dic
# 
