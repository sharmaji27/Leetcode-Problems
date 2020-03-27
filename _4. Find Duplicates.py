# Given an array of integers where each value 1 <= x <= len(array), write a
# function that finds all the duplicates in the array.

a = [3,3,3,3]
result = set()

for i in a:
    if a[abs(i)-1] > 0:
        a[abs(i)-1] *= -1
    
    else:
        result.add(abs(i))

print(list(result))