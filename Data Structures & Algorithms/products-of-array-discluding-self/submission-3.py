class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_counter = 0
        product = 1

        for element in nums:
            if element != 0:
                product *= element
            else:
                zero_counter += 1

        if zero_counter >= 2:
            return [0]*len(nums)

        res = []
        if zero_counter == 1:
            for element in nums:
                if element == 0:
                    res.append(product)
                else:
                    res.append(0)

        if zero_counter == 0:
            for element in nums:
                res.append(int(product/element))

        return res