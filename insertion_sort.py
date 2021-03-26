def insertion_sort(list):
    for i in range(1,len(list)):
        for j in range(0,i):
            if list[j] > list[i]:
                list[i],list[j] = list[j],list[i]
           
    return list

if __name__=="__main__":
    list=[61,55,12,1,3,89,999,21546,2,3,]
    print(insertion_sort(list))


