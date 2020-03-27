# Given an unsorted array, find the length of the longest sequence of
# consecutive numbers in the array.

a = [5,5,3,1]
max_len = 0

Hashset = set()

for i in a:
    Hashset.add(i)
    
for j in Hashset:
    if j-1 in Hashset:
        continue
    curr_len = 1
    while j+1 in Hashset:
        j+=1
        curr_len+=1
        
    if curr_len>max_len:
       max_len = curr_len
       
print(max_len)