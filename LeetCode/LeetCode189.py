'''189. Rotate Array'''
'''Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]'''


def rotate(nums, k) :
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums) # In case k > n
    nums[:] = nums[-k:] + nums[:-k]
    return nums
nums = [-1,-100,3,99]
k = 2
print(rotate(nums, k))


'''
def rotate(nums, k):
    n = len(nums)
    k = k % n  # In case k > n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse the entire array
    reverse(0, n - 1)
    
    # Step 2: Reverse first k elements
    reverse(0, k - 1)
    
    # Step 3: Reverse remaining elements
    reverse(k, n - 1)

'''