def swap(num_list, first_index, second_index):
    global no_of_swaps
    temp=num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=temp
    no_of_swaps+=1

def bubble_sort(num_list):
    global no_of_passes
    end_index=len(num_list)
    for index1 in range(0, end_index-1):
        swapped=False
        no_of_passes+=1
        for index2 in range(0, (end_index-index1-1)):
            print("index1,index2", index1, ",", index2)
            if(num_list[index2]>num_list[index2+1]):
                swap(num_list, index2, index2+1)
                swapped=True
        if(swapped==False):
            break
        print("At the end of pass-",no_of_passes,":",num_list)

no_of_swaps=0
no_of_passes=0
num_list=[89,43,99,55,87,67]
print("In the beginning:",num_list)
print("-------------------------------------------------")
bubble_sort(num_list)
print("-------------------------------------------------")
print("At the end:",num_list)
print("-------------------------------------------------")
print("No. of swaps:", no_of_swaps)
print("No. of passes:",no_of_passes)

