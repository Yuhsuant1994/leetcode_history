class Solution(object):        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #fibonacci sequence
        a,b=0,1 #result=a+b
        for i in range(n):
            a,b=b,a+b
        return b