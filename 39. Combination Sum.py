'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
Each element of candidate is unique.
1 <= target <= 500
'''
class Solution:
    def combinationSum(self, A: List[int], B: int) -> List[List[int]]:
        ans = []
        A.sort()
        
        def solve(ind=0,curr_sum=0,curr_list=[]):
            if curr_sum==B:
                if curr_list not in ans:
                    ans.append(curr_list[:])
                return
            for i in range(ind,len(A)):
                if curr_sum+A[i]>B:
                    break
                solve(i,curr_sum+A[i],curr_list+[A[i]])
        
        solve()
        return ans