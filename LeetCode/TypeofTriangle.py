def typeofTriangle(nums):
    nums.sort()
    if nums[2]>=nums[1]+nums[2]:
        return "none"
    if nums[0]==nums[2]:
        return "equilateral"
    if nums[0]==nums[1] or nums[1]==nums[2]:
        return "isosceles"
    return "scalene" 
nums=list(map(int,input().split()))
print(typeofTriangle(nums))