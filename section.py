a =[5, 3, 6, 2, 1]
b =[6, 2, 7, 8, 9]
c =[]

for i in range(len(a)):
    j = 0
    while j < len(b) and b[j] != a[i]:
        j += 1

    if j < len(b):
        c.append(a[i])
    
print(c)

