from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.validate(root)

    def validate(
        self,
        root: TreeNode,
        mini: Optional[int] = None,
        maxi: Optional[int] = None,
    ) -> bool:
        if mini is not None and not mini < root.val:
            return False
        if maxi is not None and not root.val < maxi:
            return False
        if root.left and not self.validate(root.left, mini, root.val):
            return False
        if root.right and not self.validate(root.right, root.val, maxi):
            return False
        return True


sol = Solution()
print(sol.isValidBST(TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))))
