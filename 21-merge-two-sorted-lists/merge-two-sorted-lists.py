# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        temp1 = list1
        temp2 = list2

        while temp1 and temp2:
            if temp1.val > temp2.val:
                current.next = ListNode(temp2.val)
                temp2 = temp2.next  
            elif temp1.val < temp2.val:
                current.next = ListNode(temp1.val)
                temp1 = temp1.next  
            else:
                current.next = ListNode(temp1.val)
                current = current.next
                current.next = ListNode(temp2.val)
                temp1 = temp1.next
                temp2 = temp2.next
            current = current.next

        while temp1:
            current.next = ListNode(temp1.val)
            current = current.next
            temp1 = temp1.next

        while temp2:
            current.next = ListNode(temp2.val)
            current = current.next
            temp2 = temp2.next        

        return dummy.next
