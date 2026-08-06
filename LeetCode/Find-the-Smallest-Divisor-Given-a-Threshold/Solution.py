1class Solution(object):
2    def smallestDivisor(self, nums, threshold):
3        """
4        :type nums: List[int]
5        :type threshold: int
6        :rtype: int
7        """
8        left = 1
9        right =max(nums)
10        
11        ans = right
12        while left <= right:
13            mid =(left+right)//2
14            total=0
15
16            for i in nums:
17                total += (i + mid - 1) // mid
18
19            if total <=threshold:
20                ans=mid
21                right =mid-1
22
23            else:
24                left=mid+1
25
26        return ans 