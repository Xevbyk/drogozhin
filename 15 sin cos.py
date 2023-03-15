while True:
    try:
        a = int(input())
        b = int(input())
        c = int(input())
    except ValueError:
        print('Введите число')
    else:
        break
 
s1 = b / c
c1 = a / c
print("sin:", s1 ,"cos:", c1)
