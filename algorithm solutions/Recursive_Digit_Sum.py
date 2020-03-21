def superDigit(n, k):    
    p=len(n)    
    if p==1:
        print( n)
    else:
        a=0
        for i in n:
            a=a+int(i)
        
        a=a*k
        x=str(a)
        superDigit(x,1)
    
    
nk = input().split()
n = nk[0]
k = int(nk[1])
superDigit(n, k)