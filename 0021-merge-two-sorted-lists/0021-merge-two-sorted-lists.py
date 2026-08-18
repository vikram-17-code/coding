# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        re = result
        l1 = list1
        l2 = list2
        while(l1 is not None and l2 is not None):
            
            if l1.val <= l2.val:
                re.next = ListNode(l1.val)
                l1 = l1.next
                
                
            else:
    
                re.next = ListNode(l2.val)
                l2 = l2.next
                
            re = re.next
        if(l2 is not None):
            re.next = l2
        if(l1 is not None):
            re.next = l1
        return result.next