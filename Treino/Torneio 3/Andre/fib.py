import sys

def fib(n):
	if n <= 1:
		return 1
	return fib(n-1)+fib(n-2)

cache = {}  #dicionario para memoization/caching

# fib com memoria 
def mfib(n):
	if n in cache:
		return cache[n]
	if n <= 1:
		cache[n] = 1
		return 1
	cache[n] = mfib(n-1)+mfib(n-2)
	return cache[n]

def pdfib(n):
	cache = {} #reiniciamos a cache mas podiamos reutilizar
	cache[0] = 1
	cache[1] = 1
	for i in range(2,n+1):
		cache[i] = cache[i-1] + cache[i-2]
	return cache[n]

def fpdfib(n):
	cache = {} #reiniciamos a cache mas podiamos reutilizar
	cache_0 = 1
	cache_1 = 1
	for i in range(2,n+1):
		cache_0,cache_1 = cache_1, cache_0+cache_1
	return cache_1

for l in sys.stdin:
	print fpdfib(int(l))
