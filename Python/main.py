# a = 2000

# if (a % 4==0 and a % 100 !=0) or a % 400== 0:
#     print("високосный")
# else: 
#     print("невисокосный")
# n = 'th\'gk'
# print(n)

# a = 5
# b = 5.67
# c = 'hello'
# print(a,b,c)
# # или
# print(a,'-',b,'-',c)
# # или
# print(f"{a}-{b}-{c}")
# # или
# print("{}-{}-{}".format(a,b,c))

# print('введите первое число: ')
# a = input()
# b = input('введите второе число: ')
# print(a, '+', b, '=', a+b)


# print('введите первое число: ')
# a = int(input())
# b = int(input('введите второе число: '))
# print(a, '+', b, '=', a+b)

# a = 5.68346
# b = 3.957
# print(round(a*b, 1))


# c = 5.89
# print(c)
# n = int(c)
# print(n)

# c = 5.89
# print(c)
# print(type(c))
# c = str(c)
# print(c + '90')
# print(type(c))

# username = input('Введите имя: ')
# if username == "Маша":
#     print('Ура, это же Маша!')
# elif username == "Марина":
#     print('Это же Марина!')
# elif username == "Коля":  
#     print('Коля Николай!')
# else:
#     print('Привет,', username )


n = 423
summa = 0
while n > 0:
    x = n%10
    summa = summa+x
    n = n // 10
print(summa)



