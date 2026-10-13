class Solution:
    def search(self, nums: List[int], target: int) -> int:
        head = 0
        tail = len(nums) - 1

        while head < tail:
            mid = int((head+ tail) / 2)

            if nums[mid] > target > nums[tail]:
                tail = mid
            elif nums[mid] > target < nums[tail]:
                head = mid + 1
            elif nums[mid] < target > nums[tail]:
                tail = mid
            elif nums[mid] < target < nums[tail]:
                head = mid + 1
            if nums[mid] == target:
                return mid

        return -1
