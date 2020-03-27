# Write a function that returns all permutations of a given list.
# arr = [1,2,3] 
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]


#------------- return method will take O(n!) space--------------------------

def perm(lst):
    if len(lst)==0:
        return []
    elif len(lst)==1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm(xs):
                l.append([x]+p)  
        print('l -> ',l)
        return l
    
for p in perm([1,2,3]):
    print(p)

#------------- yield method will only take O(1) space--------------------------    
    
def perm1(lst):
    if len(lst)==0:
        yield []
    elif len(lst)==1:
        yield lst
    else:
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm1(xs):
                yield [x]+p  
    
for p in perm1([1,2,3]):
    print(p)