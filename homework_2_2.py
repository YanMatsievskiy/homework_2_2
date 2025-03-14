'''Задача 2. Сортировка с параметром'''

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
s = str(input('Введите символ "<" или ">": '))

if s == '>' and a < b:
  print(b, a)
elif s == '<' and a > b:
  print(b, a)
else:
  print(a, b)