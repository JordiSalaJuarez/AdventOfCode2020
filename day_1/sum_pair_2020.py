def numbers():
    while True:
        try:
            yield int(input())
        except:
            return

xs = sorted(numbers())
i, j = 0 , len(xs) - 1

while xs[i] + xs[j] != 2020 and i < j:
    while xs[i] + xs[j] < 2020: i += 1
    while xs[i] + xs[j] > 2020: j -= 1

if i >= j: print("Failed")
else: print(xs[i] * xs[j])