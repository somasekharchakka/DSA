1class Solution(object):
2    def findMaxAverage(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: float
7        """
8        window_size=sum(nums[:k])
9        avg=window_size/float(k)
10        max_average=avg
11        for i in range(k,len(nums)):
12            window_size=window_size+nums[i]-nums[i-k]
13            avg=window_size/float(k)
14            max_average=max(avg,max_average)
15        
16        return max_average