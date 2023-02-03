## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def print_nodes(start) :
	curr = start
	if curr == None :
		return
	print(curr.data, end = ' ')
	while curr.link != None: # 다음노드가 비어있지 않으면
		curr = curr.link # 다음 노드로 이동.
		print(curr.data, end = ' ') # 다음 데이터 찍음
	print()

## 전역 변수 선언 부분 ##
memory = []
head, curr, pre = None, None, None
datas = ["피카츄", "라이츄", "파이리", "꼬부기", "버터풀"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	node = Node()		# 첫 번째 노드
	node.data = datas[0]
	head = node
	memory.append(node)

	for data in datas[1:] :	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		# pre.link = node # 이 부분을 지우면 노드끼리 연결 안됨.
		memory.append(node)

	print_nodes(head)
	print(memory)
