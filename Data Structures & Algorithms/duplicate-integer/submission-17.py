
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_unique = set()

        for element in nums:
            if element in is_unique:
                return True
            else:
                is_unique.add(element)

        return False