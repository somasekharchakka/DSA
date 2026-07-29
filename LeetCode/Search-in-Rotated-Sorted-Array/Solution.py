1class Solution(object):
2    def search(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        left=0
9        right=len(nums)-1
10        while left <= right:
11            mid =(left+right) //2
12
13            if nums[mid] == target:
14                return mid
15            
16            if nums[left] <= nums[mid]:
17                if nums[left] <= target < nums[mid]:
18                    right = mid -1
19                else:
20                    left=mid+1
21        
22            else:
23                if nums[mid] < target <= nums[right]:
24                    left=mid+1
25
26                else:
27                    right=mid-1
28
29        return -1