from sys import stdin
a = int(stdin.readline())
b = []
for n in range (a):
    b.append(int(stdin.readline()))
    
b.sort()

for result in b:
    print(result)
