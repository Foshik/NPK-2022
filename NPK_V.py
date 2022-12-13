def DV(x):
    if x >= 0:
        p = ''
    else:
        p = '-'
    x = abs(x)
    a = []
    while x != 0:
        a.append(x % 2)
        x //= 2
    if p == '-':
        a.append(p)
    a = a[::-1]
    return a


def N(x):
    x = abs(x)
    i = 0
    while 2 ** i < x:
        i += 1
    return i


print("Введите x,y через пробел")
s = input().split()
x = int(s[0])
y = int(s[1])
if x == 0:
    print("Ответ:0")
    exit()
if y == 0:
    print("На 0 не делим")
    exit()
znakx = '+' if x >= 0 else '-'
znaky = '+' if y >= 0 else '-'
k = x / y
print("X в двоичной записи", *DV(x))
print("Y в двоичной записи",' ', *DV(y))
print("Минимальная разрядная сетка", N(k) + 1)
print("Введите разрядную сетку")
n = int(input()) - 1
# |X| перевод в доп код с разрядной сеткой
mx = DV(abs(x))
if 2 * n > len(mx):
    mx = mx[::-1]
    for i in range(2 * n - len(mx)):
        mx.append(0)
    mx.append(0)
    mx.append(0)
    mx = mx[::-1]
else:
    mx = mx[::-1]
    mx.append(0)
    mx.append(0)
    mx = mx[::-1]
# перевод окончен
my = DV(-(abs(y)))
my.pop(0)
# Перевод -|y| в доп код
for i in range(len(my)):
    if my[i] == 1:
        my[i] = 0
    else:
        my[i] = 1
for i in range(len(my) - 1, -1, -1):
    if my[i] == 1:
        my[i] = 0
    else:
        my[i] = 1
        break
if n > len(my):
    my = my[::-1]
    for i in range(n - len(my)):
        my.append(1)
    my.append(1)
    my.append(1)
    my = my[::-1]
else:
    my = my[::-1]
    my.append(1)
    my.append(1)
    my = my[::-1]

print("Проверка |X| - |Y|:")
print("|X| = ", *mx)
print("-|Y| =", *my)

# |X| -|Y| сложение
for i in range(len(my)):
    mx[i] += my[i]
for i in range(len(mx) - 1, 0, -1):
    if mx[i] == 3:
        mx[i] = 1
        mx[i - 1] += 1
    elif mx[i] == 2:
        mx[i] = 0
        mx[i - 1] += 1
if mx[0] == 3:
    mx[0] = 1
elif mx[0] == 2:
    mx[0] = 0
# Сложение закончено
print("RES = ", *mx)
if mx[0] == mx[1] == 1:
    print("Переполнения не будет, делить можно")
else:
    print("Будет переполнение, делить нельзя")
    exit()
# окончание проверки

# сначала конвектируем потом +1
a = DV(x)
if a[0] == '-':
    a.pop(0)
    for i in range(len(a)):
        if a[i] == 1:
            a[i] = 0
        else:
            a[i] = 1
    for i in range(len(a) - 1, -1, -1):
        if a[i] == 0:
            a[i] = 1
            break
        else:
            a[i] = 0
    a = a[::-1]
    for i in range(2 * n - len(a)):
        a.append(1)
    a.append(1)
    a.append(1)
    a = a[::-1]

else:
    a = a[::-1]
    for i in range(2 * n - len(a)):
        a.append(0)
    a.append(0)
    a.append(0)
    a = a[::-1]
XDOP = a.copy()
del a

print(" X в доп коде: ", *XDOP)
# перевод y в доп код
a = DV(y)
if a[0] == '-':
    a.pop(0)
    for i in range(len(a)):
        if a[i] == 1:
            a[i] = 0
        else:
            a[i] = 1
    for i in range(len(a) - 1, -1, -1):
        if a[i] == 0:
            a[i] = 1
            break
        else:
            a[i] = 0
    a = a[::-1]
    for i in range(n - len(a)):
        a.append(1)
    a.append(1)
    a.append(1)
    a = a[::-1]

else:
    a = a[::-1]
    for i in range(n - len(a)):
        a.append(0)
    a.append(0)
    a.append(0)
    a = a[::-1]
YDOP = a.copy()

print(" Y в доп коде: ", *YDOP)
del a
# Перевод -У
a = DV(-y)
if a[0] == '-':
    a.pop(0)
    for i in range(len(a)):
        if a[i] == 1:
            a[i] = 0
        else:
            a[i] = 1
    for i in range(len(a) - 1, -1, -1):
        if a[i] == 1:
            a[i] = 0
        else:
            a[i] = 1
            break
    a = a[::-1]
    for i in range(n - len(a)):
        a.append(1)
    a.append(1)
    a.append(1)
    a = a[::-1]

