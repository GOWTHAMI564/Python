## Reverse a string

''' 1 st method '''
def reverse(s):
    k=s[::-1]
    return k
s=input()
print(reverse(s))

''' 2 nd method '''
def reverse(s):
    k=list(s)
    k.reverse()
    return ''.join(k)
s=input()
print(reverse(s))


## Find sum of maximum and minimum element in the array 
def findSum(n,arr):
    if n==1:
        return arr[0]
    if arr[0]>arr[1]:
        mini=arr[1]
        maxi=arr[0]
    else:
        mini=arr[0]
        maxi=arr[1]
    for i in range(2,n):
        if arr[i]<mini:
            mini=arr[i]
        elif arr[i]>maxi:
            maxi=arr[i]
    return maxi+mini
n=4
arr=[1,2,3,4,2,4]
print(findSum(n,arr))


## kth smallest element 
def kthsmallestelement(arr,k):
    if len(arr)==1:
        return arr[0]
    arr.sort()
    return arr[k-1]
k=2
arr=[1,2,3,4,5,7,8]
print(kthsmallestelement(arr,k))


## kth smallest element  with duplicates 
def kthsmallestelement(arr,k):
    arr = sorted(set(arr)) 
    if len(arr)==1:
        return arr[0]
    
    return arr[k-1]
k=2
arr=[1,2,2,3,4,5,7,8]
print(kthsmallestelement(arr,k))


## kth largest element 
def kthlargestelement(arr,k):
    if len(arr)==1:
        return arr[0]
    arr.sort(reverse=True)
    return arr[k-1]
k=2
arr=[1,2,3,4,5,7,8]
print(kthlargestelement(arr,k))



## kth smallest element  with duplicates 
def kthlargestelement(arr,k):
    arr = sorted(set(arr), reverse=True ) 
    if len(arr)==1:
        return arr[0]
    return arr[k-1]
k=2
arr=[1,2,3,4,5,7,6,7,8]
print(kthlargestelement(arr,k))