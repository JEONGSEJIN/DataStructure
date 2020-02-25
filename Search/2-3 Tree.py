# 트리를 연결 리스트로 표현
class TreeNode :
    def __init__(self, key1, key2, data_num) :
        self.key1 = key1    # ( key1 < key2 으로 봄)
        self.key2 = key2
        self.data_num = data_num
        self.left = None
        self.mid = None
        self.right = None

# 노드를 만드는 함수
def create_node(key1) :
    node = TreeNode(key1, None, 1)    # key1으로 루트 노드에서 data에 접근
    return node
    
# 2-3 tree 만드는 함수
def create_tree(root, data) :
    if root.data_num == 0 :               # 루트 노드 밑에 값이 하나도 없다(트리 공백 상태)
        return create_node(data)          # 새로운 노드 반환
    else :
        if root.data_num == 1 :               # 루트 노드 밑에 값이 적어도 하나라도 있다
            if data < root.key1 :             # 루트 노드 밑에 값이 한 개 있다
                #if root.left.data_num == 2 :
                    # 써줭 세진아
                if (root.left != None) and (root.right != None) :   # 이거 또 필요한 곳에 써주기!!
                    root.left.key2 = data
                    root.left.data_num += 1
                else : 
                    root.key2 = root.key1
                    root.ket1 = data
                    root.data_num += 1
                return root
    
            if data > root.key1 :
                if (root.left != None) and (root.right != None) :   # 이거 또 필요한 곳에 써주기!!
                    if root.right.data_num == 2 :
                        if (root.right.left != None) and (root.right.mid != None) and (root.right.right != None) :
                            root.right.right.key2 = data
                            root.right.right.data_num +=1 
                        else :
                            root.key2 = root.right.key2
                            root.data_num += 1
                            root.mid = create_node(root.right.key1)
                            root.right.key1 = data
                            root.right.key2 = None
                            root.right.data_num -= 1
                    else :
                        if data < root.right.key1 :
                            root.right.left.key2 = data
                        if root.right.key1 < data :
                            #if data < root.right.right.key1 :
                            #    root.right.right.key2 = root.right.right.key1
                            #    root.right.right.key1 = data
                            if (root.right.left != None) and (root.right.right != None) :
                                if root.right.right.key1 < data :
                                    #if root.right.right.key1 < data and root.right.right.key2 < data
                                    # 요거 참고행
                                    if root.right.right.data_num == 2 :
                                        root.right.key2 = root.right.right.key2
                                        root.right.data_num += 1
                                        root.right.mid = create_node(root.right.right.key1)
                                        root.right.right.key1 = data
                                        root.right.right.key2 = None
                                        root.right.right.data_num -= 1
                                    else :
                                        root.right.right.key2 = data
                                        root.right.right.data_num += 1

                            else :          
                                root.right.key2 = data
                                root.right.data_num += 1
                #if root.right.data_num == 2 :
                #    root.mid = create_node(root.right.key1)
                #    root.key2 = root.right.key2
                #    root.right.key1 = data
                #    root.right.key2 = None
                else :
                    root.key2 = data
                    root.data_num += 1
                return root
                
        if root.data_num == 2 :               # 루트 노드 밑에 값이 두 개 있다
            if data < root.key1 :
                root.left = create_node(data)
                root.right = create_node(root.key2)
                root.key2 = None
                root.data_num -= 1
                return root
            
            if root.key2 < data :
                if (root.left != None) and (root.mid != None) and (root.right != None) :   # 이거 또 필요한 곳에 써주기!!
                    if root.right.data_num == 2 : # 뭘해도 root.key1는 이제 root.key2로 바뀜
                        #if data < root.right.key1 : # root.right.key1가 위로 올라감
                            #root.left = 
                            #root.key1 = root.key2
                            
                        if root.right.key2 < data : # root.right.key2가 위로 올라감
                            root.left.left = create_node(root.left.key1)
                            root.left.right = create_node(root.mid.key1)
                            root.mid = None
                            root.left.key1 = root.key1
                            root.key1 = root.key2
                            root.key2 = None
                            root.data_num -= 1

                            root.right.left = create_node(root.right.key1)
                            root.right.key1 = root.right.key2
                            root.right.right = create_node(data)
                            root.right.key2 = None
                            root.right.data_num -= 1

                        #if (root.right.key1 < data) and (data < root.right.key2) : # data가 위로 올라감
                        #    root.
                    else :
                        if data < root.right.key1 :
                            root.right.key2 = root.right.key1
                            root.right.key1 = data
                            root.right.data_num +=1 
                        else :
                            root.right.key2 = data
                            root.right.data_num +=1 

                else :    
                    root.left = create_node(root.key1)
                    root.right = create_node(data)
                    root.key1 = root.key2
                    root.key2 = None
                    root.data_num -= 1
                return root

            if (root.key1 < data) and (data < root.key2) :
                root.left = create_node(root.key1)
                root.right = create_node(root.key2)
                root.key1 = data
                root.key2 = None
                root.data_num -= 1
                return root    
            
# 전위 순회 연산(루트->왼->중간->오) 함수
def preorder_trav(root) :
    if root != None :
        if (root.key1 != None) or (root.key2 != None) :
            if root.key1 != None :
                print(root.key1)
            if root.key2 != None :
                print(root.key2)
            preorder_trav(root.left)
            preorder_trav(root.mid)
            preorder_trav(root.right)
    
# 중위 순회 연산(왼->루트->오) 함수
def inorder_trav(root) :
    if root != None :
        inorder_trav(root.left)
        if (root.key1 != None) or (root.key2 != None) :
            if root.key1 != None :
                print(root.key1)
                inorder_trav(root.mid)
            if root.key2 != None :
                print(root.key2)        
        inorder_trav(root.right)
    
# main 함수
def main() :
    root = TreeNode( None, None, 0 )    # 루트 노드 생성
    
    root = create_tree( root, 10 )           # 트리 생성
    root = create_tree( root, 20 )
    root = create_tree( root, 30 )
    root = create_tree( root, 40 )
    root = create_tree( root, 50 )
    root = create_tree( root, 60 )
    root = create_tree( root, 70 )
    root = create_tree( root, 80 )
    root = create_tree( root, 90 )
    root = create_tree( root, 100 )
    
    print("< 전위 순회 연산 >")
    preorder_trav(root)
    
    print("< 중위 순회 연산 >")
    inorder_trav(root)
    
main()
