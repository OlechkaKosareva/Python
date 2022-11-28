#Задайте список из нескольких чисел. Напишите программу, 
#которая найдёт сумму элементов списка, стоящих на нечётной позиции.
list1 = []
for i in range(1, 11): 
   if (i%2 == 1):
    list1.append(i);
print(list1)
sum = 0
for i in list1:
 sum = sum + i
print(sum)
