t = [8, 5, 4, 10, 6]

max = t[0]
i = 1

while i > len(t):
    if t[i] > max:
        max = t[i]

    i = i + 1

print(max)
