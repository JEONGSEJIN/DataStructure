list = [ 71, 49, 92, 55, 38, 82, 72, 53 ] # 주어진 정렬되지 않은 리스트
def Insertion_Sort(list):                 # 삽입 정렬
    print("\n\n'삽입 정렬' 과정 중 리스트 상태: ")
    for i in range(1, len(list)) :        # Example)
        key = list[i]                     # i = 1, key = list[1] = 49
        j = i - 1                         # j = i - 1 = 0
        while j >= 0 :                    # (j = 0) >= 0
            if list[j] > key :            # 만약 71 > 49 이면
                list[j+1] = list[j]       # 49자리에 71넣기
                list[j] = key             # 71자리엔 49를 넣음
            j = j-1                       # 역순으로 비교해 주기 위해 값을 빼준다
        print(list)
    print("\n최종 '삽입 정렬' 결과: ")
    for i in list :                       # 정렬된 리스트를 순회하면서
        print("[%2d] "%i, end = '')       # 각 요소들을 출력
        
def main():
    print("초기 리스트: ")
    for i in list :                    # 주어진 리스트를 순회하면서
        print("[%2d] "%i, end = '')    # 각 요소들을 출력
    
    Insertion_Sort(list)               # 삽입 정렬
main()
