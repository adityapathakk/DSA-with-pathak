# Link to problem: https://www.geeksforgeeks.org/problems/product-array-puzzle4525/1

class Solution:
    def productExceptSelf(self, nums):
        product, zeros = 1, 0
        
        for i in nums:
            if i == 0:
                zeros += 1
                if zeros >= 2: # if there are more than 2 zeros, product for each index will always be 0
                    product = 0
                    break
                continue
            product *= i # calculating total product of all elements in nums

        P = [product] * len(nums) # array of same size as nums, populated with total product
        
        if zeros < 2: # if there are 2 or more 0s, product array will only have 0s
            for i in range(len(nums)):
                if nums[i] == 0: # if there's only one zero.. 
                    P = [0] * len(nums) # product array will only have 0s.. 
                    P[i] = product # except at nums[i] == 0, where product will be total product without 0
                    break
                P[i] //= nums[i] # integer dividing product with number at that index

        return P # we get products of all elements except self