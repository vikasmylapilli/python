def quick_sort(list_1):
    left = []
    right= []
    
    if len(list_1) <= 1:
        return list_1
    else:
        middle=[] 
        middle.append(list_1[-1])
        p_p = list_1[-1]
        for i in range (len(list_1)-1): 
             
            if list_1[i] < p_p:
                left.append(list_1[i])
            else:
                right.append(list_1[i])       
        a = left + middle + right   
    return   quick_sort(left) + middle + quick_sort(right)   
             
            
if __name__=="__main__":
    y = [3, 4, 2,-6, 7, 1, 9]    
    print(quick_sort(y))
  

