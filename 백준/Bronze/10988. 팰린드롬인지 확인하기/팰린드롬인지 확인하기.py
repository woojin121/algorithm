a = input()

def pelin(a):
    for idx in range(0,(len(a)//2)+1,1):
        if a[idx]!= a[-1-idx] :
            return 0
        # TODO: write code...
        
    return 1
        
print(pelin(a))