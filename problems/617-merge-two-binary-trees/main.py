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
    def mergeTrees(
        self,
        root1: Optional[TreeNode],
        root2: Optional[TreeNode],
    ) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None

        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0

        return TreeNode(
            v1 + v2,
            self.mergeTrees(
                root1.left if root1 else None,
                root2.left if root2 else None,
            ),
            self.mergeTrees(
                root1.right if root1 else None,
                root2.right if root2 else None,
            ),
        )
