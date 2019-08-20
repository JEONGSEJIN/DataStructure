# Topological Sort 코드
import copy # copy 모듈을 불러옴

# 그래프의 정점의 인접정점을 넣을 클래스
class GraphNode :
    def __init__(self, vertex) :
        self.vertex = vertex    
        self.link = None           
        
# 데이터 여는 함수_파일에서 데이터(간선)를 가져와서 리스트에 튜플인자로 저장하는 함수
def open_data(new_list) :
    with open('topo_sort_data.txt') as topo_sort_data : 
        data_list = [line.split('\n')[0] for line in topo_sort_data]
        for data in data_list :                                         
            vert1, vert2 = data.split(',')                          
            vert1 = vert1.replace("<", "")                              
            vert2 = vert2.replace(">", "")                              
            new_list.append((vert1, vert2))                             

# 인접정점 초기화 함수
def insert_node(node, vertex) :
    new_node = GraphNode(vertex)   
    new_node.link = node           
    return new_node                             
                
# 정점 초기화 함수
def init_node(node) :
    node.vertex = None             
    node.link= None                 
    return node                 
    
# 각 정점들의 인접 정점들을 출력해주는 함수
def print_adj_node(head) :
    for i in head :                                  
        print("\n"+str(i.vertex) + ":", end = " ")   
        while i.link.link != None :                  
            print(i.link.vertex,"->", end = " ")     
            i.link = i.link.link                    

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
                    j.link.vertex -= 1 
                    if j.link.vertex == 0 : 
                        stack.append(j.vertex) 
                        break

def main() :
    edge_list = []                        
    open_data(edge_list)                   
    
    vert_list = []                         
    for i in edge_list :                  
        a, b = i                         
        if vert_list.count(a) == 0 :      
            vert_list.append(a)           
        if vert_list.count(b) == 0 :
            vert_list.append(b)
        vert_list.sort()                
    
    head = []                              
    for i in range(len(vert_list)) :      
        head.append(GraphNode(None))      
    
    count = 0    
    for i in vert_list :               
        head[count].vertex = i           
        count += 1                      
    
    edge = copy.deepcopy(head)       
    edge_num = 0
    in_degree = copy.deepcopy(head)
    degree = 0
    
    # 각 정점에 연결된 정점 연결 리스트를 생성
    head_node = GraphNode(None)         
    head_node2 = GraphNode(None)          
    head_node3 = GraphNode(None)          
    new_node = []
    num_node = []
    num = 0
    
    # 정점 리스트, 간선 리스트
    for i in vert_list :                                 
        for j in edge_list :                             
            a, b = j                                     
            if i == a :                                                               
                head_node = insert_node(head_node, b)    
                edge_num += 1
        new_node.append(copy.deepcopy(head_node))        
        head_node2 = insert_node(head_node2, edge_num)
        head[num].link = new_node[num]                   
        num_node.append(copy.deepcopy(head_node2))
        edge[num].link = num_node[num]
        num += 1                                         
        head_node = init_node(head_node)                 
        head_node2 = init_node(head_node2)
        edge_num = 0
    
    print("각 정점에 연결된 정점 리스트")
    temp = copy.deepcopy(head)             
    temp4 = copy.deepcopy(head)
    print_adj_node(temp)                   

    print("\n\n각 정점의 인접 정점의 개수(간선) 리스트")
    temp2 = copy.deepcopy(edge)
    print_adj_node(temp2)
    
    head_node = GraphNode(None)       
    head_node2 = GraphNode(None)       
    head_node3 = GraphNode(None)      
    new_node = []
    num_node = []        
    num = 0    
    
    # 진입 차수 리스트
    for i in vert_list :                                 
        for j in edge_list :                           
            a, b = j                                     
            if i == b :                                  
                head_node = insert_node(head_node, a)    
                degree += 1
        new_node.append(copy.deepcopy(head_node))        
        head_node3 = insert_node(head_node3, degree)
        head[num].link = new_node[num]                 
        num_node.append(copy.deepcopy(head_node3))
        in_degree[num].link = num_node[num]
        num += 1                                        
        head_node = init_node(head_node)                 # 다시 None으로 초기화 해줌
        head_node3 = init_node(head_node3)
        degree = 0 
    
    print("\n\n각 정점의 진입 차수 리스트")
    temp3 = copy.deepcopy(in_degree)
    print_adj_node(temp3)

    Topo_sort(temp4, in_degree)  # 위상 정렬
    
main()
