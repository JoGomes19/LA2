import sys
import json
from collections import Counter, OrderedDict


s = sys.stdin.readlines()
words = [word for line in s for word in line.split()]
cnt = Counter(words)
lis = sorted(cnt.items(), key=lambda tup: (-tup[1], tup[0]))

for aTuple in lis:
        print( '%s: %s' % aTuple)

        #for aTuple in gradebook:
        #print('Class: %s.....Subject: %s.....Term: %s.....Grade: %s' % aTuple)