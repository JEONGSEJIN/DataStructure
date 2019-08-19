list = [ 71, 49, 92, 55, 38, 82, 72, 53 ] # 주어진 정렬되지 않은 리스트
def Quick_Sort(list):                     # 퀵 정렬
    print(list)
    if len(list) <= 1:                    # 만약 리스트 안의 요소가 1개이면 
        return list                       # 그 리스트를 바로 리턴
    pivot = list[0]                       # pivot: 리스트의 제일 첫 번째 요소 = list[0] = 71
    smaller = []                          # pivot보다 작은 요소들을 저장하기 위한 리스트
    bigger = []                           # pivot보다 큰 요소들을 저장하기 위한 리스트
    for num in list:                      # Example)
        if num < pivot:                   # 49 < 71 
            smaller.append(num)           # smaller = [ 49, 55, 36, 53 ]
        if num > pivot:                   # 92 > 71 
            bigger.append(num)            # bigger = [ 92, 82, 72 ]
    # smaller리스트도 정렬해 주고, bigger리스트도 정렬해 준 뒤에, pivot 양 옆에 합쳐서 리턴
    return Quick_Sort(smaller) + [pivot] + Quick_Sort(bigger)

def main():
    print("초기 리스트: ")
    for i in list :                  # 주어진 리스트를 순회하면서
        print("[%2d] "%i, end = '')  # 각 요소들을 출력
        
    print("\n\n'퀵 정렬' 과정 중 리스트 상태 및 최종 결과: ")
    print(Quick_Sort(list))          # 퀵 정렬
    
main()
