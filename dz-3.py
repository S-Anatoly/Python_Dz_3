# -Task_1-
print('Сумма элементов списка, стоящих на нечётной позиции')
list1 = [2, 3, 5, 9, 3]
print(list1)
sum = 0
for i in range(len(list1)):
    if i %2!=0:
        sum+=list1[i]
        print(f'Число с нечетным индексом -> {list1[i]}')

print(f'Сумма элементов, стоящих на на нечетных позициях -> {sum}')

# -Task_2-
print('Напишите программу, которая найдёт произведение пар чисел списка. '
      'Парой считаем первый и последний элемент, второй и предпоследний и т.д')
list1 = [2, 3, 4, 5, 6]
print(list1)
pr = 0
n=0
len1 = len(list1)
while n < (len1):
    pr = list1[n] * list1[len1-1]
    n+=1
    len1-=1
    print(pr, end=' ')

# -Task_3-
print('Разница между максимальным и минимальным значением дробной части элементов.'
      'Пример: - [3.1, 1.2, 3.1, 10.01] => 0.19')

list1= [1.1, 1.2, 3.1, 5, 10.01]
list2 = []
for i in range(len(list1)):
      if type(list1[i]) == float:         # Проверка: если число дробное, то записываем его дробную часть в новый список
            list2.append(round((list1[i]-int(list1[i])),2))  #берем ,сокращенную до двух знаков, дробную часть элемента, и записываем его в новый список
raz = round((max(list2)-min(list2)),2)                # находим разницу между мак и мин
print(f'Исходный список -> {list1}')
print(f'Список дробных частей списка -> {list2}')
print(f'Разница между максимальным и минимальными дробными частами -> {raz}')

# -Task_4-
print('Напишите программу, которая будет преобразовывать десятичное число в двоичное.'
      'Пример: - 45 -> 101101'
      '- 3 -> 11'
      '- 2 -> 10')
number = int(input('Введите число: '))
b=[]
print(f'Число {number} в двоичной сисстеме = ', end='')
while number != 0:
      b.insert(0,number%2)
      number//=2
print(''.join(map(str,b)))

# -Task_5-
print('Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов')
number = int(input('Введите число: '))
arr=[0]
def fib(x):
      if x <= 1:
            return 1
      else:
            return fib(x-1)+fib(x-2)
for i in range(number):
      arr.append(fib(i))
print(arr)
arr2=[]
def fib2(x):
      if x <= 1:
            return 1
      else:
            return fib(x)-fib(x+2)
for i in range(number):
      arr2.append(fib2(i))
print(arr2)
print(sorted(arr2,reverse=False)+arr)
