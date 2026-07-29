1class Solution(object):
2    def singleNonDuplicate(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        n=len(nums)
8        for i in range(0,n-1,2):
9            if nums[i] != nums[i+1]:
10                return nums[i]
11
12        return nums[-1]