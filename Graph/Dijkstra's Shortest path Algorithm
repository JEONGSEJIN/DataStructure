import math
import numpy
import copy
INF = math.inf
true = 1         # 방문o
false = 0        # 방문x
distance = []    # 시작 정점으로의 최단경로 거리 리스트
found = []       # 방문한 정점 리스트, 방문o:1, 방문x:0
path = []        # 경로 저장 리스트

# 다음 시작 정점을 선택하는 함수
def choose(distance, n, found) :
    minpo = -1
    min_num = INF
    for i in range(0, n) :
        if (distance[i] < min_num) and (not found[i]) :
            min_num = distance[i]
            minpos = i
    return minpos

# 각 단계 출력 함수
def print_step(graph) :
    print("distance: ",end = "")
    for i in range(0, len(graph)) :
        if distance[i] == INF :
            print("*", end = "  ")
        else :
            print("%2d"%distance[i], end = "  ")
            
    print("\nfound:", end = " ")
    for i in range(0, len(graph)) :
        print("%2d"%found[i], end = " ")
    print("\n")     
        
# Dijkstra's Shortest Path Algorithm 함수
def Dijkstra(graph, start) :
    for i in range(0, len(graph)) :
        distance.append(graph[start][i])
        found.append(false)

    found[start] = true
    distance[start] = 0
    
    for i in range(0, len(graph)) :
        path.append([chr(start+65),chr(i+65)])
    
    step = 1
    print(path)    
    for i in range(0, (len(graph)-1)) :
        print("<STEP %d>"%step)
        print_step(graph)
        u = choose(distance, len(graph), found)
        found[u] = true
        for w in range(0, len(graph)) :
            if not found[w] :
                if (distance[u] + graph[u][w]) < (distance[w]) :
                    distance[w] = distance[u] + graph[u][w]
                    path[w].append(chr(u+65))
                    path[w].sort()
        step = step + 1
    
    print("< {}에서 각 정점까지의 최단 거리 >".format(chr(start+65)))
    for i in range(0, len(graph)) :
        print("{0}에서 {1}까지의 경로: ".format(chr(start+65),chr(i+65)),end = "")
        for j in range(0,len(path[i])) :
            print(path[i][j],"-> ", end="")
        print(", 가중치:",distance[i])     

        
# main() 함수
def main() :
    graph = [ [   0,   7, INF,   5, INF, INF, INF ],
              [   7,   0,   8,   9,   7, INF, INF ],
              [ INF,   8,   0, INF,   5, INF, INF ],
              [   5,   9, INF,   0,  15,   6, INF ],
              [ INF,   7,   5,  15,   0,   8,   9 ],
              [ INF, INF, INF,   6,   8,   0,  11 ],
              [ INF, INF, INF, INF,   9,  11,   0 ] ]
    print("< Dijkstra의 최단 경로 알고리즘 >\n")
    start = input("시작할 정점 입력: ")
    start = (ord(start) - 65)
    Dijkstra(graph, start)    
    
main()
