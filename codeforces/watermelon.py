w = int(input())
good = False
for i in range(2, w, 2):
   good = good or (w - i) % 2 == 0
print('YES' if good else 'NO')
