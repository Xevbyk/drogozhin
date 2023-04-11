#1
a = 10 
b = 25.4
while a <= 22:
    sant = a * b
    print (sant)
    a +=1 

#2
a = int(input())
b = 1 
while b <= 20:
    rub = b * a
    print(rub)
    b+=1

#3
e = int(input())    
i = 1 
while i <= 20:
    e **= i
    print(e)
    i += 1 

#4
i = 1.1 
while i <= 21.1:
    print (i)
    i+=1    

#5
i = 2.1 
while i <= 3:
    print (i)
    i+=0.1

#6
a = 0
while a < 40:
    a = a + 2
    print(a)

#7 
a = 1
i = 0
while i < 15:
    a = a + 2
    i = i + 1
    print(a)

#8 
a = 0
b = 0
i = 0
while i < 20:
    a = (b+2)**0.5
    b = b + 2
    i = i + 1
    print(a)
    
#9 
a = int(input())
b = 1
n = 10
i = 0
while i < n:
    i = i + b
    ii = i * a
    print("КГ", i)
    print('Стоимость', ii)
#10
a = int(input())
b = int(input())
while a < b:
    y = a ** 0.5
    print(y)
    a += 1

#11
a = int(input())
b = int(input())
while a < b:
    y = a ** 2 - 1
    print(y)
    a += 1
    
#12
a = int(input())
b = int(input())
while a < b:
    y = 1/2*a
    print(y)
    a += 1

#13
a = int(input())
b = int(input())
while a < b:
    y = (a - 1)**2
    print(y)
    a += 1
    
#14
x = 0
while x <= 20:
    t = 1 + x
    y = (2 * t**2) + 2 * t + 2
    print(y)
    x = x + 1
    
# 15
x = 2
while x <= 20:
    f = 2 * x
    z = 8 * (f**2) - f 
    print(z)
    x = x + 1