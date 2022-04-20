# 173. Binary Search Tree Iterator

# https://leetcode.com/problems/binary-search-tree-iterator/

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root_node=root
        self.current_node=root
        self.stack=[]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.current_node is not None or len(self.stack)!=0

    def next(self):
        """
        :rtype: int
        """
        while self.current_node:
            self.stack.append(self.current_node)
            self.current_node=self.current_node.left
        next=self.stack.pop()
        self.current_node=next.right
        return next.val