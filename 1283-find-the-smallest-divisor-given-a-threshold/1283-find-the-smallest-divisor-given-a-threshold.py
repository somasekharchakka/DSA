class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left = 1
        right =max(nums)
        
        ans = right
        while left <= right:
            mid =(left+right)//2
            total=0

            for i in nums:
                total += (i + mid - 1) // mid

            if total <=threshold:
                ans=mid
                right =mid-1

            else:
                left=mid+1

        return ans 