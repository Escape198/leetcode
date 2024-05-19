class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, min_val, max_val):
            if not node:
                return True
            if not (
                min_val < node.val < max_val):
                return False
            return is_valid(node.left, min_val, node.val) and is_valid(node.right, node.val, max_val)


        return is_valid(root, float('-inf'), float('inf'))
