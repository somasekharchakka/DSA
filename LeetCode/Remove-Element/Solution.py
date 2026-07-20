1class Solution(object):
2    def removeElement(self, nums, val):
3        """
4        :type nums: List[int]
5        :type val: int
6        :rtype: int
7        """
8        k=0
9        for i in range(len(nums)):
10            if nums[i]!=val:
11                nums[k]=nums[i]
12                k+=1
13        
14        return k