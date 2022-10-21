# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        queue = []
        answer = []
        queue.append(root)
        while(queue):
            subarray = []
            queueL = len(queue)
            for i in range(queueL):
                element = queue.pop(0)
                if(element):
                    subarray.append(element.val)
                    queue.append(element.left)
                    queue.append(element.right)
            if(subarray):
                answer.append(subarray[-1])
        return answer
                