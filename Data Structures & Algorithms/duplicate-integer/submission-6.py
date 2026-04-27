class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_unique = set()
        for ele in nums:
            if ele in is_unique:
                return True
            else:
                is_unique.add(ele)

        return False