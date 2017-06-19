import sys
try:
    xrange
except:
    xrange = range
 
 
peso_maximo = int(sys.stdin.readline().rstrip())



items = []
for l in sys.stdin:
    items.append(int(l))
    #print a
    #  groupeditems.append((a[0],int(a[2]),int(a[1]),250))
#print items

class Bin(object):
    """ Container for items that keeps a running sum """
    def __init__(self):
        self.items = []
        self.sum = 0

    def append(self, item):
        self.items.append(item)
        self.sum += item

    def __str__(self):
        """ Printable representation """
        return 'Bin(sum=%d, items=%s)' % (self.sum, str(self.items))


def pack(values, maxValue):
    values = sorted(values, reverse=True)
    bins = []

    for item in values:
        # Try to fit item into a bin
        for bin in bins:
            if bin.sum + item <= maxValue:
                #print 'Adding', item, 'to', bin
                bin.append(item)
                break
        else:
            # item didn't fit into any bin, start a new bin
            #print 'Making new bin for', item
            bin = Bin()
            bin.append(item)
            bins.append(bin)

    return bins


print len(pack(items,peso_maximo))
