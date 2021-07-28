def insertion_sort(list):
    for i in range(1,len(list)):
        for j in range(i,0,-1):
            if list[j-1] > list[j]:
                list[j-1],list[j] = list[j],list[j-1]

            else:
                continue

           
    return list

if __name__=="__main__":
    list=[61,55,12,1,3,89,999,21546,2,3,]
    print(insertion_sort(list))


