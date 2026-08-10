class Solution:

    def countNodes(self, root):
        # code here
        if root is None:
            return 0
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
