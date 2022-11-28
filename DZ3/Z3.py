# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением 
# дробной части элементов.
import random
list = []
for i in range(1,11):
    list.append(round(random.uniform(1,10),2))
print(list)
import math
list2 = math.modf(list)
print(list2)



