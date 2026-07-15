1class Solution(object):
2    def subarraySum(self, nums, k):
3        count = 0
4        current_sum = 0
5        sums = {0: 1}
6
7        for num in nums:
8            current_sum += num
9
10            need = current_sum - k
11
12            if need in sums:
13                count += sums[need]
14
15            sums[current_sum] = sums.get(current_sum, 0) + 1
16
17        return count