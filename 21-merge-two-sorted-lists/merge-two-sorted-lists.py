# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur=list1
        cur2=list2
        l1=[]
        while cur:
            l1.append(cur.val)
            cur=cur.next
        while cur2:
            l1.append(cur2.val)
            cur2=cur2.next
        l1.sort()
        cur = dummy = ListNode(0)
        for e in l1:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next