1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def mergeTwoLists(self, list1, list2):
8        """
9        :type list1: Optional[ListNode]
10        :type list2: Optional[ListNode]
11        :rtype: Optional[ListNode]
12        """
13        dummy=ListNode(0)
14        current=dummy
15        while list1 and list2:
16            if list1.val <= list2.val:
17                current.next=list1
18                list1=list1.next
19
20            else:
21                current.next=list2
22                list2=list2.next
23
24            current=current.next
25
26        if list1:
27            current.next=list1
28
29        if list2:
30            current.next=list2
31
32        return dummy.next