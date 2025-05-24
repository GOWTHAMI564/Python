'''
20. Valid Parentheses'''

'''Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false'''
def isValid( s):
    stack=[]
    for ele in s:
        if (ele in "([{"):
            stack.append(ele)
        else:
            if(len(stack)==0):
                return False
            x=stack.pop()
            if(x=="(" and ele==")" or x=="[" and ele=="]" or x=="{" and ele=="}"):
                continue
            else:
                return False
    return len(stack)==0     
s = "()[]{}"
print(isValid( s))