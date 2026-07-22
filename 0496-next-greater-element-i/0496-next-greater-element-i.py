class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        hashr={}
        for num in nums2:
            while stack and num>stack[-1]:
                smaller=stack.pop()
                hashr[smaller]=num

            else:
                stack.append(num)

        while stack:
            hashr[stack.pop()] =-1

        ans=[]
        for i in nums1:
            ans.append(hashr[i])

        return ans
