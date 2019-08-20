# Prim Code
# 수학과 관련된 함수나 기호를 쓰기위한 모듈
import math

# Prim's MST Algorithm
def prim(Graph, route, start, compare) : 
    del_list = []    # 삭제할 간선 저장 리스트
    route.append(start)
    
    for i in range(len(compare)) :
        if(compare[i][1] in route and compare[i][0] in route) :
            del_list.append(compare[i])
            
    for i in range(len(del_list)) :
        compare.remove(del_list[i])
        
    for i in range(len(Graph)) :
        if(Graph[i][0] == start) :
            if(Graph[i][1] not in route) :
                compare.append(Graph[i])
        elif(Graph[i][1] == start) :
            if (Graph[i][0] not in route) :
                compare.append(Graph[i])
                
    if len(compare) == 0 :
        return 
    
    temp = math.inf
    for i in range(len(compare)) :
        if(temp > compare[i][2]) :
            temp = compare[i][2]
            edge = compare[i]
    
    if (edge[1] not in route) :
        start = edge[1]
        
    if (edge[1] in route and edge[0] not in route) :
        start = edge[0]
        
    compare.remove(edge)
    
    if(start not in route) :
        prim(Graph, route, start, compare)

# main() 함수
def main() :
    compare = []    # 가중치를 비교하기 위한 리스트
    route = []      # MST 알고리즘을 위한 최적 비용의 간선(즉, 최적의 경로)을 저장하는 리스트
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
              ('F','G',11) ]

    start = input("시작 정점 입력: ")
    prim(Graph, route, start, compare) 
    print("\nPrim's MST Algorithm을 사용한 결과: \n")
    print(route)
    
main()
