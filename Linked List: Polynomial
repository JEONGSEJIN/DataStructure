class ListNode:                        # 다항식을 표현해 주는 클래스
    def __init__(self,coef,expon) :
        self.coef = coef               # 계수를 나타내는 인스턴스 멤버
        self.expon = expon             # 지수를 나타내는 인스턴스 멤버
        self.link = None               # 링크를 나타내는 인스턴스 멤버
class ListType:                        # 다항식을 관리해 주는 클래스
    def __init__(self,size) :
        LN = ListNode(0,0)             # 다항식을 표현해주는 인스턴스 객체를 
                                       # 다항식을 관리해주는 클래스 안에 선언
        self.size = size               # 항의 개수를 나타내는 인스턴스 멤버
        LN.head = None                 # 초항(->차수가 가장 높은 항)에 접근
        LN.tail = None                 # 막항(->차수가 가장 낮은 항)에 접근
def error(message) :                   # 오류를 출력해주는 함수
    print("%s" %message)               # 오류메세지 출력
def create():                          # 리스트의 헤더 생성 함수
    plist = ListType(0)                # plist는 다항식을 가리키는 헤더포인터 생성
    plist.size = 0                     # 다항식의 사이즈
    plist.head = None                  # 다항식의 초항
    plist.tail = None                  # 다항식의 막힝
    return plist                       # 만들어진 다항식의 헤더포인터를 반환
def insert_last(plist, coef, expon) :  # 다항식의 항을 연결리스트에 넣어주는 함수 (노드생성함수)
    temp = ListNode(0,0)               
    if temp == None :                  
        error("메모리 할당 에러")      
    temp.coef = coef                   
    temp.expon = expon                 
    temp.link = None                   
    if plist.tail == None :             
        plist.head = temp              
        plist.tail = temp               
    else :
        plist.tail.link = temp          
        plist.tail = temp               
    plist.size += 1
def poly_add(plist1, plist2, plist3) : # 다항식의 합을 계산해주는 함수               
    a = plist1.head                     
    b = plist2.head                     
    while a and b :                     
        if a.expon == b.expon :         
            sum = a.coef + b.coef       
            if(sum != 0) :              
                insert_last(plist3, sum, a.expon)       
            a = a.link                  
            b = b.link                  
        elif a.expon > b.expon :        
            insert_last(plist3, a.coef, a.expon)        
            a = a.link                  
        else :                          
            insert_last(plist3, b.coef,b.expon)         
            b = b.link                  
    while a != None:                    
        insert_last(plist3, a.coef, a.expon)            
        a = a.link                      
    while b != None:                    
        insert_last(plist3, b.coef, b.expon)            
        b = b.link                      
def poly_print(plist) :                 # 다항식을 보여주는 함수           
    p = plist.head                       
    print("polynomial =  ", end = ' ')   
    while p.link != None :              
        print('%d x^ %d '%(p.coef,p.expon), end = ' ')  
        if p.link != None :             
            print('+ ', end = ' ')      
        p = p.link                      
    print('%d x^ %d '%(p.coef,p.expon), end = ' ')      
    print('\n')                       
def main() :                           # main()함수
    # 연결 리스트 헤더 생성
    list1 = create()                    
    list2 = create()                    
    list3 = create()                    
    
    # 다항식1 (A(x)) 생성
    insert_last(list1, 3, 6)           # (다항식 리스트, 계수, 차수)
    insert_last(list1, 7, 3)             
    insert_last(list1, -2, 2)
    insert_last(list1, -9, 0)
    
    # 다항식2 (B(x)) 생성
    insert_last(list2, -2, 6)
    insert_last(list2, -4, 4)
    insert_last(list2, 6, 2)
    insert_last(list2, 6, 1)
    insert_last(list2, 1, 0)
    
    # 다항식1(A(x)), 다항식2(B(x)) 출력
    poly_print(list1)                  # 다항식1 출력
    poly_print(list2)                  # 다항식2 출력
    
    # 다항식3 = 다항식1 + 다항식2 (C(x)) 생성
    poly_add(list1, list2, list3)      # 다항식1과 다항식2를 더함
    poly_print(list3)                  # 다항식3 출력
main()                                 # main()함수 실행
