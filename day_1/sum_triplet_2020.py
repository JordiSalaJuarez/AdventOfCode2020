def numbers():
    while True:
        try:
            yield int(input())
        except:
            return

xs = sorted(numbers())
i, j, k = 0, 1 , len(xs) - 1

while xs[i] + xs[j] + xs[k] != 2020 and i < j < k:
    while xs[i] + xs[j] + xs[k] != 2020 and j < k:
        while xs[i] + xs[j] + xs[k] < 2020: j += 1
        while xs[i] + xs[j] + xs[k] > 2020: k -= 1
    if xs[i] + xs[j] + xs[k] == 2020: break 
    i, j, k = i + 1, i + 2 , len(xs) - 1
else:
    print("Failed")

print(xs[i] * xs[j] * xs[k])