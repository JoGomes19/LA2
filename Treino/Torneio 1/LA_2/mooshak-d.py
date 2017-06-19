import sys



def letsGo(l):
	y=0
	x=0
	orientacao='cima'
	#coord=[((x,y),orientacao)]
	MaxX=x
	MaxY=y
	MinX=x
	MinY=y

	for c in l:
		if c == 'D':
			if orientacao == 'cima':
				orientacao = 'dir'
			elif orientacao == 'dir':
				orientacao = 'baixo'
			elif orientacao == 'baixo':
				orientacao = 'esq'
			elif orientacao == 'esq':
				orientacao = 'cima'
		elif c == 'E':
			if orientacao == 'cima':
				orientacao = 'esq'
			elif orientacao == 'esq':
				orientacao = 'baixo'
			elif orientacao == 'baixo':
				orientacao = 'dir'
			elif orientacao == 'dir':
				orientacao = 'cima'
		elif c == 'A':
			if orientacao == 'cima':
				x+=1
				if x>MaxX:
					MaxX=x
			elif orientacao == 'dir':
				y+=1
				if y>MaxY:
					MaxY=y
			elif orientacao == 'baixo':
				x-=1
				if x < MinX:
					MinX = x
			elif orientacao == 'esq':
				y-=y
				if y<MinY:
					MinY = y
		elif c == 'H':
			#print ("(%d,%d) (%d,%d)") % (MinX,MinY,MaxX,MaxY)
			print(" (%s , %s) (%s , %s) ") % (MinX,MinY,MaxX,MaxY)
			# y=0
			# x=0
			# orientacao='cima'
			# coord=[((x,y),orientacao)]
			# MaxX=x
			# MaxY=y
			# MinX=x
			# MinY=y



l=[]

for s in sys.stdin:
	x = s.split()
	l += x

#print l

letsGo(l)
