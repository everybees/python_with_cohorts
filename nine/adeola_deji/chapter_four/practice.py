a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}

new_dic = {}

for key, val in a_dict.items():
    new_dic[val] = key
print(new_dic)

objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']

a_dict = {key: value for key, value in zip(categories, objects)}
print(a_dict)


incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
print(sorted(incomes))
for key in sorted(incomes):
    print(key, '->', incomes[key])

def sort_by_value(item):
    return item[1]

for k, v in sorted(incomes.items(), key= sort_by_value):
    print(k, "==>", v)

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
count = 0
while count < len(a_dict)-1:
    try:
        print(f'Dictionary length: {len(a_dict)}')
        item = a_dict.popitem()
        print(f'{item} was removed')
    except:
        print('The dictionary has no item now')
        break
count += 1
print(a_dict)
