# count the number of digits in the given integer
# def count(n):
#     if n//10==0:return 1
#     return 1+count(n//10)
# print(count(1234))


# #sum of digits
# n=123
# def sum(n):
#     if n//10==0 : return n
#     return n%10 + sum(n//10)
# print(sum(1))


#find min value in the integer
# n=[1,2,3,4,5]
# def minmax(n):
#     min=n[0]
#     max=n[-1]
#     for i in n:
#         if i <= min:
#             print(i)
#             break
        
#         if i >= max:
#             print(i)
#             break
# print(minmax([1,2,3,4,5,0]))

''' min value '''
# def func(nums):
#     def rec(nums,i):
#         if i==len(nums)-1:
#             return nums[i]
#         min=rec(nums,i+1)
#         return min if min<nums[i] else nums[i]
#     return rec(nums,0)
# print(func([1,2,3,4,5]))
''' max value '''
# def func(nums):
#     def rec(nums,i):
#         if i==len(nums)-1:
#             return nums[i]
#         max=rec(nums,i+1)
#         return max if max > nums[i] else nums[i]
#     return rec(nums,0)
# print(func([1,2,3,4,5]))

''' min and max value '''
# def func(nums):
#     def rec(nums,i):
#         if i==len(nums)-1: 
#             return nums[i],nums[i]
#         min,max=rec(nums,i+1)
#         min=min if min < nums[i] else nums[i]
#         max=max if max > nums[i] else nums[i]
#         return min,max
#     return rec(nums,0)
# print(func([1,2,3,4,5]))
''' if you dont want output in tuple '''
# def func(nums):
#     def rec(nums,i):
#         if i==len(nums)-1:
#             return nums[i],nums[i]
#         min,max=rec(nums,i+1)
#         min=min if min < nums[i] else nums[i]
#         max=max if max > nums[i] else nums[i]
#         return min,max
#     return rec(nums,0)
# min,max=func([1,2,3,4,5])
# print(min,max)

#find the mid element in the list without len function
# def mid(n):
#     s=n
#     t=n
#     while s and t[1:]:
#         s=s[1:]
#         t=t[2:]
#     return s[0]
        
# print(mid([1,2,3,4,5])) 

# def rec(n,s,f):
#     if f<n-1:
#         return s
#     return rec(n,s+1,f+2)

# print(rec(n,0,0))

l=[7,5,4,2,3]
slow=0
fast=0
while fast<len(l)-1 and fast+1<len(l):
    slow+=1
    fast+=2
print(l[slow])




    

