1class Solution(object):
2    def mySqrt(self, x):
3        """
4        :type x: int
5        :rtype: int
6        """
7        if x<2:
8            return x
9
10        left =1
11        right =x
12        while left <= right:
13            mid =(left+right)//2
14
15            squ = mid * mid
16
17            if squ == x:
18                return mid
19
20            elif squ < x:
21                left =mid+1
22
23            else:
24                right =mid-1
25
26        return right
27                 