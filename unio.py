a =[1, 2, 3, 4, 5]
b =[4, 5, 6, 7, 8]
c = []

i = 0 

while i < len(a):
    c.append(a[i])
    i = i + 1

j = 0

while j < len(b):
    if b[j] not in c:
        c.append(b[j]) 
    j = j + 1 


print(c)