import math
import numpy
import copy
INF = math.inf
true = 1         # 방문o
false = 0        # 방문x

# 각 단계 출력 함수
def print_Step(graph) :
    graph = copy.deepcopy(graph)
    print("==================================")
    for i in range(0, len(graph)) :
        for j in range(0, len(graph)) :
            if graph[i][j] == INF :
                graph[i][j] = "*"
    graph = numpy.array(graph)
    print(graph)
    print("==================================")
    
# Floyd's Shortest Path Algorithm 함수
def Floyd(graph) :
    step = 1
    print("<STEP %d>"%step)   
    print_Step(graph)
    step = 2
    for k in range(0, len(graph)) :    # 거쳐가는 노드
        print("<STEP %d>"%step)
        for i in range(0, len(graph)) :    # 출발 노드
            for j in range(0, len(graph)) :    # 도착 노드
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        print_Step(graph)
        step = step + 1
        
# main() 함수
def main() :
    graph = [ [   0,   7, INF,   5, INF, INF, INF ],
              [   7,   0,   8,   9,   7, INF, INF ],
              [ INF,   8,   0, INF,   5, INF, INF ],
              [   5,   9, INF,   0,  15,   6, INF ],
              [ INF,   7,   5,  15,   0,   8,   9 ],
              [ INF, INF, INF,   6,   8,   0,  11 ],
              [ INF, INF, INF, INF,   9,  11,   0 ] ]
    print("< Floyd의 최단 경로 알고리즘 >\n")
    Floyd(graph)    
    
main()
