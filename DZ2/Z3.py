# Задайте список из n чисел последовательности (1+1/n)**n
# и выведите на экран их сумму.
n = int(input('Введите число N = '))
list = []
i = 1
list = [round((1+1/i)**i,1) for i in range(1,n+1)]
print(list)
count = 0
sum = 0
while (count < n):
   count = count + 1
   sum = sum + list[i]
print(sum)