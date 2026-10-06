from inspect import getgeneratorstate

narxlar = [1000, 2000, 3000, 4000, 5000]

it = iter(narxlar)
print(type(it).__name__)

while True:
    try:
        n=next(it)
    except StopIteration:
        break
    print(n ,end=" ")
print()

print(iter(narxlar) is iter(narxlar))
print(iter(it) is it)


class Snagich :
    
    def __init__(self,n):
        self.i=0
        self.n=n
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i>=self.n:
            raise StopIteration
        self.i+=1
        return self.i
    
def sanagich(n):
    i=0
    while i<n:
         i+=1
         yield i
print(sanagich(3))
# print(list(sanagich(3)),list(sanagich(3)))
from collections.abc import Iterable, Iterator

def manba(xs: Iterable[int]) -> Iterator[int]:
    for x in xs:
        print("manba:", x)
        yield x

def kvadratlar(it: Iterable[int]) -> Iterator[int]:
    for x in it:                 # indeks yo'q, len yo'q
        y = x ** 2               # yangi qiymat, kirish o'zgarmaydi
        print("  kvadratlar:", y)
        yield y

def juftlar(it: Iterable[int]) -> Iterator[int]:
    for x in it:
        if x % 2 == 0:
            print("    juftlar:", x)
            yield x

print(list(juftlar(kvadratlar(manba([1, 2, 3, 4])))))