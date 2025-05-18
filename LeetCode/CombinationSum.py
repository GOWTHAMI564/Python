def generate(ind,curr,ans,candidates,target):
    if target==0:
        ans.append(curr.copy())
        return
    if target<0:
        return
    if ind==len(candidates):
        return
    curr.append(candidates[ind])
    generate(ind,curr,ans,candidates,target-candidates[ind])
    curr.pop()
    generate(ind+1,curr,ans,candidates,target)
def combinationSum(candidates, target) :
    ind=0
    curr=[]
    ans=[]
    generate(ind,curr,ans,candidates,target)
    return ans
    
candidates = list(map(int,input().split()))
target=int(input())
print(combinationSum(candidates, target))