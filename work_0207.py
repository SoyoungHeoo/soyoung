# 8장 응용예제 1 - 편의점에서 판매된 물건 목록 출력하기
import random

# 노드 만들기
class Node:
    def __init__(self, data = None):
        self.data = data
        self.right = None
        self.left = None

# 전역변수
memory = list()
items = ['캔커피', '도시락', '삼각김밥', '츄파츕스', '코카콜라']
sold_items = [random.choice(items) for _ in range(20)]

# 메인함수
if __name__ == "__main__":
    # root
    node = Node()
    node.data = sold_items[0]
    root = node
    for item in sold_items[1:]:
        node = Node(item)
        current = root
        while True:
            if item == current.data:
                break
            if item < current.data :
                if current.left == None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right == None:
                    current.right = node
                    break
                current = current.right


    def preorder(node):
        if node == None:
            return
        print(node.data, end = ' ')
        preorder(node.left)
        preorder(node.right)

    print(sold_items)
    preorder(root)

