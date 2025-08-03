n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print("*",end=" ")
    print()

o/p:
4
* * * * 
* * * * 
* * * * 
* * * * 


# 2
n=3
for i in range(0,n):
    for j in range(i+1):
        print("*",end=" ")
    print()
o/p:
* 
* * 
* * * 


#3
n=3
for i in range(0,n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
o/p:
1 
1 2 
1 2 3 


#4
n=3
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
o/p:
1 
2 2 
3 3 3 


#5
n=3
for i in range(0,n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()

o/p:
1 
2 2 
3 3 3 


#6
n=3
for i in range(0,n):
    for j in range(n-i):
        print('*',end=' ')
    print()

o/p :
* * * 
* * 
* 


#7
n=3
for i in range(0,n):
    for j in range(n-i):
        print(j+1,end=' ')
    print()
o/p:
1 2 3 
1 2 
1 


#8
n=3
for i in range(0,n):
    for j in range(n-i-1):
        print(' ',end='')
    for j in range(2*i+1):
        print("*",end='')
    print()
o/p:
  *
 ***
*****


#9
n=3
for i in range(0,n):
    for j in range(i):
        print(' ',end='')
    for j in range(2*n-2*i-1):
        print("*",end='')
    print()
o/p:
*****
 ***
  *


#10
n=3
for i in range(0,n):
    for j in range(n-i-1):
        print(' ',end='')
    for j in range(2*i+1):
        print("*",end='')
    print()
for i in range(0,n):
    for j in range(i):
        print(' ',end='')
    for j in range(2*n-2*i-1):
        print("*",end='')
    print()

o/p :

  *
 ***
*****
*****
 ***
  *