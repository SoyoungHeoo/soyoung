class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1 = Graph(4) # 4 X 4 2차원 배열 생성.

G1.graph[0][1] = 1
G1.graph[1][0] = 1
G1.graph[1][2] = 1
G1.graph[1][3] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1
G1.graph[3][1] = 1
G1.graph[3][2] = 1


print(G1.graph)
print("#무방향 그래프#")
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end=' ')
    print()

stack = []
visited_array = []

current = 3 # 시작정점의 인덱스를 current로 지정.
stack.append(current)
visited_array.append(current) # stack, 방문기록에 시작정점의 인덴스 입력.

while True:
    next = None
    if len(stack) == 0:
        break
    else:
        for new_vertex in range(4):
            next = None
            if G1.graph[current][new_vertex] == 1:
                if new_vertex in visited_array:
                    pass # 다음 for 문으로 이동. 이번 차례가 [0][1] 이었다면 [0][2] 순회
                else:
                    next = new_vertex
                    break

        if next is not None: # 다음 연결지점이 있는 경우
            current = next
            stack.append(current)
            visited_array.append(current)
        else: # 다음 연결지점이 없는 경우 -> 돌아가기
            current = stack.pop()

print('그래프 순회 순서')
print(visited_array)
# for i in visited_array:
#     print(i, end = " ")