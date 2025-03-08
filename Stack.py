#If there are no elements top is -1, Stack is LIFO or FILO mechanism and a linear data structure
class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    # push(data):
    # 1. Check whether the stack is full. If full, display appropriate message
    # 2. If not,
    #     a. increment top by one
    #     b. Add the element at top position in the elements array

    #pop:
    # 1. Check whether the stack is empty. If empty, display appropriate message
    # 2. If not,
    #    a. Retrieve data at the top of the stack
    #    b. Decrement top by 1
    #    c. Return the retrieved data
    


