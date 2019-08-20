# 파일에서 데이터(간선)를 가져와서 리스트에 튜플인자로 저장하는 함수
def open_data(new_list) :
    with open('dfs_data.txt') as dfs_data: 
        data_list = [line.split('\n')[0] for line in dfs_data] # [0]은 0번째 열임
        for data in data_list :
            vert1, vert2 = data.split(',')
            vert1 = vert1.replace("(", "")
            vert2 = vert2.replace(")", "")
            new_list.append((int(vert1), int(vert2)))
            
# DFS(깊이 우선 탐색) 함수
def dfs_stack(g, visited, num) : # (튜플요소형태의 간선 리스트, 탐색 시작 정점)
    visited.sort()
    adj_vert_stack = []
    visited.append(num)
    print(num, end = " ")
    for data in g :
        vert1, vert2 = data
        if visited.count(vert2) == 0 and vert1 == num and vert2 != num : 
            adj_vert_stack.append(vert2)
        if visited.count(vert1) == 0 and vert1 != num and vert2 == num : 
            adj_vert_stack.append(vert1)
    adj_vert_stack.sort() # 리스트 오름차순 정렬
    for i in adj_vert_stack:        
        if visited.count(i) == 0:  # 방문을 안 했다면 해당 노드로 이동
            print("->", end = " ")
            dfs_stack(g, visited, i)
            
# BFS(너비 우선 탐색) 함수
def bfs_queue(g, visited, num) :
   q = []
   visited.append(num)
   q.append(num)
   while(len(g) != len(visited)):
        temp = q.pop(0)
        for data in g :
            vert1, vert2 = data
            if q.count(vert2) == 0 and visited.count(vert2) == 0 and vert1 == temp and vert2 != temp : 
                q.append(vert2)
            if q.count(vert1) == 0 and visited.count(vert1) == 0 and vert1 != temp and vert2 == temp : 
                q.append(vert1)
        # q.sort()                # sort를 추가하면 DFS됨
        visited.append(temp)
        print(temp, end = " ")
        if len(q) != 0 :
            print("->", end = " ")

def main() :
    new_list = []
    open_data(new_list)
    print(new_list)
    temp = new_list
    
    while(True) :
        Q = input("DFS, BFS를 선택(D, B, Q는 종료): ")
        if Q == 'Q' :
            break
        num = int(input('탐색을 시작할 정점을 입력: '))
        visited = []
        if Q == 'D' :
            print("DFS: ", end = "")
            dfs_stack(temp, visited,  num)  # (튜플요소형태의 간선 리스트, 탐색 시작 정점
            print("\n")
            visited.clear()
        if Q == 'B' :
            print("BFS: ", end = "")
            bfs_queue(temp, visited,  num)
            print("\n")
            visited.clear()      
main()
