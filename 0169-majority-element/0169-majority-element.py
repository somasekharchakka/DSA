class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mos={}
        for i in range(len(nums)):
            if nums[i] in mos:
                mos[nums[i]]+=1
            
            else:
                mos[nums[i]]=1

        return max(mos , key=mos.get)

        