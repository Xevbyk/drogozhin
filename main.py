import math
while True:
    try:
        x = int(input())
    except ValueError:
        print('Введите x: ')
    else:
        break
c = 3.14/4
if x > c:
    s1 = math.sin(x)
    c1 = math.cos(x)
    print("sin:", s1, "and" ,"cos:", c1)
else:
    print("x < 3.14/4")