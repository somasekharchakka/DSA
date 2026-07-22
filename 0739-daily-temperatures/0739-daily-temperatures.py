class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack=[]
        num=len(temperatures)
        array=[0]*num
        for i in range(num):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev=stack.pop()
                array[prev]=i-prev
            
            stack.append(i)
        
        return array
        
        
