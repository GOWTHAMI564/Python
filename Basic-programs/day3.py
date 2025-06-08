#decimal to binary conversion
# a=8
# rem=""
# while a:
#     rem+=str(a%2)
#     a=a//2
# num=rem[::-1]
# print(num)


#decimal to binary conversion using bitwise &
# a=8                                                                
# rem=""                                                 
# while a:
#     rem+=str(a&1)
#     a=a>>1
# print(rem[::-1])




# 8:1000                  >>  0100  >> 0010 >> 0001 >> 0000
# 1:0001                      0001     0001    0001    0001
# """# & :0000 """                
# """ we consider this"""     0        00      000     0001



#decimal to octal conversion
# a=8
# rem=""
# while a:
#     rem+=str(a%8)
#     a=a//8
# num=rem[::-1]
# print(num)



#binary to decimal conversion
# a="101"
# a= a[::-1]
# dec=0

# for i in range(len(a)):
#     dec+=int(a[i])*(2**i)
# print(dec)

#binary to decimal conversion using bitwise 






#count no of bits a binary number
# a=1
# count=0
# while a:
#     a= a>>1
#     count+=1
# print(count)



#countsetbit
# set bit =1
# a=5
# count=0
# while a:
#     if a &1==1:
#         count+=1
#     a=a>>1

# print(count)

# reset bit=0
# a=8
# count=0
# while a:
#     if a &1==0:
#         count+=1
#     a=a>>1
# 
# print(count)

#first set bit (1) from right
# a=16
# count=0
# while a &1==0:
#     a=a>>1
#     count+=1
# print(count)



#first reset bit (0) from right
# a=2
# count=0
# while a &1==1:
#     a=a>>1
#     count+=1
# print(count)


# first set bit (1) 
# a=7
# temp=a
# count=0
# while a:
#     a=a>>1
#     count+=1
# while temp &1==0:
#     temp=temp>>1
#     count-=1
# print(count)
# '''
# position:123
#          101
#         <---- o/p:3
# position:12345
#          10000
#         <---- o/p:1
# '''



# replacing the ith index from 0-1 or from 1-0
# def clear(a,i):
#     mask=1<<i
#     mask=~mask
#     return a & mask
# print(clear(5,0))


# # set 1 in ith bit
# def fun(a,i):
#     mask=1<<i
#     return a | mask
# print(fun(8,1))


'''
a=1000
i=2 
after left shit
1100 o/p :12

'''


# get the ith position bit
# def fun(a,i):
#     mask=1<<i
#     """return 1 if mask & a>1 else 0"""
    # return int(mask & a >0 )
# print(fun(8,3))


# check if a number is power of 2 
'''
2  00010
4  00100
8  01000
16 10000 
'''

# def fun(a):
#     return a &a-1==0
# print(fun(7))


# remove all even duplicate values does not work for [3,4,3,3,4,9] bcz odd number of duplicates
# a=[3,4,3,4,9]
# res=0
# for i in a:
#     res ^=i
# print(res)   
'''
o/p : 9 

'''



#count the digit in a number using recursion
# n="123"
# count=0
# for i in n:
#     if i.isdigit():
#         count+=1
# print(count)

# def count(n):
#     count=0
#     for i in n:
#         if i.isdigit():
#             count+=1
#     return count
# print(count("123"))


# def func(n):
#     if n==0:return
#     print(n)
#     func(n-1)
        
# print(func(5))


# def fun(n):
#     if n<=1:return 1
#     fun(n-1)
    
#     print(n)
#     fun(n-3)
# print(fun(5))

# '''RecursionError: maximum recursion depth exceeded in comparison'''
# def fun(n):
#     if n==1 and n==0 :return 1
#     fun(n-1)
    
#     print(n)
#     fun(n-3)
# print(fun(5))

# '''RecursionError: maximum recursion depth exceeded in comparison'''
# def fun(n):
#     if n==1 or n==0 :return 1
#     fun(n-1)
    
#     print(n)
#     fun(n-3)
# print(fun(5))



# def fun(n):
#     if n<=1:return 1
#     fun(n-1)
#     return n+fun(n-2)
# print(fun(5))







