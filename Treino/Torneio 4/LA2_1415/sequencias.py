import sys
import itertools

n = int(sys.stdin.readline())

l = []

for s in sys.stdin:
	x = s.split()
	l.append(map(int,x))

# = list(itertools.permutations([1,2,3]))


def sublists(input, depth):
      output= []
      if depth > 0:
          for i in range(0, len(input)):
              sub= input[0:i] + input[i+1:]
              output += [sub]
              output.extend(sublists(sub, depth-1))
      return output

def valida(l):
	if sum(l) == n:
		return True


def procura(l,n):
	final = []
	i = 0
	for x in l:
		temp = sublists(x,len(x))
		for t in temp:
			if valida(t) and (t,i) not in final:
				final.append((t,i))
		i+=1
	return final

#print procura(l,n)
final = []
for x in procura(l,n):
	final.append(l[x[1]])

for x in final:
	x = map(str,x)
	print ' '.join(x)




