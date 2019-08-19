# Topological Sort 코드
import copy # copy 모듈을 불러옴

# 그래프의 정점의 인접정점을 넣을 구조체
class GraphNode :
    def __init__(self, vertex) :
        self.vertex = vertex       # data 인스턴스 멤버
        self.link = None           # link 인스턴스 멤버
        
# 데이터 여는 함수_파일에서 데이터(간선)를 가져와서 리스트에 튜플인자로 저장하는 함수
def open_data(new_list) :
    with open('topo_sort_data.txt') as topo_sort_data :            # topo_sort_data.txt파일을 열어서 topo_sort_data에 저장하고 닫아줌
        data_list = [line.split('\n')[0] for line in topo_sort_data]    # dfs_data에 저장된 데이터를 한줄씩 읽으면서
                                                                        # 줄바꿈 기호를 삭제해주면서 다시 data_list에 삽입
                                                                        # [0]은 0번째 열임 
        for data in data_list :                                         # data_list에 있는 요소들을 각각 돌면서
            vert1, vert2 = data.split(',')                              # ','를 기준으로 각각 나눠서 vert1과 vert2에 언패킹
            vert1 = vert1.replace("<", "")                              # vert1에 있는 '<'를 지움
            vert2 = vert2.replace(">", "")                              # vert2에 있는 '>'를 지움
            new_list.append((vert1, vert2))                             # 그리고 vert1과 vert2를 튜플로 묶어서 
                                                                        # new_list에 하나의 요소로 저장

# 인접정점 초기화 함수
def insert_node(node, vertex) :
    new_node = GraphNode(vertex)    # vertex인자를 가지고 새로운 GraphNode클래스 타입으로 바꾸고 new_node에 삽입
    new_node.link = node            # 만들어진 new_node의 link에 node인자 삽입
    return new_node                 # 하고나서 다시 new_node 리턴해줌                
                
# 정점 초기화 함수
def init_node(node) :
    node.vertex = None              # data 인스턴스에 None 삽입
    node.link= None                 # link 인스턴스에 None 삽입
    return node                     # 하고나서 다시 들어왔던 인자를 다시 리턴해줌
    
# 각 정점들의 인접 정점들을 출력해주는 함수
def print_adj_node(head) :
    for i in head :                                  # 정점들을 하나씩 방문하면서
        print("\n"+str(i.vertex) + ":", end = " ")   # 기준 정점 출력
        while i.link.link != None :                  # 정점에 연결된 인접 정점의 연결이 끝날 때까지
            print(i.link.vertex,"->", end = " ")     # 인접 정점 출력
            i.link = i.link.link                     # 다음 연결된 노드(인접 정점)로 이동

# Topological Sort(위상 정렬)해주는 함수            
def Topo_sort(head, in_degree) :
    stack = []
    for i in in_degree :
        if i.link.vertex == 0 :
            stack.append(i.vertex) 
    print("\n\n위상 정렬 순서 :") 
    while stack != [] :
        v = stack.pop()
        print(v, "->",end = ' ')
        vert = []
        for i in head :
            if i.vertex == v :
                while i.link.vertex != None :
                    vert.append(i.link.vertex)
                    i.link = i.link.link
                break
        for j in in_degree :
            for a in vert :
                if j.vertex == a :
                    while j.link.vertex != None :
                        j.link.vertex -= 1
                        if j.link.vertex == 0 :
                            stack.insert(0,j.vertex)
                            j.link = j.link.link
                            break
    
