def isValidBST(root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _isValidBST(root, minim, maxim):
            if not root:
                return True
            if minim < root.val < maxim:
                return _isValidBST(root.left, minim, root.val) and _isValidBST(root.right, root.val, maxim)
            else:
                return False
        return _isValidBST(root, float('-inf'), float('inf'))