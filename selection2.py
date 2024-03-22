a =[1, 2, 3, 5, 8, 9]
b =[]

i = 0

while i < len(a):
    if a[i] < 5:
        b.append(a[i])
    i = i + 1
    
print(b)  
