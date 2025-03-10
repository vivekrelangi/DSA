#lex_auth_0127667385791856643328
def swap(num_list, first_index, second_index):
    #Remove pass and copy the code written earlier for this function
    temp=num_list[first_index]
    num_list[first_index] = num_list[second_index] 
    num_list[second_index] = temp


def find_next_min(num_list,start_index):
    #Remove pass and copy the code written earlier for this function
    s=0
    ind = 0
    while start_index < len(num_list):
        if(s==0):
            s=num_list[start_index]
            ind = start_index
        elif(num_list[start_index]<s):
            s=num_list[start_index]
            ind = start_index
        start_index+=1
    return ind

def selection_sort(num_list):
    #Remove pass and implement the selection sort algorithm to sort the elements of num_list in ascending order
    passes = 0
    for i in range(len(num_list)-1):
        j = find_next_min(num_list,i)
        swap(num_list, i, j)
        passes+=1
    return passes

def bubble_sort(num_list):
    total_no_of_passes=0
    end_index=len(num_list)
    for index1 in range(0, end_index-1):
        swapped=False
        total_no_of_passes+=1
        for index2 in range(0, (end_index-index1-1)):
            if(num_list[index2]>num_list[index2+1]):
                swap(num_list, index2, index2+1)
                swapped=True
        if(swapped==False):
            break
    return total_no_of_passes

# num_list=[8,2,19,34,23, 67, 91]
num_list=[65, 23, 87, 112, 30, 1]
print("Selection Sort - No. of passes:",selection_sort(num_list))
print(num_list)

# num_list=[8,2,19,34,23, 67, 91]
num_list=[65, 23, 87, 112, 30, 1]
print("Bubble Sort - No. of passes:",bubble_sort(num_list))
