class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts, result = {}, []
       
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        counts = sorted(counts.items(), key = lambda counts: (counts[1], - counts[0]))
        
        for i, n in counts:
            add = [i] * n
            result.extend(add)
        return result

''' Alternate Approach - hashmap (optimised)

        hashMap = defaultdict(int)

        for num in nums:
            hashMap[num] += 1

        #nums.sort(reverse = True)
        nums.sort(key = lambda x: (hashMap[x], -x))
        return nums

'''
        

''' Alternate Approach - Counter function

from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        nums.sort(key = lambda x: (freq[x], -x))
        return nums

'''
