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




'''unique value'''

# METHOD - 1
list=[1,2,1,2,3]
unique=[]
for i in list:
    if list.count(i)==1:
        unique.append(i)
print(unique) 

'''Using a set to get all distinct values (ignoring duplicates)'''
# METHOD - 2
lst = [1, 2, 1, 2, 3]
unique = list(set(lst))
print(unique)  # Output could be [1, 2, 3], order not guaranteed


''' Using a dictionary or collections.Counter to get elements with count 1'''
# METHOD - 3
from collections import Counter
lst = [1, 2, 1, 2, 3]
counts = Counter(lst) 
print(counts) # Counter({1: 2, 2: 2, 3: 1})
unique = [x for x, count in counts.items() if count == 1]
print(unique)  # Output: [3]



#vowels

'''Method 1: Using a loop and checking vowels'''
word = "HelloWorld"
vowels = "aeiouAEIOU"
count = 0
for char in word:
    if char in vowels:
        count += 1

print(count)  # Output: 3
 
'''Method 2: Using list comprehension with sum()'''
word = "HelloWorld"
vowels = "aeiouAEIOU"
count = sum(1 for char in word if char in vowels)
print(count)  # Output: 3


'''Method 3: Using regular expressions (re module)'''
import re
word = "HelloWorld"
vowels = re.findall(r'[aeiouAEIOU]', word)
## count = (vowels) ## ['e', 'o', 'o']
print(len(vowels))  # Output: 3



'''ASCII value'''
a=input()
b=ord(a)
print(b)

#abcd=10 since a=1,b=2,c=3,d=4 sum=10
s=input()
sum=0
for i in s:
    sum+=ord(i)-96
print(sum)

s = input()
print(sum(ord(i) - 96 for i in s))

def letter_sum(s):
    return sum(ord(i) - 96 for i in s.lower() if i.isalpha())

print(letter_sum(input()))

# to convert vowels to upper case
s="abceiK"
vowels="aeiou"
for char in s:
    if char in vowels:
        print(chr(ord(char)-32),end="")
    else:
        print(char,end="")

#small to capital and capital to small
s="AbceiK"

for char in s:
    if 'a'<=char<='z':
        print(chr(ord(char)-32),end="")
    else:
        print(chr(ord(char)+(32)),end="")

# # print('a'<'b') # True

# print(chr(66)) # B

#input: abcd ,jk output: ajbkCD
s1="abcd"
s2="jk"
i=0
res=""
while i<len(s1) and i<len(s2):
    res+=(s1[i]+s2[i])
    i+=1
while i<len(s1):
    res+=(chr(ord(s1[i])-32))
    i+=1
while i<len(s2):
    res+=(chr(ord(s2[i])-32))
    i+=1
print(res)


#circular substring
s1="abcde"
s2="dea"
double=s1+s1
print(double)
if s2 in double :
    print("True")
else:
    print("False")    


#1a2b3c
n="3a2b5c"
output=""
for i in range(0,len(n),2):
    # count=int(n[i])
    # char=n[i+1]
    # output+=char*count  # or
    output+=int(n[i]) *n[i+1]      
print(output)


#10aa2b12c
n="3aaa2b5c"
output=""
i=0
while i<len(n):
    num_str=""
    while i<len(n) and n[i].isdigit():
        num_str+=n[i]
        i+=1
    count=int(num_str)
    char_str = ""
    while i < len(n) and not n[i].isdigit():
        char_str += n[i]
        i += 1
    output += char_str * count

print(output)



def strict_rle_compress(s):
    result = ''
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += str(count) + s[i - 1]
            count = 1
    result += str(count) + s[-1]  # for the last group  # result += str(count)   : IndexError: string index out of range

    return result

# Example
s = "aaaaaaaaaaaabcccc"
print(strict_rle_compress(s))  # Output: 12a1b4c



def compress_custom(s):
    result = ''
    i = 0
    while i < len(s):
        # Check for repeating pattern "ab"
        if i + 1 < len(s) and s[i:i+2] == "ab":
            count = 0
            while i + 1 < len(s) and s[i:i+2] == "ab":
                count += 1
                i += 2
            result += str(count) + "ab"
        else:
            # Count single character repetitions
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            result += str(count) + s[i]
            i += 1
    return result

# Example
s = "ababababbcccc"
print(compress_custom(s))  # Output: 4ab1b4c



def custom_pattern_compress(s):
    result = ''
    i = 0
    n = len(s)

    while i < n:
        matched = False

        # Try to match 3-character patterns (like 'abc')
        if i + 5 <= n:
            pattern = s[i:i+3]
            count = 0
            j = i
            while j + 3 <= n and s[j:j+3] == pattern:
                count += 1
                j += 3
            if count > 1:
                result += str(count) + pattern
                i += 3 * count
                matched = True

        # If not matched, try 2-character patterns (like 'ab')
        if not matched and i + 3 <= n:
            pattern = s[i:i+2]
            count = 0
            j = i
            while j + 2 <= n and s[j:j+2] == pattern:
                count += 1
                j += 2
            if count > 1:
                result += str(count) + pattern
                i += 2 * count
                matched = True

        # If no pattern, apply normal run-length encoding
        if not matched:
            count = 1
            while i + 1 < n and s[i] == s[i + 1]:
                count += 1
                i += 1
            result += str(count) + s[i]
            i += 1

    return result

# Test Cases
print(custom_pattern_compress("abcabcababbcccc"))  # Output: 2abc2ab1b4c
print(custom_pattern_compress("ababababbcccc"))    # Output: 4ab1b4c








