x = int(input())
print(type(x))
c = 3.14/4
if type(x) == int:
    s1 = (1 - x ** 3)
    c2 = (x - x ** 3 / 6)
    print("sin:", s1, "and" ,"cos:", c2)
elif type(x) == str:
    print("нет")