1class Solution(object):
2    def searchInsert(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        left =0
9        right =len(nums)-1
10        while left <= right:
11            mid =(left+right)//2
12
13            if nums[mid] == target:
14                return mid
15            
16            elif nums[mid]<=target:
17                left=mid+1
18
19            else:
20                right =mid-1
21
22        return left