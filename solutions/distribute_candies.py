"""
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started 
to gain weight, so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). 
Alice likes her candies very much, and she wants to eat the maximum number of different 
types of candies while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different 
types of candies she can eat if she only eats n / 2 of them.
"""

class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        return min(len(candyType)/2, len(set(candyType)))


# slower

class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        result = list()
        limit = len(candyType)/2
        for candy in candyType:
            if candy not in result:
                result = result + [candy]
                if len(result) == limit:
                    return len(result)
        return len(result)

a = Solution()
print(a.distributeCandies(4))
print('hi')
        
