# list_1 =[1, 5]
# print(list_1)
# list_1.append(8)
# print(list_1)
# list_1.append(85)
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# t = ()
# print(type(t))

# t = (1,)
# print(type(t))

# v = [1,2,5,]

# v = tuple(v)


# a,b = 1, 2
# a=b=1

# a,b,c = v
# print(a,b,c)
# print(type(v))


d ={} # созданте пустого словаря
d = dict() # созданте пустого словаря

d['q'] = 'qwerty' # добавление элемента в словаря
d['w'] = 'werty'

print(d['w']) # вывод элемента из словаря синдексом w


dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→' }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться

# dictionary[895]  = 98998 # добавление числа в словарь строк
# print(dictionary)

# # dictionary['left'] = '⇐'
# # print(dictionary['left']) # ⇐
# #print(dictionary['type']) #  KeyError: 'type' когда нет такого значения в словаре
# del dictionary['left'] # удаление элемента

# for it in dictionary: 
    
#     print(it)


# #     # for (k,v) in dictionary.items():
# print('{}: {}'.format(it, dictionary[it]))

# # # up: ↑
# # down: ↓
# # right: →

# МНОЖЕСТВА

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}

#ОПЕРАЦИИ С МНОЖЕСТВАМИ

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}  копирование
print(c)
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} объединение
i = a.intersection(b) # i = {8, 2, 5}   пересечение
dl = a.difference(b) # dl = {1, 3}   разность а-в
dr = b.difference(a) # dr = {13, 21}  разность в-а
q = a \
 .union(b) \
 .difference(a.intersection(b))
# {1, 21, 3, 13}


