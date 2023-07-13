# *Выведите все успешные варианты расстановок
from random import randint
import itertools

count = 0
def queens_all_wins():
    for pos in itertools.permutations(range(8)):
        yield [x for x in enumerate(pos)]
for i in queens_all_wins():
    err = False
    for a, b in ((a, b) for a in i for b in i if a[0] < b[0]):
        if abs(a[0] - b[0]) == abs(a[1] - b[1]):
            err = True
            break
    if not err: 
        count += 1
        print(i)

queens_all_wins()
print(count)