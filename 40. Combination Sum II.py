'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        
        def solve(ind=0,curr_sum=0,curr_list=[]):
            if curr_sum==target:
                if curr_list not in combinations:
                    combinations.append(curr_list[:])
                return
            
            for i in range(ind,len(candidates)):
                if candidates[i]+curr_sum>target:
                    break
                solve(i+1,candidates[i]+curr_sum,curr_list+[candidates[i]])
        solve()
        return combinations