class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = len(names)
        height_name = OrderedDict()

        for height, name in zip(heights, names):
            height_name[height] = name

        height_name = OrderedDict(sorted(height_name.items(), reverse = True))
        names = list(height_name.values())

        return names


# similar approach to the one above
        # height_to_name = {heights[i]: names[i] for i in range(len(names))}
        # heights.sort()
        # result = []
        
        # for height in reversed(heights):
        #     result.append(height_to_name[height])
        
        # return result
        

# brute force approach - O(N^2) time, O(1) space 
        # for i in range(len(names) - 1):
        #     for j in range(len(names) - 1):
        #         if heights[j] < heights[j + 1]:
        #             heights[j], heights[j + 1] = heights[j + 1], heights[j]
        #             names[j], names[j + 1] = names[j + 1], names[j]        
        
        # return names
