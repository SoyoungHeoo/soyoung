
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


def make_linked_list(phone_list):
    global memory, head, current, pre
    print_nodes(head)

    node = Node()
    node.data = phone_list
    memory.append(node)
    if head == None:
        head = node
        return
    if head.data[1] > phone_list[1]:
        node.link = head
        head = node
        return
    # 중간노드 삽입
    current = head # 초기화. 처음부터 다시 수노히
    while current.link != None:
        pre = current
        current = current.link
        if current.data[1] > phone_list[1]:
            pre.link = node
            node.link = current
            return
    # 삽입하는 노드가 가장 큰 경우
    current.link = node


memory = []
head, current, pre = None, None, None
data_array = [["지민", 180], ["정국", 177], ["뷔", 183], ["슈가", 175], ["진", 179]]

## 메인 코드 부분 ##
if __name__ == "__main__" :

    for data in data_array :	# 두 번째 이후 노드
        make_linked_list(data) # 한개씩 데이터르 넣어 알맞는 위치에 배치해줍니다

    print_nodes(head)
    #
    # insert_data("피카츄", "라이츄")
    # print_nodes(head)
    #
    # insert_data("꼬부기", "어니부기")
    # print_nodes(head)
    #
    # delete_nodes("라이츄")
    # print_nodes(head)
    #
    # delete_nodes("피죤스")
    # print_nodes(head)
    #
    # print(find_nodes("파이리"))
    # print(find_nodes("김철수"))
    #
    # print(make_linked_list())