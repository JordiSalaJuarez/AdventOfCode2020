def read():
    while True:
        try:
            lr, [c, _], p = input().split()
            l, r = map(int, lr.split('-'))
            yield [l, r], c, p
        except:
            return

def valid(lr, c, p):
    l , r = lr
    return l <= sum(x==c for x in p) <= r

print(sum(valid(lr, c, p) for lr, c, p in read()))