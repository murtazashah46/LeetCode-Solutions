# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def findSum(node,target_sum,path,array):
    if(node == None):
        return  
    path.append(node.val)
    if(node.val == target_sum and node.left == None and node.right == None):
        array.append(list(path))
    
    findSum(node.left,target_sum-node.val,path,array)
    
    findSum(node.right,target_sum-node.val,path,array)
    path.pop()
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if(root == None):
            return []
        answer = []
        findSum(root,targetSum,[],answer)
        return answer
