t = [1, 5, 8, 11]

value = 3

i = 0

while i < len(t) and t[i] != value:
    i += 1

if i < len(t):
    print("value is exists")
    print(f"index: {i}")

else:
    print("value is not exists")

