1class Solution(object):
2    def findPeakElement(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        n=len(nums)
8        if n == 1 or nums[0]>nums[1]:
9            return 0
10
11        for i in range(1,n-1):
12            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
13                return i
14
15        return n-1