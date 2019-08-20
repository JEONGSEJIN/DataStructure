# Kruskal Code

# 오름차순으로 정렬하기 위한 모듈
from operator import itemgetter

# 정점 형성 클래스
class GraphNode() :
    def __init__(self, data) :
        self.data = data
        self.link = None
        
# 각 정점을 저장하는 함수
def make_vertex(Graph, vertex) :
    for i in range(len(Graph)) :    # 가중치의 오름차순으로 그래프의 간선 정렬
        Graph.sort(key = itemgetter(2))
    
    for i in range(len(Graph)) :    # 그래프의 각 정점을 vertex리스트에 저장
        a = Graph[i][0]
        b = Graph[i][1]
        if a not in vertex :
            vertex.append(a)
        if b not in vertex :
            vertex.append(b)
            
# 각 정점들의 부모 노드를 초기화 해주는 함수
def init(vertex, parent) :
    for i in range(len(parent)) :
        parent[i] = GraphNode(vertex[i])
    for i in range(len(parent)) :
        parent[i].link = GraphNode(vertex[i])

# Union-Find 함수의 Find 함수
def find(parent, vert) :
    index = 0
    for i in range(len(parent)) :
        if parent[i].data == vert :
            index = i
    v = parent[index].link.data
    
    if vert == v :
        return v
    else :
        return find(parent, v)

# Union-Find 함수의 Union 함수
def union(v1, v2, parent) :
    if v1 < v2 :
        for i in range(len(parent)) :
            if parent[i].data == v2 :
                parent[i].link.data = v1
    else :
        for i in range(len(parent)) :
            if parent[i].data == v1 :
                parent[i].link.data = v2

# Kruskal's MST Algorithm
def Kruskal(Graph, parent, route) :                      # (그래프의 간선 리스트, 각 정점의 부모 노드 리스트, 경로 저장 리스트)
    count = 0
    for i in range(len(Graph)) :
        if count != (len(parent) - 1) :
            vert1 = Graph[i][0]
            v1 = find(parent, vert1)
            vert2 = Graph[i][1]
            v2 = find(parent, vert2)
            if v1 != v2 :
                count = count + 1
                route.append(Graph[i])
                union(v1, v2, parent)
    return route

# main() 함수
def main() :
    vertex = []   # 그래프의 각 정점을 저장하는 리스트
    parent = []   # 그래프의 각 정점에 해당하는 부모 노드를 저장하는 리스트
    route = []    # MST 알고리즘을 위한 최적 비용의 간선(즉, 최적의 경로)을 저장하는 리스트
    
    Graph = [ ('A','B',7), 
              ('A','D',5), 
              ('B','C',8), 
              ('B','D',9), 
              ('B','E',7), 
              ('C','E',5),
              ('D','E',15), 
              ('D','F',6), 
              ('E','F',8), 
              ('E','G',9), 
              ('F','G',11)]
    
    make_vertex(Graph, vertex)
    
    parent = [None for i in vertex]
    
    init(vertex, parent)
    
    print("Kruskal's MST Algorithm을 사용한 결과: \n")
    print(Kruskal(Graph, parent, route))
    
main()
