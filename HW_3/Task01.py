# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# 1) Какие вещи взяли все три друга (реализовано - общий список вещей без повторов)

# 2) Какие вещи уникальны, есть только у одного друга и имя этого друга

# 3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

campaign = {
    'Никита': ('Палатка', 'Спальник', 'Фонарик', 'Зажигалка', 'Столик', 'Стулья'),
    'Ярик': ('Палатка', 'Спальник', 'Вода', 'Продукты', 'Кружка'),
    'Наташа': ('Спальник', 'Подушка', 'Сгущенка', 'Ложка', 'Кружка', 'Салфетки', 'Фонарик')
}

lst = []
lst_all = []
dict_unique = {}
dict_items_out = {}

for v in campaign.values():
    if v not in lst:
        lst += v

for i in lst:
    if i not in lst_all:
        lst_all.append(i)

for item in campaign:
    items_unique = set(campaign[item])
    items_out = set()
    for next_item in campaign:
        if next_item != item:
            items_unique -= set(campaign[next_item])
            if not items_out:
                items_out |= (set(campaign[next_item]))
            else:
                items_out.intersection_update(set(campaign[next_item]))
    dict_unique[item] = items_unique
    dict_items_out[item] = items_out - set(campaign[item])

print(f'\nОбщий список вещей, которые взяли с собой все друзья: {lst_all}\n')
print(f'Уникальные вещи: {dict_unique}\n')
print(f'Вещи, которые есть у всех, кроме одного: {dict_items_out}\n')