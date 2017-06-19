import sys
from itertools import groupby

if not(sys.stdin.readlines()):
    sys.exit();

sys.stdin.seek(0)

peso_maximo = int(sys.stdin.readline().rstrip())



groupeditems = []
for l in sys.stdin:
    a=l.split()
    groupeditems.append((a[0],int(a[2]),int(a[1]),250))
#print groupeditems

try:
    xrange
except:
    xrange = range
 #ola

items = sum( ([(item, wt, val)]*n for item, wt, val,n in groupeditems), [])
 
def knapsack01_dp(items, limit):
    table = [[0 for w in range(limit + 1)] for j in xrange(len(items) + 1)]
 
    for j in xrange(1, len(items) + 1):
        item, wt, val = items[j-1]
        for w in xrange(1, limit + 1):
            if wt > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w],
                                  table[j-1][w-wt] + val)
 
    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j-1][w]
 
        if was_added:
            item, wt, val = items[j-1]
            result.append(items[j-1])
            w -= wt
 
    return result
 
print items
bagged = knapsack01_dp(items, peso_maximo)

print sum(item[2] for item in bagged)
for item in sorted(bagged):
    print item[0]

'''
print("Bagged the following %i items\n  " % len(bagged) +
      '\n  '.join('%i off: %s' % (len(list(grp)), item[0])
                  for item,grp in groupby(sorted(bagged))))
print("for a total value of %i and a total weight of %i" % (
    sum(item[2] for item in bagged), sum(item[1] for item in bagged)))
'''
