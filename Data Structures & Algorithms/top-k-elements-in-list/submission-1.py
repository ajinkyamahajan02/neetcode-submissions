from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_c = Counter(nums)
        elements = nums_c.most_common(k)

        lst = []
        for element in elements:
            lst.append(element[0])
        print(elements[0])

        return lst
        