# """Необходимо создать функцию sumNumbers(n), которая будет
# считать сумму всех элементов от 1 до n."""

# def sum_numbers(n):
#     summa =0
#     for i in range(1, n+1):
#         summa+=1
#     return summa

# a = sum_numbers(5)
# print(a)


# def sum_str(*args):
#     res = ''
#     for i in args:
#         res+=i
#     return res

# print(sum_str('a', 'c', 'f'))



'''рекурсия'''

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list1 = []
# for i in range(5,30):
#     list1.append(fib(i))
# print(list1) 

'''алгоритмы'''

'''быстрая сортировка'''
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0] # сохраняем первый элемент
#     less = [i for i in array[1:] if i <= pivot]  # массив с числами меньше pivot
#     greater = [i for i in array[1:] if i > pivot] # массив с числами больше pivot
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([10,5,6,3,9,23,4,67,8]))

'''Сортировка слиянием'''

def merge_sort (nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0 #счетчики индексов
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k +=1
        while i < len(left): # если левая часть длиннее чем правая
            nums[k] = left[i]
            i+= 1
            k+= 1
        while j < len(right): #если правая часть длиннее чем левая 
            nums[k] = right[j]
            j +=1
            k+=1
list1 = [1,4,7,89,56,44,34,2,33,12,2,33,11,2,3,4]
merge_sort(list1)
print(list1)