a =[3, 6, 8]
b = []
c = []

for element in a:
    b.append(element*2)

print(b)

i = 0

while i < len(a):
    c.append(a[i] * 3)
    i = i + 1

print(c)
