x=2
n=-2
c=1
val=x
if n < 0:
    x = 1/x
    n = abs(n)
while n>2:  
    if n%2!=0:
        c=c*val
    val=val*val
    n=n//2
    print(f'{c}*{val}^{n}')
    
                
if n == 0:
    print( 1)
elif n==1:
    print( c*val)
else: #n==2:
    print( c*val*val)