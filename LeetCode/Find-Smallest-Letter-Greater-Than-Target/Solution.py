1class Solution(object):
2    def nextGreatestLetter(self, letters, target):
3        """
4        :type letters: List[str]
5        :type target: str
6        :rtype: str
7        """
8        left = 0
9        right = len(letters) - 1
10
11        ans = letters[0]
12
13        while left <= right:
14            mid = (left + right) // 2
15
16            if letters[mid] > target:
17                ans = letters[mid]
18                right = mid - 1
19            else:
20                left = mid + 1
21
22        return ans