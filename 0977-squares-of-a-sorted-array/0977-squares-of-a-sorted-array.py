class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squares=[]
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
            squares.append(nums[i])

        squares.sort()
        return squares