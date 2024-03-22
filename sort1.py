a =[9, 6, 4, 7, 2]

i = 0

while i < len(a) - 1:
    j = i + 1
    while j < len(a):
        

        print(f'i = {i}')
        print(f'j = {j}')
        print(f'a[i] = {a[i]}')
        print(f'a[j] = {a[j]}')

        if a[j] > a[i]:
            print("CSERE")
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
        j = j + 1
        print(a)
        print("------------------------------")

    i = i + 1        

#print(a)