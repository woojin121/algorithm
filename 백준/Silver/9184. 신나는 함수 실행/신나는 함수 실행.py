from sys import stdin
while True:
    a = list(map(int, stdin.readline().split()))
    ar1 = a[0]
    ar2 = a[1]
    ar3 = a[2]
    if a[0] == -1 and a[1] == -1 and a[2] == -1:
        quit()
    elif a[0] <= 0 or a[1] <= 0 or a[2] <= 0:
        print(f"w({a[0]}, {a[1]}, {a[2]}) = 1")
    else:
        if a[0] > 20 or a[1] > 20 or a[2] > 20:
            a[0] = 20
            a[1] = 20
            a[2] = 20
        
        
        
        arr = [[[0 for col in range(a[2]+1)] for row in range(a[1]+1)] for depth in range(a[0]+1)]
        #print(a[0],a[1],a[2])
        #arr[2][0][0] = 1
        #arr[2][1][0] = 1
        #print(arr)
        
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                for k in range(len(arr[i][j])):
                    if i <= 0 or j <= 0 or k <= 0:
                        arr[i][j][k]=1
                    elif i < j and j < k:
                        arr[i][j][k]=arr[i][j][k-1] + arr[i][j-1][k-1] - arr[i][j-1][k]
                    else:
                        arr[i][j][k]=arr[i-1][j][k] + arr[i-1][j-1][k]+ arr[i-1][j][k-1] - arr[i-1][j-1][k-1]
        
        #print(arr)                
        print(f"w({ar1}, {ar2}, {ar3}) = {arr[a[0]][a[1]][a[2]]}")