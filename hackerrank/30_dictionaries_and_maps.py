n = int(input())
contacts = dict()
for i in range(n):
    name, number = input().split()
    contacts[name] = number
while True:
    try:
        name = input()
        print('Not found' if name not in contacts else f'{name}={contacts[name]}')
    except EOFError:
        break
 