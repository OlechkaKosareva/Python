# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
print ('Введите координату первой точки х1 =')
x1 = int(input())
print ('Введите координату второй точки х2 =')
x2 = int(input())
print ('Введите координату первой точки y1 =')
y1 = int(input())
print ('Введите координату второй точки y1 =')
y2 = int(input())
dist = (x1-x2)**2+(y1-y2)**2
print ('Расстояние между точками =', dist)