#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.
arr = [1, 2, 3, 4, 3, 2, 1]
list = []
list_len = len(arr)
if list_len%2 == 0:
    n = list_len//2
else: n = list_len//2 + 1
for i in range(0,n):
    list.append(arr[i]*arr[list_len - i - 1])
print(list)

