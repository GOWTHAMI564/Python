''' PRIME NUMBER ''' 
# METHOD-1
n=int(input())
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Not prime")
            break
    else:
        print("prime") 
else:
    print("Not a prime")    

# METHOD-2
n=int(input())
if n>1:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("Not prime")
            break
    else:
        print("prime") 
else:
    print("Not a prime")    


# prime number in the given range 
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num,end=" ")