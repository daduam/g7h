t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    good = a+b==c or a+c==b or b+c==a
    print('yes' if good else 'no')
