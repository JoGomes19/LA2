import sys # importa a biblioteca stdio

def factoriza(n):
	p = 2
	while p <= n:
		if n%p == 0:
			print p
			n = n/p
		else:
			p += 1

    
s = sys.stdin.readline() # recebe o argumento como string
factoriza(int(s)) # int(s) faz um cast de s para int


		




