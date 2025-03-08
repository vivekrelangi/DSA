class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__front = 0
        self.__rear = -1

    # enqueue (data):
    # 1. Check whether queue is full. If full, display appropriate message
    # 2. If not,
    #    a. increment rear by one
    #    b. Add the element at rear position in the elements array

    #dequeue()
    # 1. Check whether the queue is empty. If it is empty, display appropriate message
    # 2. If not,
    #    a. Retrieve data at the front of the queue
    #    b. Increment front by 1
    #    c. Return the retrieved data

