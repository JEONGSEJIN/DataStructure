import copy    # copy 모듈을 불러옴

# 그래프의 정점의 인접정점을 넣을 구조체
class NodeType:
    def __init__(self, data):
        self.data = data       # data 인스턴스 멤버
        self.link = None       # link 인스턴스 멤버
        
# 데이터 여는 함수_파일에서 데이터(간선)를 가져와서 리스트에 튜플인자로 저장하는 함수
def open_data(new_list) :     
    with open('dfs_data.txt') as dfs_data:                        # dfs_data.txt파일을 열어서 dfs_data에 저장하고 닫아줌 
        data_list = [line.split('\n')[0] for line in dfs_data]    # dfs_data에 저장된 데이터를 한줄씩 읽으면서
                                                                  # 줄바꿈 기호를 삭제해주면서 다시 data_list에 삽입
                                                                  # [0]은 0번째 열임 
        for data in data_list :                                   # data_list에 있는 요소들을 각각 돌면서
            vert1, vert2 = data.split(',')                        # ','를 기준으로 각각 나눠서 vert1과 vert2에 언패킹
            vert1 = vert1.replace("(", "")                        # vert1에 있는 '('를 지움
            vert2 = vert2.replace(")", "")                        # vert2에 있는 ')'를 지움
            new_list.append((int(vert1), int(vert2)))             # 그리고 vert1과 vert2를 int형으로 둘을 튜플로 묶어서 
                                                                  # new_list에 하나의 요소로 저장
                
# 정점 초기화 함수
def init_node(node):
    node.data = None    # data 인스텀스에 None 삽입
    node.link= None     # link 인스턴스에 None 삽입
    return node         # 하고나서 다시 들어왔던 인자를 다시 리턴해줌

# 인접정점 초기화 함수
def insert_node(node, data):
    new_node = NodeType(data)    # data인자를 가지고 새로운 NodeType클래스 타입으로 바꾸고 new_node에 삽입
    new_node.link = node         # 만들어진 new_node의 link에 node인자 삽입
    return new_node              # 하고나서 다시 new_node 리턴해줌

# 각 정점들의 인접 정점들을 출력해주는 함수
def print_adj_node(head) :
    for i in head:                                 # 인접 정점들을 하나씩 방문하면서
        print(str(i.data) + " :", end = " ")       # 제일 첫번째 정점인 기준 정점 출력
        while(i.link.link != None):                # 정점에 연결된 인접 정점의 연결이 끝날 때까지
            print(i.link.data,"->", end = " ")     # 인접 정점 출력
            i.link = i.link.link                   # 다음 연결된 노드로 이동
        print("\n")

# 깊이 우선 탐색 함수
def dfs(head, visited, start) :
    visited.append(start)                                      # 시작한 정점을 제일 먼저 방문한 리스트에 넣어 준다
    print(start, end = " ")                                    # 시작한 정점 출력
    for i in head:                                             # 인접 정점을 연결해준 리스트들을 하나씩 돌면서
        if i.data == start :                                   # 만약 시작한 정점과 인접 정점이 같으면
            while (i.link.data != None):                       # 다음 인접 정점이 None이 아닐 때까지 while문을 돌면서
                if visited.count(i.link.data) == 0:            # 만약 인접 정점이 방문한 정점 리스트에 하나도 없으면
                    new_start = copy.deepcopy(i.link.data)     # 새로운 변수에 그 인접 정점을 넣어줌
                    i.link = i.link.link                       # 다름 노드로 이동
                    print("->", end = " ")                     # "->" 출력
                    dfs(head, visited, new_start)          # 새로운 변수가 된 인접 정점을 시작 정점으로 해서 다시 깊이 우선 탐색 시작
                else:                                          # 만약 인접 정점이 방문한 정점 리스트에 하나라도 있으면
                    i.link = i.link.link                       # 다음 노드로 이동
            break                                              # 시작한 정점과 인접 정점이 같지 않을 때 break

# main() 함수
def main():    
    data_list = []                    # 데이터를 받을 빈 리스트 생성
    open_data(data_list)              # 텍스트파일에서 데이터를 받아서 저장함
    head_list = []                    # 전체 정점들을 저장해줄 빈 리스트 생성
    for i in data_list :              # 받은 데이터를 하나씩 방문하면서
        a , b = i                     # 튜플로 받은 데이터를 언패킹
        if head_list.count(a) == 0:   # count() : 리스트에서 문자의 개수를 세어줌
            head_list.append(a)       # count()함수를 사용하여 리스트에 없는 요소들을 하나씩 비교하여 저장해줌
        if head_list.count(b) == 0:
            head_list.append(b)
    head = []                         # NodeType클래스 타입의 전체 정점들을 저장해줄 빈 리스트
    for i in range(len(head_list)) :  # 전체 정점의 개수만큼 for문을 돌면서 
        head.append(NodeType(None))   # 각 리스트의 요소들을 모두 NoneType으로 만들어 줌
    count = 0    
    for i in head_list:               # 전체 정점마다 for문을 돌면서
        head[count].data = i          # head 리스트의 각 data부분에 차례대로 전체 정점을 넣어줌
        count = count + 1             # 리스트의 다음 요소로 넘어가기 위해 count를 for문을 돌때마다 하나씩 증가시킴
    head_node = NodeType(None)        # 새로운 를 None으로 초기화 해줌
    new_node = []                     # 빈 리스트 생성
    num = 0
    for i in head_list:                                   # 전체 정점마다 for문을 돌면서
        for j in data_list:                               # 받은 데이터를 하나씩 방문하면서
            a , b = j                                     # 튜플로 받은 데이터를 언패킹
            if i == a :                                   # 전체 정점의 한 원소 == 언패킹한 원소 중 첫 번째 원소
                head_node = insert_node(head_node, b)     # data를 b로하는 node를 하나 생성한 후 head_node에 연결해 줌
            if i == b :                                   # 전체 정점의 한 원소 == 언패킹한 원소 중 두 번째 원소
                head_node = insert_node(head_node, a)     # data를 a로하는 node를 하나 생성한 후 head_node에 연결해 줌
        new_node.append(copy.deepcopy(head_node))         # head_node를 deepcopy해준 뒤 new_node리스트에 넣어줌
        head[num].link = new_node[num]                    # 정점에 인접 정점들을 연결해 줌
        num += 1                                          # 다음 인접 정점들을 서로 연결해줌
        head_node = init_node(head_node)                  # 다시 None으로 초기화 해줌
    print("각 정점에 연결된 정점 리스트")
    temp = copy.deepcopy(head)                            # 인접 정점들을 연결해준 리스트를 다시 temp에 deepcopy해줌
    print_adj_node(temp)                                  # 각 정점들의 인접 정점들을 출력해주는 함수
    visited = []                                          # 방문한 정점을 저장할 리스트
    while(True):                                          # while문을 무한 반복
        temp = copy.deepcopy(head)                        # 인접 정점들을 연결해준 리스트를 다시 temp에 deepcopy해줌
        start = input("깊이 우선 탐색을 시작 할 정점을 입력: ")
        dfs(temp, visited, int(start))                    # 깊이 우선 탐색 
        visited.clear()                                   # 리스트를 비워줌
        print("\n")

main()
