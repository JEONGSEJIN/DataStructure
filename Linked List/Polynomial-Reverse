class ListNode :
    def __init__(self, coef, expon) :
        self.coef = coef
        self.expon = expon
        self.link = None
def insert_first(head, coef, expon) :
    p = ListNode(0,0)
    p.coef = coef
    p.expon = expon
    p.link = head
    head = p
    return head
def poly_add(plist1, plist2, plist3) :
    while plist1 != None and plist2 != None :
        if plist1.expon == plist2.expon :
            sum = plist1.coef + plist2.coef
            if(sum != 0 ) :
                plist3 = insert_first(plist3, sum, plist1.expon)
            plist1 = plist1.link
            plist2 = plist2.link
        elif plist1.expon < plist2.expon :
            plist3 = insert_first(plist3, plist1.coef, plist1.expon)
            plist1 = plist1.link
        else :
            plist3 = insert_first(plist3, plist2.coef, plist2.expon)
            plist2 = plist2.link
    while plist1 != None :
        plist3 = insert_first(plist3, plist1.coef, plist1.expon)
        plist1 = plist1.link
    while plist2 != None :
        plist3 = insert_first(plist3, plist2.coef, plist2.expon)
        plist2 = plist2.link
    return plist3
def reverse(head) :
    p = head;
    q = None
    while p != None :
        r = q
        q = p
        p = p.link
        q.link = r
    return q
def print_list(head) :
    print('polynomial = ', end = ' ')
    p = head
    while p != None :
        print('%dx^%d '%(p.coef, p.expon), end = ' ')
        if p.link != None:
            print('+ ', end = ' ')
        p = p.link
    print('\n')
def main() :
    list1 = None
    list2 = None
    list3 = None
    
    list1 = insert_first(list1, 3, 6)
    list1 = insert_first(list1, 7, 3)
    list1 = insert_first(list1, -2, 2)
    list1 = insert_first(list1, -9, 0)
    
    list2 = insert_first(list2, -2, 6)
    list2 = insert_first(list2, -4, 4)
    list2 = insert_first(list2, 6, 2)
    list2 = insert_first(list2, 6, 1)
    list2 = insert_first(list2, 1, 0)

    list3 = poly_add(list1, list2, list3)

    list1_prime = reverse(list1)
    list2_prime = reverse(list2)
    
    print_list(list1_prime)
    print_list(list2_prime)
    print_list(list3)
main()
