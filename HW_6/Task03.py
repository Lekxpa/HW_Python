# *Выведите все успешные варианты расстановок

import itertools

count = 0
def queens_all_wins():
    for pos in itertools.permutations(range(8)):
        yield [x for x in enumerate(pos)]
        
for i in queens_all_wins():
    chnc = False
    for r, c in ((r, c) for r in i for c in i if r[0] < c[0]):
        if abs(r[0] - c[0]) == abs(r[1] - c[1]):
            chnc = True
            break
    if not chnc: 
        count += 1
        print(i)

queens_all_wins()
print(f'Количество успешных расстановок:  {count}')