
def power(x,n) :
    if n==0:
        return 1
    if n%2 ==1 :
        return x*power(x,n-1)
    if n%2==0:
        return power(x*x,n//2)
def myPow(x,n):
    if n<0:
        x=1/x
    n=abs(n)
    return power(x,n)
x=float(input())
n=int(input())
print(myPow(x,n))
