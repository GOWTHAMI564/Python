def generate(ind,curr_str,ans,O,C,n):
    if O==C and ind==2*n:
        ans.append(curr_str)
        return
    if O>n:
        return
    generate(ind+1,curr_str+"(",ans,O+1,C,n)
    if O>C:
        generate(ind+1,curr_str+")",ans,O,C+1,n)
def generateParenthesis(n):
    ind=0
    curr_str=""
    ans=[]
    O=0
    C=0
    generate(ind,curr_str,ans,O,C,n)
    return ans
n=int(input())
print(generateParenthesis(n))