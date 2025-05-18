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
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        def build(preorder: list[int], inorder: list[int]):
            val = preorder[0]
            preorder.pop(0)
            idx = inorder.index(val)
            inorder_left, inorder_right = inorder[:idx], inorder[idx + 1 :]
            node = TreeNode(val)
            if inorder_left:
                node.left = build(preorder, inorder_left)
            if inorder_right:
                node.right = build(preorder, inorder_right)
            return node

        return build(preorder, inorder)
