nums = [1,2,3,4]
l=[]
for i in range(0,len(nums),2):
    l+=([nums[i+1]]*nums[i])
print(l)