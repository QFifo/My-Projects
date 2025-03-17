def Sin(x):
    n=0
    total=0
    while n!=43:
        y=(2*n)+1
        c=1
        for f in range(1,y+1):
            c=f*c
        sinx=(((-1)**n)/(c))*((x)**((2*n)+1))
        total=total+sinx
        n=n+1
    return total
def Cos(x):
    n=0
    total=0
    while n!=43:
        y=(2*n)
        c=1
        for f in range(1,y+1):
            c=f*c
        cosx=(((-1)**n)/(c))*((x)**(2*n))
        total=total+cosx
        n=n+1
    return total

