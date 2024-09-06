# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummyNode = ListNode(next = head)
        current = dummyNode

        while current.next:
            if current.next.val in nums:
                current.next = current.next.next
            else:
                current = current.next
            
        return dummyNode.next