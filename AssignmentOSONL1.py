#lex_auth_0127438990347550721631

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
                print(self.__elements[index], end=" ")
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
        
        
def change_smallest_value(number_stack):
    #write your logic here
    smallest_values=Stack(number_stack.get_max_size())
    remaing_values=Stack(number_stack.get_max_size())
    temp_stack=Stack(number_stack.get_max_size())
    temp1=number_stack.pop()
    smallest=temp1
    number_stack.push(temp1)
    while not number_stack.is_empty():
        temp=number_stack.pop()
        if temp>=smallest:
            temp_stack.push(temp)
        elif temp<smallest:
            smallest=temp
            temp_stack.push(temp)
    while not temp_stack.is_empty():
        temp2=temp_stack.pop()
        if temp2==smallest:
            smallest_values.push(temp2)
        else:
            remaing_values.push(temp2)
    while not remaing_values.is_empty():
        temp_stack.push(remaing_values.pop())
    while not smallest_values.is_empty():
        temp_stack.push(smallest_values.pop())
    while not temp_stack.is_empty():
        number_stack.push(temp_stack.pop())

    return number_stack

#Add different values to the stack and test your program
number_stack=Stack(8)
number_stack.push(7)
number_stack.push(8)
number_stack.push(5)
number_stack.push(66)
number_stack.push(5)
print("Initial Stack:")
number_stack.display()
change_smallest_value(number_stack)
print("After the change:")
number_stack.display()