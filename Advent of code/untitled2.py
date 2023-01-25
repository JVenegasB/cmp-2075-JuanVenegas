

def isbalanced(root):
    if root is None:
        return 0
    lheight = isbalanced(root.left)
    rheight = isbalanced(root.right)
    if lheight  == False:
        return False
    if rheight == False:
        return False
    if (lheight - rheight == 0):
        return True