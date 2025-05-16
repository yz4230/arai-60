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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []
        result = list[list[int]]()
        queue = list[tuple[TreeNode, int]]()
        queue.append((root, 0))
        while queue:
            node, depth = queue.pop(0)
            if len(result) < depth + 1:
                result.append([node.val])
            else:
                if depth % 2 == 0:
                    result[depth].append(node.val)
                else:
                    result[depth].insert(0, node.val)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return result
