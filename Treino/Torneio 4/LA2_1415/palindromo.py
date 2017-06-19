import sys
import itertools


l = []

for s in sys.stdin:
	x = s.split()
	l += x

l = l[0]



def valida(s):
	if s[-1::-1] == s:
		return True
	return False



def permutate_all_substrings(text):
  permutations = []
  # All possible substring lengths
  for length in range(1, len(text)+1):
    # All permutations of a given length
    for permutation in itertools.permutations(text, length):
      # itertools.permutations returns a tuple, so join it back into a string
      permutations.append("".join(permutation))
  return permutations

final = list(set(permutate_all_substrings(l)))


c = 0


for x in final:
	if valida(x):
		c+=1
print c













