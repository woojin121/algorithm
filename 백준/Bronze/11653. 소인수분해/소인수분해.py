from sys import stdin
a = int(stdin.readline())

if a <= 1:
    quit()

i = 2
b = []
while i < a :
    if a%i == 0:
        a = a/i
        b.append(i)
    else:
        i+=1
b.append(int(a))        

print('\n'.join(map(str,b)))