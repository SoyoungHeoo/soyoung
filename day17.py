# 이진트리

# 이진트리 생성


# 이진트리 순회 : 이진트리 노드 전체를 한 번씩 방문하는 것
# 전위순회, 중위순회, 후위순회


# 전위순회
def preorder(node):
    if node == None:
        return
    print(node.data, end = "->")
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data, end = "->")
    inorder(node.right)


def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end="->")




class TreeNode:
    def __init__(self, data=None):
        self.left = None
        self.data = data
        self.right = None

# 이진탐색트리
# 이진트리중 활용도가 높은 트리로, 데이터 크기를 기준으로 일정 형태로 구성.


if __name__ == "__main__":

    node1 = TreeNode()
    node1.data = 'node1'
    node2 = TreeNode('node2')
    node1.left = node2
    node3 = TreeNode('node3')
    node1.right = node3
    node4 = TreeNode('node4')
    node2.left = node4
    node5 = TreeNode('node5')
    node3.left = node5
    node6 = TreeNode('node6')
    node3.right = node6
    node7 = TreeNode('node7')
    node4.right = node7

    preorder(node1)
    print('')
    inorder(node1)
    print('')
    postorder(node1)