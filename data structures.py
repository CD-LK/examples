# list

list0 = []  
list1 = list()
list2 = [1, 2, "text", True, 3.3]
list3 = list(list2)
list4 = [0] * 10

''' Списки позволяют обратиться к отдельному элементу с помощью конструкции list_name[index].
index может изменяться от 0 до (количество элементов в списке - 1). 
При обращении к list_name[0] - получим самый первый элемент списка.
Так же можно обращаться с отрицательными значениями:
list_name[-1] - получить последний элемент списка

'''

random_var = list3[1] #  обратиться к элементу списка по индексом 1.
random_var = list3[-2] # получить предпоследний элемент списка
list3[0] = 11 # изменить последний элемент списка на значение 11
list3[1] = True # изменить последний элемент списка на значение True
list3[2] = [10,11,12] # изменить последний элемент списка на значение True
del list3[0] # удалить элемент из списка

'''цикл для последовательного чтения всех элементов списка.
Переменная num на каждой итерации будет последовательно хранить значение 0го, 1го, 2го и т.д.
элемента списка.
'''
for num in list3:
    print("    ",type(num), num)
    #num = 11 # не позволяет изменять элемемент списка
for index, num in enumerate(list3):
    print(index, ": ", num)
    #num = 11 # не позволяет изменять элемемент списка

for index in range(len(list3)):
    print(index,":", list3[index])
    list3[index] = 11


list10 = [1,2,3]

list10.append(1) # добавить новый элемент в конец списка. [1,2,3,1]
list10.insert(2,11) # добавить новый элемент в список на позицию под индексом 2. Остальные элементы сдвинутся на +1. [1, 2, 11, 3, 1]
list10.insert(0,1) # добавить новый элемент в список на позицию под индексом 2. Остальные элементы сдвинутся на +1. [1, 1, 2, 11, 3, 1]
list10.insert(10, 10) # Просто добавит элемент в конец списка, если максимальный индекс в списке меньше заданного. [1, 1, 2, 11, 3, 1, 10]
print("count(1):", list10.count(1)) # узать количество чисел 1 в списке
list3.reverse() # интвертировать список
list3.clear() # очистить список
list3.remove(1) # удалить самый первый элемент зо значением 11
list2.sort() # сортировать список. Работает, только если элементы списка поддерживают операцию < между собой

list5 = list0.copy() # полное копирование списка. В ином случае переменные list5 и list0 будут обращаться к одному и тому же списку.
list5 = list0      # если осуществить простое присваивание
list5[0] = 100000  # при изменении list5[0] изменится и значение list0[0], так как и list5 и list0 ссылаются на один и тот же список
list5.extend(list0) # расширить список значениями из существующего
  
# поиск в списке
if 1 in list2:
    print("1 in list2")
if 1 not in list2:
    print("1 not in list2")


list6 = [0,1,2,3,4,5,6,7,8,9]

list7 = list6[2:6:2] # создание списка на основе уже существующего, начиная с 0го элемента, заканчивая 6, с шагом копируемых элементов 2
# двумерные списки
list10 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]


# dictionary

dict0 = {}
dict0 = dict()
dict0 = {
    0: "data0", 
    1: "data1"
    }

dict2 = {
    12: "data0", 
    "dict":{1:"kek"},
    "list":[1,2,3,4]
    }


rand_var = dict0[0]  # обращение к элементу словаря
dict0[0] = 123              # запись в словарь. Как запись в существующий элемент, 
dict0["perf_key"] = "data"  # так и создание нового

# пробег по словарю
for key in dict2:  # получение ключей
    print(key)
for key in dict2.keys():  # получение ключей
    print(key)
for value in dict2.values():   # получение значений
    print(value)

for item in dict2.items():   # получение ключей и значений
    print(item)
for key, value in dict2.items():   # получение ключей и значений
    print(key, value)

if 'key0' in dict2:  # поиск по ключу словаря
    print('key0 in dict2')

del dict2['key0']  # удалить элемент словаря
dic10 = dict2.copy()
dict2.clear()
dict2.update(dict0)


# tuple
tuple0 = (0, 1, [1, 2, 3], "123123", 4)
tuple1 = tuple()
print(tuple0.count(0))
list0 = [1,2,3,5, 5, 33, 33]
tuple0.index(10)
len(list0)

#set
set0 = set(list0)
print(set0)
set1 = {1,2,3,4,5}


