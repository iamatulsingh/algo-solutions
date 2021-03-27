# Given a Binary Tree, find the vertical sum of the nodes 
# that are in the same vertical line. 
# Print all sums through different vertical lines.

# Example:

#           1
#        /     \ 
#       3       7 
#     /  \     / \
#    6    8   2   9

# Output: {0: 9, -1: 3, -2: 6, 1: 7, 2: 9}



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.track = {0: root.val}
        if root.left is not None:
            self.rec_check(root.left, -1)
        if root.right is not None:
            self.rec_check(root.right, 1)
        return self.track

    def rec_check(self, root, ind):
        if self.track.get(ind, ""):
            self.track[ind] += root.val
        else:
            self.track[ind] = root.val
        if root.left is not None:
            self.rec_check(root.left, ind - 1)
        if root.right is not None:
            self.rec_check(root.right, ind + 1)
        


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    solution = Solution()
    final_result = solution.verticalSum(root)
    print(final_result)
