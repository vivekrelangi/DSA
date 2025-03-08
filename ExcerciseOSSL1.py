#lex_auth_0127667370895278083332

def find_next_min(num_list,start_index):
    #Remove pass and write the logic to find the minimum element in a sub-list and return the index of the identified element in the num_list.
    #start_index indicates the start index of the sub-list
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
        

#Pass different values to the function and test your program
num_list=[10,2,100,67]
start_index=1
print("Index of the next minimum element is", find_next_min(num_list,start_index))