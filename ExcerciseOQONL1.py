#lex_auth_012742591379062784950
                                        
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
    
    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])
                                       
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

    
def split_queue(num_queue):
    #Populate queue_list with odd_queue and even_queue
    odd_queue=Queue(num_queue.get_max_size())
    even_queue=Queue(num_queue.get_max_size())
    while(not num_queue.is_empty()):
        ele=num_queue.dequeue()
        if ele % 2 == 0:
            even_queue.enqueue(ele)
        else:
            odd_queue.enqueue(ele)
    queue_list=[]
    queue_list.append(odd_queue)
    queue_list.append(even_queue)
    #write your logic here


    return queue_list

# Enqueue different values to the queue and test your program

num_queue=Queue(7)
num_queue.enqueue(2)
num_queue.enqueue(7)
num_queue.enqueue(9)
num_queue.enqueue(4)
num_queue.enqueue(6)
num_queue.enqueue(5)
num_queue.enqueue(10)

q_list=split_queue(num_queue)
q_list[0].display()
print("------------------------------------------------------")
q_list[1].display()