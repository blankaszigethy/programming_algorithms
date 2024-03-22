a = [3, 2, 7, 1, 4, 5, 8, 15, 17]
b = []
c = []
d = []

i = 0

while i < len(a):
    if a[i] < 5:
        b.append(a[i])

    elif a[i] > 5:
        c.append(a[i])
       
    else:
        d.append(a[i])


    i = i + 1

print(b)
print(c)
print(d)