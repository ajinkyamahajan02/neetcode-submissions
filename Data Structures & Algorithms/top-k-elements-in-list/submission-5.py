from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = Counter()
        for element in nums:
            res[element] = res.get(element, 0) + 1

        return [item[0] for item in res.most_common(k)]
