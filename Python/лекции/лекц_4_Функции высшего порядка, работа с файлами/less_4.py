"""def f(x):
    return x * x
print(f(5))

print(type(f))


"""
####################################
'''def calk1(a):
    return a+a

def calk2(a):
    return a*a

def math(op, x):
    print(op(x))

math(calk2, 5)'''
############################
'''def calk1(a, b):
    return a + b

def calk2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(calk2, 5, 3)'''
#################################

# lambda функция
'''def math(op, x, y):     ##то же самое def calk1(a, b):
                          #                 return a + b
    print(op(x, y))

calk1 = lambda a,b: a+b

math(calk1, 5, 7)   #или    math(lambda a,b: a+b, 5, 7)
'''
 
"""1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
(число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)]"""

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = list()

for i in data:
    if i % 2 == 0:
        res.append((i, i**2))

print(res)