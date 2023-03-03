#1 
n = (input())
if (int(n)>999) and (int(n)<10000):
    a = int(n[0])+int(n[1])+int(n[2])+int(n[3])
    b = int(n[0])*int(n[1])*int(n[2])*int(n[3])
    print (a)
    print (b)
else:
    print("не четырехзначное число")
#2
a = (input())
if (int(a)>9999) and (int(a)<100000):
    q = int(a[3]) 
    w = int(a[4])
    print (q)
    print (w)
else:
    print("не пятизначное число")
#3
x = int(input())
aa = x // 100 % 10
b = x // 10 % 10
c = x % 10
x1 = c * 100 + b*10 + aa
print (x-x1)

#5
nn = int(input())
print("2" in list(str(nn)))
#7
x = int(input())
a1 = x // 100 % 10
b1 = x // 10 % 10
c1 = x % 10
x = a1 + b1 + c1
if (int(x)>9) and (int(x)<100):
    print("является")
else:
    print('не является')
x1 = a1*b1*c1
if (int(x1)>99) and (int(x1)<1000):
    print("является")
else:
    print('не является')
if (int(x1)>a1):
    print("больше")
else:
    print('не больше')
if (int(x)%5==0):
    print("кратна")
else:
    print('не кратна')
if (int(x)%a1==0):
    print("кратна")
else:
    print('не кратна')
#8
x = int(input())
a3 = x // 1000 % 10
b3 = x // 100 % 10
c3 = x // 10 % 10
d3 = x % 10
x1 = a3+b3+c3+d3
x2 = a3*b3*c3*d3
if int(a3+b3) == int(c3+d3):
    print("Равняется")
else:
    print('не равняется')
if (int(x1)%3==0):
    print("кратна")
else:
    print('не кратна')
if (int(x2)%4==0):
    print("кратна")
else:
    print('не кратна')
if (int(x2)%a==0):
    print("кратна")
else:
    print('не кратна')