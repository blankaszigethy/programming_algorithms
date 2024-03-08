t =[2, 5, 6, 7]

value = 9
exists = False
i = 0

while i < len(t):
    if t[i] == value:
        exists = True

    i += 1

print(exists)

