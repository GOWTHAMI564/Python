# missing first positive value in a given list 
# input :[1,2,3,4] len=5 output: 5 
# input :[1,4,2]  len= 4 output= 3


# def append(nums):
#     n=len(nums)+1
#     return list(range(1,n+1))
# nums=[1,4,3]
# print(append(nums))

# nums=[1,4,3]
# for i in range(1,nums+1):










# move zeros to the last 

# n=[0,1,0,2,4]
# res=[]
# for i in n:
#     if i !=0:
#         res.append(i)
# t=n.count(0)
# print(t)
# res+=[0]*t
# print(res)



# n=[0,1,0,2,4]
# for i in n:
#     if i ==0:
#         n.append(0)
#         n.remove(0)
#         # n.append(0)
# print(n)

# move even numbers to the last 
# n=[0,1,0,2,4]
# even=[]
# odd=[]
# for i in n:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# res=odd+even
# print(res)


#two pointer method
# n=[1,2,3,4,5]
# k=0
# for i in range(len(n)):
#     if n[i]%2!=0:
#         temp=n.pop(i)
#         n.insert(k,temp)
#         k+=1
# print(n)



#count the number of 1's in a number
# num = 65
# binary = bin(num)[2:] # [2:] removes the '0b' prefix
# print("Binary:", binary)
# print(binary.count('1'))
# oct=oct(num)[2:]
# print(oct)

