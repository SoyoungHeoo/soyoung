from collections import deque

class Graph() :
	def __init__ (self, size) :
		self.SIZE = size
		self.graph = [ [0 for _ in range(size)] for _ in range(size) ]

## 전역 변수 선언 부분 ##
G1 = None
dequeue_ = deque([])
visit_array = []		# 방문한 정점

## 메인 코드 부분 ##
G1 = Graph(9)

A, B, C, D, E, F, G, H, I = 0, 1, 2, 3, 4, 5, 6, 7, 8

G1.graph[A][D] = 1; G1.graph[A][B] = 1; G1.graph[A][C] = 1; G1.graph[A][D] = 1
G1.graph[B][A] = 1; G1.graph[B][C] = 1; G1.graph[B][D] = 1
G1.graph[C][A] = 1; G1.graph[C][B] = 1; G1.graph[C][D] = 1; G1.graph[C][E] = 1; G1.graph[C][F] = 1
G1.graph[D][B] = 1; G1.graph[D][C] = 1
G1.graph[E][A] = 1; G1.graph[E][C] = 1; G1.graph[E][G] = 1; G1.graph[E][H] = 1
G1.graph[F][C] = 1 # f
G1.graph[G][E] = 1; G1.graph[G][I] = 1# g
G1.graph[H][E] = 1; G1.graph[H][I] = 1
G1.graph[I][G] = 1; G1.graph[I][H] = 1

print('## G1 무방향 그래프 ##')
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
print('  ', end=' ')
for i in alphabet:
	print(i, end=' ')
print()
for row in range(9) :
	print(alphabet[row], end= '  ')
	for col in range(9) :
		print(G1.graph[row][col], end=' ')
	print()

if __name__ == "__main__":
	current = 0  # 시작 정점 A
	dequeue_.append(current)  # push
	visit_array.append(current)  # push

	while (len(dequeue_) != 0):  # stack = 0 이 아니면 아직 순회할 것이 남았다는 뜻
		next = None
		for vertex in range(9):
			if G1.graph[current][vertex] == 1:
				if vertex in visit_array:  # 방문한 적이 있는 정점이면 탈락
					pass
				else:  # 방문한 적이 없으면 다음 정점으로 지정
					next = vertex
					break

		if next != None:  # 다음에 방문할 정점이 있는 경우
			dequeue_.append(current)
			current = next
			visit_array.append(current)
		else:  # 다음에 방문할 정점이 없는 경우
			current = dequeue_.popleft()
		print(dequeue_)

	print('방문 순서 -->', end='')
	for i in visit_array:
		print(chr(ord('A') + i), end='   ')

