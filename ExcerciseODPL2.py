#lex_auth_0127667323215544323487

#Code I have tried
# def find_subseqs_in_inc_ord(n_l):
#     # for n in n_l:
#     #     subseqs.append(n)
#     # for i,v in enumerate()
#     # return subseqs

#     # for i in sortedlist:
#     #     subseqs.append(i)
#     # for ind in range
#     subseqs = []
#     temp_dict = {}
#     sortedlist = sorted(n_l)
#     temp_dict[1] = []
#     for i in sortedlist: 
#         subseqs.append([i])
#         temp_dict[1].append([i])
#     temp_dict[2] = []
#     for i1 in range(len(temp_dict[1])):
#         for i2 in range(i1, len(temp_dict[1])):
#             if i1!=i2:
#                 temp = temp_dict[1][i1][:]
#                 temp_dict[2].append(temp.extend([sortedlist[i2]]))
#     print('Temp dict:', temp_dict)
#     return subseqs
    


# def max_sum_is(num_list):
#     subseqList = find_subseqs_in_inc_ord(num_list) 


#Pass different values to the function and test your program
# num_list=[1, 101, 2, 3, 100, 4, 5]
# # print("Sum of the maximum sum increasing subsequence is :" ,max_sum_is(num_list))
# print("subseqs", find_subseqs_in_inc_ord(num_list))

#Code I have copied
def max_sum_is(num_list):
    #Remove pass and write your logic here
    Max,dp = num_list[0],[i for i in num_list]#Assigning the first element of num_list as Maximum and given elements in num_list to dp
    i=1 #assigning i value as 1
    try: #try block
        while True: # using while true to break at certain condition
            tmp_max,element = 0,num_list[i] #Assigning temporary max value as 0 and element is the second element in the array
            for j in range(i): # for j in range of 1 (i value for first iteration)
                if dp[j] > tmp_max and element > num_list[j]: tmp_max = dp[j] #if dp[current index of iteration] greater than tmp_max and element is greater than
                #num_list[current index of iteration] then 
            dp[i] += tmp_max #dp[i] is append 0 if tmp_max is not set in if condition after all iterations
            if dp[i] > Max: Max = dp[i] #if current set value of dp[i] is greater than max it is max
            i+=1 #increasing i value
    except: pass #passing index out of bounds exception and stopping while condition as well 
    # print(dp)
    return Max #returning the maximum
#Pass different values to the function and test your program
num_list=[1, 6, 7, 90, 4, 8, 89]
print("Sum of the maximum sum increasing subsequence is :" ,max_sum_is(num_list))
     
