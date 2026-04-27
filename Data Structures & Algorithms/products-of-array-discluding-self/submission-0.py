class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_counter = 0
        product = 1

        for num in nums:
            if num == 0:
                zero_counter = zero_counter +1
                zero_index = nums.index(0) 
                continue
            product = product*num

        if zero_counter > 1:
            return [0]*len(nums)

        res_lst = []

        for element in nums:
            if element == 0:
                res_lst = []
                res_lst.extend([0]*len(nums))
                res_lst[zero_index] = product
                return res_lst
            else:
                val = int(product/element)
                res_lst.append(val)
        return res_lst

        