#10
a = int(input("Введите длину верхнего основания"))
b = int(input("Введите длину нижнего основания"))
c = int(input("Введите длину высоты"))
(P) = a + b + 2**0.5 * c * 2 + (a - b) * 2/4
print (P)

#11
m = int(input("масса тела"))
v = int(input("объем тела"))
p = m/v
print (p)

#12
a = int(input())
b = int(input())
x1 = a+b 
x2 = a-b
x3 = a*b 
x4 = a/b 
print (x1, x2, x3, x4)

#13
a = int(input())
b = int(input())
x = a/b 
Z = int(input("Введите произведение чисел"))
V = Z ** 0.5
print (x, V)

#14
N = int(input("Введите кол-во жителей"))
S = int(input("Введите площадь государства"))
R = N/S 
print ("Плотность населения", R)

#15
a = int(input("длинуа))
b = int(input("ширина"))
c = int(input("высота"))

v = a * b * c 
s = 2 * (a * b + b * c + a * c) 

print("Объём равен", v)
print("Площадь поверхности равна", s)