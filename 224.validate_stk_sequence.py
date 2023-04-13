class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        idx = 0
        
        for p in pushed:
            stk.append(p)
            while stk and stk[-1]==popped[idx]:
                stk.pop()
                idx+=1
        
        return not stk
