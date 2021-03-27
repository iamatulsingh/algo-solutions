# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.


# Example 1:

#           1
#        /     \ 
#       7       0 
#     /  \
#    7   -8

# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.

# Example 2:

# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2


from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        final_result = 1
        max_sum = root.val

        q = deque()
        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)

        while len(q) > 0:
            count_node = len(q)
            node_sum = 0

            while count_node:
                node = q.popleft()
                node_sum += node.val

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                
                count_node -= 1
            
            if node_sum > max_sum:
                max_sum = node_sum
                final_result += 1

        return final_result



if __name__ == "__main__":
    # [1,7,0,7,-8,null,null]
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(0)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(-8)
    solution = Solution()
    final_result = solution.maxLevelSum(root)
    print(final_result)

    # [989,null,10250,98693,-89388,null,null,null,-32127]
    root1 = TreeNode(989)
    root1.right = TreeNode(10250)
    root1.right.left = TreeNode(98693)
    root1.right.right = TreeNode(-89388)
    root1.right.right.right = TreeNode(-32127)
    print(Solution().maxLevelSum(root1))
