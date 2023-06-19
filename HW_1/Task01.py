# напечатать таблицу умножения

BEGINER, STEP, MAX_FIRST_NUM, MAX_SECOND_NUM = 2, 4, 9, 10

for i in range(BEGINER, MAX_FIRST_NUM, STEP):
    for j in range(BEGINER, MAX_SECOND_NUM + 1):
        for k in range(i, i + STEP):
            print(f'{k}  x {j:>2} = {j * k:>2}', end = ' '*3)
        print()
    print()