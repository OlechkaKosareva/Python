#Напишите программу, 
#которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)

n = int(input("Введите число: "))
list = []
for e in range(1, n + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {n}:  {list}")