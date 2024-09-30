n = int(input())
num1 = 0
num2 = 0
for i in range(1, n+1):
    if i % 2 ==0:
        num1 += 1
    else:
        num2 += 1
print(f"четные:{num1}, не четные:{num2}")