
class Node():
    def __init__(self, data=None):
        self.data = data
        self.link = None

def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()

def insert_data(find_d, insert_d):
    global memory, head, current, pre
    if head.data == find_d:  # 첫 번째 노드 삽입
        node = Node()
        node.data = insert_d
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:  # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == find_d:
            node = Node()
            node.data = insert_d
            node.link = current
            pre.link = node
            return

    node = Node()  # 마지막 노드 삽입
    node.data = insert_d
    current.link = node
    node.link = head


def delete_nodes(delete_d):
    global memory, head, current, pre
    if head.data == delete_d: # 첫번째 노드일 때
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del(current)
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == delete_d:
            pre.link = current.link
            del(current)
            return
    # 삭제할 데이터를 못찾는 경우 함수 종료
    print("삭제할 노드를 찾지 못함")
    
    
def find_nodes(find_data):
    global memory, head, current, pre
    current = head
    if current.data == find_data:
        return current
    while current.link != head:
        current = current.link
        if current.data == find_data:
            return current
    return Node() # 빈 노드 반환


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

def is_find(find_data):
    '''
    연결리스트 안에서 원소 존재 여부 판정 함수
    :param find_data: 찾고자 하는 원소. str
    :return: 원소 존재시 True, 아니면 False
    '''
    global memory, head, current, pre
    current = head
    if current.data == find_data:
        return True
    while current.link != head:
        current = current.link
        if current.data == find_data:
            return True
    return False # 빈 노드 반환



memory = []
head, current, pre = None, None, None
# data_array = [["지민", 180], ["정국", 177], ["뷔", 183], ["슈가", 175], ["진", 179]]
data_array = ['피카츄', '파이리', '어니부기', '꼬부기', '버터풀']

## 메인 코드 부분 ##
if __name__ == "__main__" :

    node = Node()
    node.data = data_array[0]
    head = node
    node.link = head

    for data in data_array[1:] :	# 두 번째 이후 노드
        # make_linked_list(data) # 한개씩 데이터르 넣어 알맞는 위치에 배치해줍니다
        pre = node
        node = Node(data)
        pre.link = node
        node.link = head

    print(is_find("꼬부기"))
    print(is_find("피카츄"))
    print(is_find("김인하"))

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