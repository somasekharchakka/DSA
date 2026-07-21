# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None or k==0:
            return head

        lenght=1
        tail=head
        while tail.next:
            tail=tail.next
            lenght+=1

        k=k%lenght
        

        if k==0:
            return head
        
        tail.next=head

        steps =lenght-k-1
        newTail=head
        for i in range(steps):
            newTail=newTail.next

        newNode=newTail.next

        newTail.next=None
        
        return newNode
        