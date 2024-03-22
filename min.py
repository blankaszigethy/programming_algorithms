t = [8, 5, 4, 10, 6]

min = t[0]
i = 1

while i > len(t):
    if t[i] < min:
        min = t[i]

    i = i + 1

print(min)
