'''
165. Compare Version Numbers

Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:
If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.

https://leetcode.com/problems/compare-version-numbers/
'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        
        if(len(ver1)==len(ver2)):
            pass
        elif (len(ver1)>len(ver2)):
            ver2+=['0']*(len(ver1)-len(ver2))
        else:
            ver1+=['0']*(len(ver2)-len(ver1))
        
        #print(ver1)
        #print(ver2)
        
        i=0
        j=0
        
        while(i<len(ver1) and j<len(ver2)):
            #Code Optimization no need to strip the leading zeros as converting them to int
            #for comparision will do this itself
            #if(ver1[i].lstrip('0')==''):
            #    ver1[i]='0'
            #if(ver2[j].lstrip('0')==''):
            #    ver2[i]='0'
                
            if(int(ver1[i])==int(ver2[j])):
                pass
            elif(int(ver1[i])>int(ver2[j])):
                return 1
            else:
                return -1
            
            i+=1
            j+=1
        
        return 0
        
        