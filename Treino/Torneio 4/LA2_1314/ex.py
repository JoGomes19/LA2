# a generator that yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num
        print num
        num += 1

print list(firstn(100))
