n = int(input(" начальный член "))
a = int(input(" начальный член "))
r = int(input(" знаменатель "))

for i in range(1, n+1):
    d = a*r**(i-1)
    print(d)