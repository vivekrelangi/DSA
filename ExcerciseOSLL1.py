#lex_auth_0127667319794565123439

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

def order_heights(student_list,height_list):
    #Write your logic here
    # students = {}
    # for index in range(len(student_list)):
    #     students[height_list[index]]=student_list[index]
    # print(students)
    # students.keys()=merge_sort(students.keys())
    # print('a',students)
    sorted_heights = merge_sort(height_list)
    sorted_students = []
    for shind in range(len(sorted_heights)):
        for hind in range(len(height_list)):
            if (sorted_heights[shind] == height_list[hind]):
                sorted_students.append(student_list[hind])
    # print(sorted_students)
    student_list = sorted_students
    height_list = sorted_heights
    return[student_list,height_list]

#Pass different values to the function and test your program
student_list=["Santa","Tris","Arun","Rachel","John"]
height_list=[132.7,129.2,135,130.6,140]
print("Initial student details :")
print("The students:",student_list)
print("Their heights:",height_list)
print()
result=order_heights(student_list,height_list)
print("After arranging the students in the order of their height:")
print("The students :",result[0])
print("Their heights:",result[1])