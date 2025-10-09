# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # just based on the diagram a level order traversal comes to mind. 
        # we are printing the rightmost element of each level.
        # implementation: 
        # use BFS with queue, for each level we add all child nodes to queue, the last node we visit at each level = rightmost node.
        if not root:
            return [] #edge case
        queue = deque([root]) #push root to queue
        result = [] #final right side view result
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                # if it's the last node of the current level, add to result
                if i==level_size-1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
        