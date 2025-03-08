#lex_auth_0127667356693872643343
#SelectionSort
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
    total_no_of_passes = 0
    for i in range(len(num_list)):
        j = find_next_min(num_list,i)
        swap(num_list, i, j)
        total_no_of_passes+=1
    return total_no_of_passes


#Pass different values to the function and test your program
num_list=[65, 23, 87, 112, 30, 1]
print("Before sorting;",num_list)
selection_sort(num_list)
print("After sorting:",num_list)