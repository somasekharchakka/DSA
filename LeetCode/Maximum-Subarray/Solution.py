1class Solution(object):
2    def maxSubArray(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        current_sum=nums[0]
8        max_sum=nums[0]
9        for i in range(1,len(nums)):
10            current_sum=max(nums[i],current_sum+nums[i])
11            max_sum=max(current_sum,max_sum)
12
13        return max_sum