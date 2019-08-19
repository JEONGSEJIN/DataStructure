class TreeNode :                                         # 노드의 기본 틀이 되어 주는 클래스
    def __init__(self, letter, freq_num):                # 클래스의 생성자
        self.letter = letter                             # 글자를 저장하는 인스턴스 멤버
        self.freq_num = freq_num                         # 빈도수를 저장하는 인스턴스 멤버
        self.edge = None                                 # Huffman Code의 비트를 저장할 인스턴스 멤버
        self.left = None                                 # 왼쪽 노드를 가리킬 인스턴스 멤버
        self.right = None                                # 오른쪽 노드르 가리킬 인스턴스 멤버
        
def create_node(let, num) :                              # 노드를 생성하는 함수
    node = TreeNode(let, num)                            # TreeNode 클래스 타입의 node객체를 하나 생성해 준다.
    return node                                          # 만들어진 노드를 return 

def create_tree(node1, node2) :                          # 트리를 만드는 함수
    freq_add = node1.freq_num + node2.freq_num           # freq_add 변수 = 함수의 인자로 들어온 노드의 빈도수의 합
    tree = TreeNode(None, freq_add)                      # TreeNode 클래스 타입의 tree객체를 하나 생성해 준다.(루트 노드 생성)
    if node1.freq_num <= node2.freq_num :                # 첫번째 노드의 빈도수 <= 두번째 노드의 빈도수이면
        tree.left = node1                                # 첫번째 노드를 트리의 루트노드의 왼쪽에 연결
        tree.right = node2                               # 두번째 노드를 트리의 루트노드의오른쪽에 연결
        tree.left.edge = '1'                             # 왼쪽 노드의 edge에 1을 문자로 저장
        tree.right.edge = '0'                            # 오른쪽 노드의 edge에 0을 문자로 저장
        
    else :                                               # 첫번째 인자의 빈도수 > 두번째 인자의 빈도수이면
        tree.left = node2                                # 두번째 노드를 트리의 루트노드의 왼쪽에 연결
        tree.right = node1                               # 첫번째 노드를 트리의 루트노드의 오른쪽에 연결
        tree.left.edge = '1'                             # 왼쪽 노드의 edge에 1을 문자로 저장
        tree.right.edge = '0'                            # 오른쪽 노드의 edge에 0을 문자로 저장
    return tree                                          # 만들어진 트리를 return 

def replace_index(list, index, key) :                    # 리스트 안의 index번째 원소를 삭제하고 key원소로 바꾸는 함수
    list.remove(list[index])                             # 리스트에서 index번째의 값을 삭제
    list.insert(index, key)                              # 리스트의 index번째에 key저장
    if key == " " :                                      # 만약, 리스트에 넣은 key값이 " "(공백)이면
        list.remove(key)                                 # 리스트의 해당 key값을 삭제
    return list                                          # 수정된 리스트를 return 
        
def print_code(root, code_list) :                        # Huffman Code를 출력하는 함수{함수인자: (트리의 루트노드, 코드 리스트)}
    code_list.append(root.edge)                          # 코드 리스트에 루트노드의 edge값을 넣음
                                                         # but, 루트 노드의 edge값은 Huffman Code에 포함되면 안되므로 
                                                         #      다음의 실행을 진행해 준다.
    if (root.left != None) :                             # 루트의 왼쪽 노드가 None값이 아니면 
        print_code(root.left, code_list)                 # 다시 print_code()함수로 가서 코드 출력 실행
            
    if (root.right != None) :                            # 루트의 오른쪽 노드가 None값이 아니면
        print_code(root.right, code_list)                # 다시 print_code()함수로 가서 코드 출력 실행
        
    if ((root.left == None) and (root.right == None)) :  # 루트의 왼쪽 노드와 오른쪽 노드 둘다 None값이 아니면 (즉,단말노드이면)
        if code_list[0] == None :                        # 코드 리스트의 0번째 인덱스가 None이면
            replace_index(code_list, 0, "")              # 코드 리스트의 0번째 원소를 삭제하고 ""원소로 바꿈
        print(root.letter + " :", end = " ")             # 출력하려는 코드의 글자를 출력
        for i in range(len(code_list)) :                 # 코드 리스트의 길이만큼 for문을 돈다
            print(code_list[i], end = "")                # 코드 리스트에 있는 코드를 하나씩 출력한다
        code_list.pop()                                  # 코드 리스트의 제일 마지막 값을 pop() (출력과 동시에 삭제)
        print("\n")                                      # 줄바꿈
    
    if ((root.left != None) and (root.right != None) and (root.letter == None)) : # 단말노드이면서, 글자가 없는 노드이면
        list = []                                        # 새로운 빈 리스트를 하나 선언
        if code_list == list :                           # 함수 인자로 들어온 리스트가 빈 리스트이면
            code_list.pop()                              # 함수로 들어온 리스트의 제일 마지막 값을 pop() (출력과 동시에 삭제)
             
def main() :                                             # main()함수
    tree = TreeNode(None, None)                          # 루트 노드 생성
    
    n1 = create_node("a", 1)                             # 자손 노드를 각각 생성 ("글자", 빈도수)
    n2 = create_node("b", 1) 
    n3 = create_node("c", 2)
    n4 = create_node("d", 3)
    n5 = create_node("e", 5)
    n6 = create_node("f", 8)
    n7 = create_node("g", 13)
    n8 = create_node("h", 21)
    
    tree = create_tree(n1, n2)                           # 만들어진 자손들을 가지고 트리 생성
    tree = create_tree(n3, tree) 
    tree = create_tree(n4, tree) 
    tree = create_tree(n5, tree) 
    tree = create_tree(n6, tree) 
    tree = create_tree(n7, tree) 
    tree = create_tree(n8, tree) 
     
    list = []                                            # dege의 값들을 저장하기 위해 리스트를 하나 생성
    print_code(tree, list)                               # 트리의 edge값을 저장한 리스트를 가지고 Huffman Codes 출력
    
main()                                                   # main()함수 실행  
