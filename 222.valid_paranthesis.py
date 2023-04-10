class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        
        for i in range(len(s)):
            if(s[i]=='(' or s[i]=='[' or s[i]=='{'):
                stk.append(s[i])
            else:
                if(len(stk)):
                    tmp = stk.pop()
                    if(s[i]==')' and tmp=='('):
                        pass
                    elif(s[i]==']' and tmp=='['):
                        pass
                    elif(s[i]=='}' and tmp=='{'):
                        pass
                    else:
                        return False
                else:
                    return False
        
        if(len(stk)==0):
            return True
        return False
