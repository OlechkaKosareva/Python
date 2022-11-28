# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением 
# дробной части элементов.
import random
list = []
for i in range(1,11):
    list.append(round(random.uniform(1,10),2))
print(list)
list2 = [round(list2%1,2) for list2 in list]
print(list2)
delta = (max(list2) - min(list2))*100
print(max(list2), min(list2),delta)






