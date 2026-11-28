from itertools import batched
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int: 
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first < second:
                diff = first - second
                heapq.heappush(stones, diff)
            if second < first:
                diff = second - first
                heapq.heappush(stones, diff)
        
        stones.append(0)
        return abs(stones[0])

                
        