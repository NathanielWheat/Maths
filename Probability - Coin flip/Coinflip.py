a = [1, 2, 4, 8, 16]

for n in range(5, 101):
    a.append(sum(a[-5:]))

probability = 1 - a[100] / 2**100

print(probability)