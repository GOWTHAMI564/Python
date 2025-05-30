# Extraction of digits using for loop
''' 1st approach '''
n=1234
num=n
while(num>0):
    last_digit=num%10
    print(last_digit)
    num=num//10

''' 2nd approach '''
def print_digits(n):
    if n == 0:
        return
    print(n % 10)
    print_digits(n // 10)
n = 1234
print_digits(n)

''' 3rd approach '''
n=1234
num=n
for _ in range(len(str(n))):
    last_digit=num%10
    print(last_digit)
    num=num//10




## count number of digits 
''' 1st approach '''
n=5234
num=n
count=0
while num:
    count+=1
    num=num//10
print(count)


''' 2nd approach '''
n=53436
count=0
for i in range(len(str(n))):
    count+=1
print(count)


''' 3rd approach '''
from math import *
def count(n):
    return int(log10(n)+1)
n=13234
print(count(n))



## check if a number is a palindrome or not
''' 1st approach '''
num=1234
n=num
res=0
while num:
    ld=num%10
    res=(res*10)+ld
    num=num//10
print(res==n)


''' 2nd approach '''
num = 12321
print(str(num) == str(num)[::-1])
# Space Complexity: O(log n) (string takes space)


''' 3rd approach '''
num = 12321
s = str(num)
i, j = 0, len(s) - 1
is_palindrome = True
while i < j:
    if s[i] != s[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1
print(is_palindrome)
