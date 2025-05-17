def twoSum(nums,target):
    d={}
    n=len(nums)
    for a in range(0,n):
        b=target-nums[a]
        if(b in d):
            return [a,d[b]]
        else:
            d[nums[a]]=a
nums=list(map(int,input().split()))
target=int(input())
print(twoSum(nums,target))
