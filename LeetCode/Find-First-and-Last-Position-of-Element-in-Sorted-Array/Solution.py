1class Solution(object):
2    def searchRange(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        left, right = 0,len(nums) - 1
9        first = -1
10
11        while left <= right:
12            mid = (left + right) // 2
13
14            if nums[mid] == target:
15                first = mid
16                right = mid - 1      # Continue searching on the left
17            elif nums[mid] < target:
18                left = mid + 1
19            else:
20                right = mid - 1
21
22        # Find last occurrence
23        left, right = 0, len(nums) - 1
24        last = -1
25
26        while left <= right:
27            mid = (left + right) // 2
28
29            if nums[mid] == target:
30                last = mid
31                left = mid + 1       # Continue searching on the right
32            elif nums[mid] < target:
33                left = mid + 1
34            else:
35                right = mid - 1
36
37        return [first, last]