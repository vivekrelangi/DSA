#lex_auth_0127667360846643203336


"""*********************Stack*****************************"""
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__top==-1):
            return True
        return False

    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

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

def merge_stack(stack1,stack2):
    #Remove pass and write your logic here
    temp =[]
    while stack1.is_empty() != True:
        temp.append(stack1.pop())
    while stack2.is_empty() != True:
        temp.append(stack2.pop())
    sortednums = merge_sort(temp)
    sortedstack = Stack(len(sortednums))
    for num in sortednums:
        sortedstack.push(num)
    return sortedstack


#Pass different values to the function and test your program
stack2=Stack(3)
stack2.push(9)
stack2.push(11)
stack2.push(15)

stack1=Stack(4)
stack1.push(3)
stack1.push(7)
stack1.push(10)
stack1.push(21)

print("The elements in stack1 are:")
stack1.display()
print("The elements in stack2 are:")
stack2.display()
print()
output_stack=merge_stack(stack1, stack2)
print("The elements in the output stack are:")
output_stack.display()