else:
    a = a[::-1]
    for i in range(n - len(a)):
        a.append(0)
    a.append(0)
    a.append(0)
    a = a[::-1]
MYDOP = a.copy()
print("-Y в доп коде: ", *MYDOP)
z = []
print("Начало деления")
R = []
if znakx == znaky:
    for t in range(n):
        XDOP.pop(0)
        R = XDOP.copy()
        print(" Сдвиг :", *XDOP, '|', *z, '-')  ##8 символов
        print("+(-Y)  :", *MYDOP)
        for i in range(len(MYDOP)):
            XDOP[i] += MYDOP[i]
        for i in range(len(XDOP) - 1, 0, -1):
            if XDOP[i] == 3:
                XDOP[i] = 1
                XDOP[i - 1] += 1
            elif XDOP[i] == 2:
                XDOP[i] = 0
                XDOP[i - 1] += 1
        if XDOP[0] == 3:
            XDOP[0] = 1
        elif XDOP[0] == 2:
            XDOP[0] = 0
        print("RES:    ", *XDOP)
        if XDOP[0] == XDOP[1] == 1:
            if znakx == '+':
                print("R < 0, Z = 0, требуется восстановление остатка")
                z.append(0)
                XDOP = R
            elif znakx == '-':
                print("R < 0, Z = 1, восстановление не требуется")
                z.append(1)
        else:
            if znakx == '+':
                print('R >= 0, Z = 1, восстановление остатка не требуется')
                z.append(1)
            else:
                print("R >=0, Z = 0, требуется восстановление остатка")
                z.append(0)
                XDOP = R
        print("X тек:  ", *XDOP, '|', *z)
else:
    for t in range(n):
        XDOP.pop(0)
        R = XDOP.copy()
        print(" Сдвиг :", *XDOP, '|', *z, '-')  ##8 символов
        print(" +Y    :", *YDOP)
        for i in range(len(YDOP)):
            XDOP[i] += YDOP[i]
        for i in range(len(XDOP) - 1, 0, -1):
            if XDOP[i] == 3:
                XDOP[i] = 1
                XDOP[i - 1] += 1
            elif XDOP[i] == 2:
                XDOP[i] = 0
                XDOP[i - 1] += 1
        if XDOP[0] == 3:
            XDOP[0] = 1
        elif XDOP[0] == 2:
            XDOP[0] = 0
        print("RES:    ", *XDOP)
        ###
        if XDOP[0] == XDOP[1] == 1:
            if znakx == '+' and znaky == '-':
                print("R<=0, Z = 1, требуется восстановление остатка")
                z.append(1)
                XDOP = R
            elif znakx == '-' and znaky == '+':
                print("R<=0, Z = 0, восстановление остатка не требуется")
                z.append(0)
        else:
            if znakx == '+' and znaky == '-':
                print("R > 0, Z = 0, восстановление остатка не требуется")
                z.append(0)
            elif znakx == '-' and znaky == '+':
                print("R > 0, Z = 1, требуется восстановление остатка")
                z.append(1)
                XDOP = R
        print("X тек:  ", *XDOP, '|', *z)
print("Результат деления в доп коде:", *z)
print("Остаток в доп коде:", *XDOP)
if znaky != znakx:
    for i in range(len(z)):
        if z[i] == 1:
            z[i] = 0
        else:
            z[i] = 1
z = z[::-1]
S = 0
for i in range(len(z)):
    S += 2 ** i * z[i]
if znakx != znaky:
    S *= -1
s = 0
if XDOP[0] == XDOP[1] == 1:
    for i in range(len(XDOP) - 1, -1, -1):
        if XDOP[i] == 0:
            XDOP[i] = 1
        else:
            XDOP[i] = 0
            break
    XDOP.pop(0)
    XDOP.pop(0)
    for i in range(len(XDOP)):
        if XDOP[i] == 1:
            XDOP[i] = 0
        else:
            XDOP[i] = 1
    XDOP = XDOP[::-1]
    for i in range(len(XDOP)):
        s += XDOP[i] * 2 ** i
    s *= -1
else:

    XDOP = XDOP[::-1]
    for i in range(len(XDOP)):
        s += XDOP[i] * 2 ** i
print(str(x) + '/' + str(y) + ' = ' + str(S) + ' + ost(' + str(s) + ')')
