1class Solution(object):
2    def maxVowels(self, s, k):
3        """
4        :type s: str
5        :type k: int
6        :rtype: int
7        """
8        vowels={"a","e","i","o","u"}
9        count=0
10        for i in range(k):
11            if s[i] in vowels:
12                count+=1
13
14        ans=count
15        for i in range(k,len(s)):
16            if s[i-k] in vowels:
17                count-=1
18
19            if s[i] in vowels:
20                count+=1
21
22            ans=max(ans,count)
23
24        return ans