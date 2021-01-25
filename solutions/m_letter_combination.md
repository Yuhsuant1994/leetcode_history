# Question
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
 

Example 1:
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

# initial solutions:

## S1: time limit exceeded
```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        number_map={'2':'abc','3':'def','4':'ghi',
                   '5':'jkl','6':'mno',
                   '7':'pqrs','8':'tuv','9':'wxyz'}
        if digits=='': return list()
        current_result=['']
        for digit in digits:
            new_result=[]
            for x in current_result:
                for y in number_map[digit]:
                    new_result+=[x+y]
            current_result=new_result
        return current_result

```

