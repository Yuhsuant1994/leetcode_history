"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        num_strs=len(strs)
        prefix=''
        ichar=0       
        if (len(strs)>0) & ('' not in strs):
            min_strlen=len(min(strs,key=len))
            while (ichar <= 200)&(ichar<min_strlen):
                current_char=strs[0][ichar]
                for index in range(num_strs):
                    if strs[index][ichar]!= current_char:
                        return strs[0][:ichar]
                    if index+1==num_strs:
                        prefix=prefix+current_char
                ichar+=1
        return prefix

        
#this option looks smarter cleaner but slower, as all would compute all 
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        num_strs=len(strs)
        prefix=''
        ichar=0       
        if (len(strs)>0) & ('' not in strs):
            min_strlen=len(min(strs,key=len))
            while (ichar <= 200)&(ichar<min_strlen):
                current_char=strs[0][ichar]
                if all(string[ichar]==current_char for string in strs):
                    prefix+=current_char
                else:
                    return strs[0][:ichar]
                ichar+=1
        return prefix


    