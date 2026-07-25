1class Solution(object):
2    def rotate(self, nums, k):
3        k=k%len(nums)
4        nums[:]=nums[-k:]+nums[:-k]
5      