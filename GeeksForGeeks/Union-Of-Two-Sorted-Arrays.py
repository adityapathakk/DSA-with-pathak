# Link To Problem: https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=union-of-two-sorted-arrays

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        s = set()
        result = []
        
        for num in arr1:
            s.add(num)
        for num in arr2:
            s.add(num)
        for num in s:
            result.append(num)
        
        result = sorted(result)    
        return result

  ''' Approach

Sets don't contain duplicates. After sorting the set, we get all distinct elements from both arrays.

  '''
