# Given a list of items with values and weights, as well as a max weight, find the
# maximum value you can generate from items where the sum of the weights is less than
# the max.

wt = [5,3,4,2]
value = [60,50,70,30]
max_weight = 5

K = [[0 for _ in range (max_weight + 1) ] for i in range (len(wt)+1)]

for item in range(1,len(wt)+1):
    
    for curr_weight in range (max_weight+1):
        
        if item-1 == 0 and curr_weight==0:
            K[item][curr_weight] = 0
            
        elif curr_weight >= wt[item-1]:
            K[item][curr_weight] = max( K[item-1][curr_weight] , value[item-1] + K[item-1][curr_weight-wt[item-1]] )
            
        else:
            K[item][curr_weight] = K[item-1][curr_weight]
            
print('The max value which can be generated --> ',K[-1][-1])