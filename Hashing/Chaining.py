# Chaining (by Linked List & Hash Table)

# 연결 리스트의 노드를 생성해주는 클래스
class ListNode :
    def __init__(self, data) :
        self.data = data     # data 인스턴스 멤버
        self.link = None    # link 인스턴스 멤버

# 체이닝 함수
def hash_chain( hash_table, data_list) :
    for new_data in data_list :
        mod = new_data % 11
        
        if hash_table[mod].data == None :
            head_node = ListNode(mod)
            hash_table[mod] = head_node
            new_node = ListNode(new_data)
            head_node.link = new_node 
        
        else :
            for i in hash_table :
                if i.data == mod :
                    new_node = ListNode(new_data)
                    while i.link.link != None :
                        i = i.link
                    i.link.link = new_node  # 연결 리스트의 다음 리스트에 연결하도록 만들기
                    break   

    for i in hash_table :
        if i.data != None :
            print(str(i.data) + " :", end = " ")
            while i.link.link != None :
                print(i.link.data, "->", end = " ")
                i.link = i.link.link
            print(i.link.data, "->", end = " ")
            print("\n")

def main():
    hash_table = []
    data_list = [ 12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5 ]
    for i in range(len(data_list)) :
        hash_table.append(ListNode(None))
    print("< Hash Table (by Chaining) >\n")
    hash_chain( hash_table, data_list)

main()
