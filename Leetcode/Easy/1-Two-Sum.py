class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap, length = {}, len(nums)
        for i in range(length):
            complement = target - nums[i]
            if complement in hmap and hmap[complement] != i: # checking if complement already exists
                return [i, hmap[complement]]
            hmap[nums[i]] = i # using hashmap to map each number in list to it's index