# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preorder(self,root,ans):
        if(root==None):
            ans.append(None)
            return 0
        
        ans.append(root.val)
        self.preorder(root.left,ans)
        self.preorder(root.right,ans)
    
    def inorder(self,root,ans):
        if(root==None):
            return 0
        
        self.inorder(root.left,ans)
        ans.append(root.val)
        self.inorder(root.right,ans)


    def postorder(self,root,ans):
        if(root==None):
            return 0
        
        self.postorder(root.left,ans)
        self.postorder(root.right,ans)
        ans.append(root.val)


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_inorder = []
        q_inorder = []

        p_preorder = []
        q_preorder = []

        p_postorder = []
        q_postorder = []
        
        self.inorder(p,p_inorder)
        self.inorder(q,q_inorder)

        self.preorder(p,p_preorder)
        self.preorder(q,q_preorder)

        self.postorder(p,p_postorder)
        self.postorder(q,q_postorder)

        print(p_inorder, q_inorder)
        print(p_preorder, q_preorder)
        print(p_postorder, q_postorder)

        if(p_inorder==q_inorder and p_preorder==q_preorder and p_postorder==q_postorder):
            return True
        
        return False


#Optimized Approach Single Iteration
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(p==None and q==None):
            return True
        
        if(p==None or q==None):
            return False

        if(p.val!=q.val):
            return False

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
