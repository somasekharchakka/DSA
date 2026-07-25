1class Solution(object):
2    def rotate(self, nums, k):
3        n=len(nums)
4        k=k%n
5        nums[:]=nums[-k:]+nums[:-k]
6        