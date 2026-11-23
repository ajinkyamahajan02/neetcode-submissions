class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, totalSum):
            if i >= len(nums) or totalSum > target:
                return 
            
            if totalSum == target:
                res.append(curr.copy())
                return 

            curr.append(nums[i])
            dfs(i, curr, totalSum+nums[i])

            curr.pop()
            dfs(i+1, curr, totalSum)

        dfs(0, [], 0)
        return res