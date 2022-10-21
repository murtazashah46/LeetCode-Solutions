# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def Sum(node,s):
    if(node == None):
        return 0
    s = s*10 + node.val
    if(node.left == None and node.right == None):
        return s
    return Sum(node.left,s) + Sum(node.right,s)

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if(root == None):
            return 0
        return Sum(root,0) 
        