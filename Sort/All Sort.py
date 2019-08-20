list = [ 71, 49, 92, 55, 38, 82, 72, 53 ] # 주어진 정렬되지 않은 리스트
def Quick_Sort(list): # 퀵 정렬
    print(list)
    if len(list) <= 1:
        return list
    pivot = list[0]
    smaller = []
    bigger = []
    for num in list:
        if num < pivot:
            smaller.append(num)
        if num > pivot:
            bigger.append(num)
    return Quick_Sort(smaller) + [pivot] + Quick_Sort(bigger)        
         
def Insertion_Sort(list): # 삽입 정렬
    print("\n\n'삽입 정렬' 과정 중 리스트 상태: ")
    for i in range(1, len(list)) :  # Examole)
        key = list[i]               # i = 3, 55
        j = i - 1                   # j = i - 1 =  2, 92
        while j >= 0 :              # (j = 2) >= 0
            if list[j] > key :      # 만약 92 > 55 이면
                list[j+1] = list[j] # 55자리에 92넣기
                list[j] = key       # 92자리엔 55를 넣음
            j = j-1
        print(list)
    print("\n최종 '삽입 정렬' 결과: ")
    for i in list :
        print("[%2d] "%i, end = '')
    
def Selection_Sort(list): # 선택 정렬
    print("\n\n'선택 정렬' 과정 중 리스트 상태: ")
    for i in range(0, len(list)-1) :
        least = i
        min_data = list[least]
        for data in list :
            if min_data > data :
                min_data = data
        list[least] = min_data
        
        
        print(list)
    
#def Bubble_Sort(list): # 버블 정렬
    
#def Shell_Sort(list): # 쉘 정렬
    
#def Merge_Sort(list): # 합병 정렬
    
#def Heap_Sort(list): # 히프 정렬
    
#def Radix_Sort(): # 기수 정렬

def main():
    print("초기 리스트: ")
    for i in list :
        print("[%2d] "%i, end = '')
        
    print("\n\n'퀵 정렬' 과정 중 리스트 상태 및 최종 결과: ")
    print(Quick_Sort(list)) # 퀵 정렬
    
    Insertion_Sort(list) # 삽입 정렬
    
    Selection_Sort(list) # 선택 정렬
    #Bubble_Sort(list)  # 버블 정렬
    #Shell_Sort(list)   # 쉘 정렬
    #Merge_Sort(list)   # 합병 정렬
    #Heap_Sort(list)    # 히프 정렬
    #Radix_Sort(list)   # 기수 정렬
    
main()
