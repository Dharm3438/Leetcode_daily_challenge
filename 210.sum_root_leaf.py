class Solution:
    def sumNumbers(self, root):
        s, tot_sum = deque([(root, 0)]), 0
        while(len(s)):
            root, cur = s.pop()
            cur = cur * 10 + root.val
            if not root.left and not root.right: 
                tot_sum += cur
            if root.right: 
                s.append((root.right, cur))
            if root.left: 
                s.append((root.left, cur))
        return tot_sum
