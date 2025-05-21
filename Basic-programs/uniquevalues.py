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
unique = [x for x, count in counts.items() if count == 1]
print(unique)  # Output: [3]