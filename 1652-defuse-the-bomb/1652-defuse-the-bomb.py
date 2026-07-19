class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(code)
        answer=[]        
        if k==0:
            return [0]*n
        for i in range(n):
            total=0
            if k>0:
                for j in range(1,k+1):
                    total +=code[(i+j)%n]

            else:
                for j in range(1,abs(k)+1):
                    total+=code[(i-j)%n]

            answer.append(total)  
        return answer