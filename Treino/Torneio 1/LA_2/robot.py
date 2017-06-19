import sys

# A - avancar na direccao para o qual esta virado
# E - virar-se 90 graus para a esquerda
# D - virar-se 90 graus para a direita
# H - parar


def coordenadas(l):
	y = 0
	x = 0
	maxX = x
	minX = x
	maxY = y
	minY = y
	orientacao = 'C' # cima
	# orientacao serve para sabermos para que lado estamos virados:
	# Cima, Baixo, Esquerda ou Direita


	for c in l:
		if c == 'A':
			if orientacao == 'C':
				y += 1
				if y > maxY:
					maxY = y
				elif y < minY:
					minY = y
			# print("(%d,%d)") % (x,y)
			if orientacao == 'E':
				x -= 1
				if x > maxX:
					maxX = x
				elif x < minX:
					minX = x
			# print("(%d,%d)") % (x,y)
			if orientacao == 'D':
				x += 1
				if x > maxX:
					maxX = x
				elif x < minX:
					minX = x
			# print("(%d,%d)") % (x,y)
			if orientacao == 'B': # baixo
				y -= 1
				if y > maxX:
					maxX = x
				elif y < minY:
					minY = y
			# print("(%d,%d)") % (x,y)
		elif c == 'E':
			if orientacao == 'C':
				orientacao = 'E'
			elif orientacao == 'E':
				orientacao = 'B'
			elif orientacao == 'D':
				orientacao = 'C'
			elif orientacao == 'B':
				orientacao = 'D'
		elif c == 'D':
			if orientacao == 'C':
				orientacao = 'D'
			elif orientacao == 'E':
				orientacao = 'C'
			elif orientacao == 'D':
				orientacao = 'B'
			elif orientacao == 'B':
				orientacao = 'E'
		elif c == 'H':
			print("(%d,%d) (%d,%d)") % (minX,minY,maxX,maxY)
			y = 0
			x = 0
			maxX = x
			minX = x
			maxY = y
			minY = y
			orientacao = 'C'



l = []

for s in sys.stdin:
	x = s.split()
	l += x

coordenadas(l)


