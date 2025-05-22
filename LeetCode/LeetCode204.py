''' 204. Count Primes '''
'''Example '''

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0
def countPrimes(n):
    prime=[1]*n
    for i in range(2,int(n**0.5)+1): # O(LOG(LOGN))
        if(prime[i]==1):
            for j in range(i*i,n,i):
                prime[j]=0
    count=0
    for i in range(2,n): #O(N)
        if(prime[i]==1):
            count+=1
    return count
n=int(input())
print(countPrimes(n))