def main() :
    edge_list = []                         # 데이터를 받을 빈 리스트 생성
    open_data(edge_list)                   # 텍스트파일에서 데이터를 받아서 저장함
    
    vert_list = []                         # 전체 정점들을 저장해줄 빈 리스트 생성
    for i in edge_list :                   # 받은 데이터를 하나씩 방문하면서
        a, b = i                           # 튜플로 받은 데이터를 언패킹
        if vert_list.count(a) == 0 :       # count() : 리스트에서 문자의 개수를 세어줌
            vert_list.append(a)            # count()함수를 사용하여 리스트에 없는 요소들만 하나씩 저장해줌
        if vert_list.count(b) == 0 :
            vert_list.append(b)
        vert_list.sort()                   # 오름차순으로 전체 정점 정렬
    
    head = []                              # GraphNode클래스 타입의 전체 정점들을 저장해줄 빈 리스트
    for i in range(len(vert_list)) :       # 전체 정점의 개수만큼 for문을 돌면서 
        head.append(GraphNode(None))       # 각 리스트의 요소들을 모두 GraphNode 객체로 만들고, None으로 초기화
    
    count = 0    
    for i in vert_list :                  # 전체 정점마다 for문을 돌면서
        head[count].vertex = i            # head 리스트의 각 vertex부분에 차례대로 전체 정점을 넣어줌
        count += 1                        # 리스트의 다음 요소로 넘어가기 위해 count를 for문을 돌때마다 하나씩 증가시킴
    
    edge = copy.deepcopy(head)       # 진입 차수(인접 정점)를 연결 리스트로 넣어줄 리스트. 미리하나 만들어 놓음
    edge_num = 0
    in_degree = copy.deepcopy(head)
    degree = 0
    
    # 각 정점에 연결된 정점 연결 리스트를 생성
    head_node = GraphNode(None)           # vertex = None, link = None, 정점 리스트
    head_node2 = GraphNode(None)          # vertex = None, link = None, 간선 리스트
    head_node3 = GraphNode(None)          # vertex = None, link = None, 진입 차수 리스트
    new_node = []
    num_node = []
    num = 0
    
    # 정점 리스트, 간선 리스트
    for i in vert_list :                                 # 정점을 순회
        for j in edge_list :                             # 간선을 순회
            a, b = j                                     # 간선 언패킹
            if i == a :                                  # 방향 그래프의 간선 <A,B> : 정점 A에서 정점 B로 가는 간선
                                                         # '정점 리스트의 요소 == 간선 리스트의 왼쪽 정점' 이면
                head_node = insert_node(head_node, b)    # vertex를 b로하는 node를 하나 생성한 후 head_node에 연결해 줌
                edge_num += 1
        new_node.append(copy.deepcopy(head_node))        # head_node를 깊은 복사해 준 뒤 new_node리스트에 넣어줌
        head_node2 = insert_node(head_node2, edge_num)
        head[num].link = new_node[num]                   # 정점에 인접 정점들을 연결해 줌
        num_node.append(copy.deepcopy(head_node2))
        edge[num].link = num_node[num]
        num += 1                                         # 다음 인접 정점들을 서로 연결해줌
        head_node = init_node(head_node)                 # 다시 None으로 초기화 해줌
        head_node2 = init_node(head_node2)
        edge_num = 0
    
    print("각 정점에 연결된 정점 리스트")
    temp = copy.deepcopy(head)             # 인접 정점들을 연결해준 리스트를 다시 temp에 깊은 복사해 줌
    temp4 = copy.deepcopy(head)
    print_adj_node(temp)                   # 각 정점들의 인접 정점들을 출력해주는 함수

    print("\n\n각 정점의 인접 정점의 개수(간선) 리스트")
    temp2 = copy.deepcopy(edge)
    print_adj_node(temp2)
    
    head_node = GraphNode(None)           # vertex = None, link = None, 정점 리스트
    head_node2 = GraphNode(None)          # vertex = None, link = None, 간선 리스트
    head_node3 = GraphNode(None)          # vertex = None, link = None, 진입 차수 리스트
    new_node = []
    num_node = []        
    num = 0    
    
    # 진입 차수 리스트
    for i in vert_list :                                 # 정점을 순회
        for j in edge_list :                             # 간선을 순회
            a, b = j                                     # 간선 언패킹
            if i == b :                                  # 방향 그래프의 간선 <A,B> : 정점 A에서 정점 B로 가는 간선
                                                         # '정점 리스트의 요소 == 간선 리스트의 왼쪽 정점' 이면
                head_node = insert_node(head_node, a)    # vertex를 b로하는 node를 하나 생성한 후 head_node에 연결해 줌
                degree += 1
        new_node.append(copy.deepcopy(head_node))        # head_node를 깊은 복사해 준 뒤 new_node리스트에 넣어줌
        head_node3 = insert_node(head_node3, degree)
        head[num].link = new_node[num]                   # 정점에 인접 정점들을 연결해 줌
        num_node.append(copy.deepcopy(head_node3))
        in_degree[num].link = num_node[num]
        num += 1                                         # 다음 인접 정점들을 서로 연결해줌
        head_node = init_node(head_node)                 # 다시 None으로 초기화 해줌
        head_node3 = init_node(head_node3)
        degree = 0 
    
    print("\n\n각 정점의 진입 차수 리스트")
    temp3 = copy.deepcopy(in_degree)
    print_adj_node(temp3)

    Topo_sort(temp4, in_degree)  # 위상 정렬
    
main()
