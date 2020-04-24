def merge(list1,list2):
    len_list1,len_list2 = len(list1),len(list2)
    i = j = 0
    flist = []
    while i<len_list1 and j<len_list2:
        if list2[j]<list1[i]:
            flist.append(list2[j])
            j+=1      
        else :
            flist.append(list1[i])
            i+=1        
    flist = flist + list1[i:] + list2[j:]    
    return flist       

def merge_sort(list,start,end):
    if start<end:
        mid = (start+end)//2
        merge_sort(list,start,mid)
        merge_sort(list,mid+1,end)
        list[start:end+1] = merge(list[start:mid+1],list[mid+1:end+1])



list = [2,8,5,9,10,13,3,25,7,9]
merge_sort(list,0,len(list)-1)
print("Final sorted list is: ",list)
