1class Solution(object):
2    def merge(self, nums1, m, nums2, n):
3        """
4        :type nums1: List[int]
5        :type m: int
6        :type nums2: List[int]
7        :type n: int
8        :rtype: None Do not return anything, modify nums1 in-place instead.
9        """
10
11        list1=nums1[:m]+nums2
12        list1.sort()
13        nums1[:]=list1