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
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        result: list[list[int]] = []

        def visit(root: Optional[TreeNode], depth=0):
            if root is None:
                return

            if len(result) == depth:
                result.append([root.val])
            else:
                result[depth].append(root.val)

            if root.left:
                visit(root.left, depth + 1)
            if root.right:
                visit(root.right, depth + 1)

        visit(root)

        return result
