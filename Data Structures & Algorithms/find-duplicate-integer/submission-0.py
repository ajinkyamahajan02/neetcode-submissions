class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = slow2 = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break
        
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow