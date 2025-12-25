def itr_pre(root):
    if not root:
        print("NO ROOT")
        return
    st = deque()
    st.append((root))
    res = []
    while st:

        from collections import deque

        class TreeNode:
            def __init__(self, data):
                self.val = data
                self.left = None
                self.right = None

        def itr_traversal(root):
            if not root:
                print("NO ROOT")
                return

            st = deque()
            st.append([root, 1])

            preorder = []
            inorder = []
            postorder = []

            while st:
                node, state = st.pop()
                if state == 1:
                    preorder.append(node.val)
                    st.append((node, 2))
                    if node.left:
                        st.append((node.left, 1))
                elif state == 2:
                    inorder.append(node.val)
                    st.append((node, 3))
                    if node.right:
                        st.append((node.right, 1))
                elif state == 3:
                    postorder.append(node.val)

            print(preorder, inorder, postorder)


root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(10)
root.right.left = TreeNode(7)
root.right.right = TreeNode(12)

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

itr_traversal(root)
