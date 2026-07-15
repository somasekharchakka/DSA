1class Solution(object):
2    def generate(self, numRows):
3        """
4        :type numRows: int
5        :rtype: List[List[int]]
6        """
7        triangle=[]
8        for i in range(numRows):
9            row=[1]*(i+1)
10            for j in range(1,i):
11                row[j]=triangle[i-1][j-1]+triangle[i-1][j]
12            triangle.append(row)
13
14        return triangle        