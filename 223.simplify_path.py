class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        res = '/'
        stk = []
        
        for val in paths:
            if(len(stk) and val=='..'):
                stk.pop()
            if(val!='' and val!='..' and val!='.'):
                stk.append(val)
        
        if(len(stk)==0):
            return '/'
        
        for val in stk:
            res+=val
            res+='/'
        
        res = res[:-1]
        
        return res
