import sys

rect=[]
maiorx=0
maiory=0
for l in sys.stdin:
	(x,y,w,z)=l.split()
	(x,y,w,z)=(int(x),int(y),int(w),int(z))
	rect.append((x,y,w,z))
	if (x>maiorx):
		maiorx=x
	if (w>maiorx):
		maiorx=w
	if (y>maiory):
		maiory=y
	if (z>maiory):
		maiory=z

M =[[' ' for x in xrange(maiorx+1)] for x in xrange(maiory+1)]


xinicial=0
yinicial=0
xfinal=0
yfinal=0
for s in rect:
	xinicial=s[0]
	yinicial=s[1]
	xfinal=s[2]
	yfinal=s[3]
	for linhas in range(yinicial,yfinal+1):
		for colunas in range(xinicial,xfinal+1):
			M[linhas][colunas]='#'

salta=0
for i in M:
	if (salta==1):
		print
	for q in i:
		salta=1
		sys.stdout.write(q)
print(1)

