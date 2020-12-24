def read():
    while True:
        try:
            yield input()
        except:
            return

i = 0
c = 0
for row in read():
    if row[i] == '#': c += 1
    i = (i + 3) % len(row)
print(c)
