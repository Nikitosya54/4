n = int(input("количество дней:"))
days1 = int(input("курс на первый день:"))
x = int(input("проценты: "))

for i in range(n):
    days1 = days1 * (1 + x / 100)
print(days1)
