class Solution: # part of neetcode 150
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

''' Bucket Sort Approach

count how many times each number occurs.
in freq, append the number to the index which is equal to the amount of times it occurs.
for example: input - [1, 1, 1, 2, 2] ; freq  - [0, 0, 2, 1, 0, 0]

then, starting from end of freq, we add the top k frequent elements.

'''

''' Starting approach

count how many times each number occurs.
then, sort the pairs of 'number : count' in ascending order. return the numbers from the last k indexes.
OR
using max heap, pop the last k pairs from heap and return the numbers.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans

'''
