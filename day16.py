
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()



def insert_data(find, insert):
    global memory, head, current, pre
    if head.data == find:  # 첫 번째 노드 삽입
        node = Node()
        node.data = insert
        node.link = head
        head = node
        return

    current = head
    while current.link != None:  # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == find:
            node = Node()
            node.data = insert
            node.link = current
            pre.link = node
            return

    node = Node()  # 마지막 노드 삽입
    node.data = insert
    current.link = node


def delete_nodes(delete_d):
    global memory, head, current, pre
    if head.data == delete_d:
        current = head
        head = head.link
        del current
        print("첫 노드가 삭제됨")
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == delete_d:
            pre.link = current.link
            del current
            print("중간노드가 삭제됨")
            return
    # 삭제할 데이터를 못찾는 경우 함수 종료
    print("삭제할 노드를 찾지 못함")
    
    
def find_nodes(find_data):
    global memory, head, current, pre
    current = head
    if current.data == find_data:
        return current
    while current.link != None:
        current = current.link
        if current.data == find_data:
            return current.data
    return "Nameless"


memory = []
head, current, pre = None, None, None
dataArray = ["피카츄", "잠만보", "파이리", "꼬부기", "버터풀"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

    node = Node()		# 첫 번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:] :	# 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    print_nodes(head)

    insert_data("피카츄", "라이츄")
    print_nodes(head)

    insert_data("꼬부기", "어니부기")
    print_nodes(head)

    delete_nodes("라이츄")
    print_nodes(head)

    delete_nodes("피죤스")
    print_nodes(head)

    print(find_nodes("파이리"))
    print(find_nodes("김철수"))
