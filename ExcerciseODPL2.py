#lex_auth_0127667323215544323487

def find_subseqs_in_inc_ord(n_l):
    # for n in n_l:
    #     subseqs.append(n)
    # for i,v in enumerate()
    # return subseqs

    # for i in sortedlist:
    #     subseqs.append(i)
    # for ind in range
    subseqs = []
    temp_dict = {}
    sortedlist = sorted(n_l)
    temp_dict[1] = []
    for i in sortedlist: 
        subseqs.append([i])
        temp_dict[1].append([i])
    temp_dict[2] = []
    for i1 in range(len(temp_dict[1])):
        for i2 in range(i1, len(temp_dict[1])):
            if i1!=i2:
                temp = temp_dict[1][i1][:]
                temp_dict[2].append(temp.extend([sortedlist[i2]]))
    print('Temp dict:', temp_dict)
    return subseqs
    


# def max_sum_is(num_list):
#     subseqList = find_subseqs_in_inc_ord(num_list) 


#Pass different values to the function and test your program
num_list=[1, 101, 2, 3, 100, 4, 5]
# print("Sum of the maximum sum increasing subsequence is :" ,max_sum_is(num_list))
print("subseqs", find_subseqs_in_inc_ord(num_list))
