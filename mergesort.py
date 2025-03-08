def merge_sort(num_list):
    # Remove pass and write the logic here to return the sorted list
    low = 0
    high = len(num_list)-1
    if(low == high):
        # print('num_list in if',num_list)
        return num_list
    else:
        mid = len(num_list)//2
        left_list = num_list[0:mid]
        right_list = num_list[mid:high+1]
        # print('divided lists',left_list,right_list)
        returned_left_list = merge_sort(left_list)
        returned_right_list = merge_sort(right_list)
        # print('returned lists',returned_left_list,returned_right_list)
        sorted_list = merge(returned_left_list,returned_right_list)
        # print('sorted list in else',sorted_list)
        return sorted_list


def merge(left_list,right_list):
    # Remove pass and write the logic to merge the elements in the left_list and right_list and return the sorted list
    i = 0
    j = 0
    sorted_list = []
    while(i< len(left_list) and j < len(right_list)):
        # print('sl:',sorted_list,i,j)
        if(left_list[i]<=right_list[j]):
            sorted_list.append(left_list[i])
            # print('while if ',sorted_list)
            i+=1
        else:
            sorted_list.append(right_list[j])
            # print('while else')
            j+=1
    while (i<len(left_list)):
        # print('i',i)
        sorted_list.append(left_list[i])
        # print('while while if i',sorted_list)
        i+=1
    while (j<len(right_list)):
        # print('j',j)
        sorted_list.append(right_list[j])
        # print('while while if j', sorted_list)
        j+=1
    return sorted_list