1class Solution(object):
2    def removeDuplicates(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        nums[:]=sorted(set(nums))
8        return len(nums)