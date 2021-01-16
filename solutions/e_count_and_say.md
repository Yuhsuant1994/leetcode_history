# Question
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), 
which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number 
of groups so that each group is a contiguous section all of the same character. 
Then for each group, say the number of characters, then say the character. 
convert the saying into a digit string, replace the counts with a number and concatenate every saying.
```
Example:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
```

# initial solutions:

## S1:
```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1 : return '1'
        result,i='1',2
        for i in range(2,n+1): #start from n=2
            current_result=''
            while result!='':
                j=0
                checkchar=result[j]
                while (result[0]==checkchar):
                    j+=1
                    checkchar= '' if j == len(result) else result[j]
                current_result=current_result+str(j)+result[0]
                result=result[j:] if j < len(result) else ''
            result=current_result
        return result

```


# explanation
* straight forward solution, start with 2nd call since there's result only after first call.
* current result is to continue adding the result of the count number
* then result remove the part that is counted
```
the same idea instead of slicing the result I can use 2 index instead
```

