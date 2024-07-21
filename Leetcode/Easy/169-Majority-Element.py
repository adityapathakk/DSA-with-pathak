class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort() Approach 1 (my solution, beat 76.8% time, 87.57% space)
        # n = len(nums) // 2
        # return nums[n]

        # n = len(nums) # Approach 2
        # d = defaultdict(int)

        # for num in nums:
        #     d[num] += 1
        
        # n = n // 2
        # for key, value in d.items():
        #     if value > n:
        #         return key

        # Approach 3 (space optimised) - Moore Voting Algo (if an element is in the majority, i.e.
        # occurs more than half of the times, than the rest of the elements will occur less than half
        # of the time. so, count of majority element should be greater than 0 when count is decremented
        # upon encountering any other element)
        
        count, candidate = 0, 0

        for num in nums:
            if count == 0: candidate = num
            if num == candidate: count += 1
            else: count -= 1

        return candidate

'''

tried a few different approaches :))

'''
