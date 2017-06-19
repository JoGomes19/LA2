import sys
import itertools



ndigitos=int(sys.stdin.readline().rstrip())
valor=int(sys.stdin.readline().rstrip())

print "ndigitos -> ",ndigitos
print "valor -> ",valor

a=range(1,ndigitos+1)
#print "a -> ",a

digits = [int(x) for x in (a)]
#print "digits -> ",digits

n_digits = len(digits)
#print "n_digits -> ",n_digits

n_power = n_digits - 1
#print "n_power -> ",n_power

permutations = itertools.permutations(digits)
#print "permutations -> ",list(permutations)

result = [sum(v * (10**(n_power - i)) for i, v in enumerate(item)) for item in permutations]
#print "result -> ",result

cont=0
for item in result:
	if item%valor == 0:
		cont+=1

print cont