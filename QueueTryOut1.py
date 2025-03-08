
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
        
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if self.__rear == self.__max_size - 1:
            return True
        return False
        #Remove pass and write the logic to check whether Queue is full. If the queue is full, return true else return false.
    
    def enqueue(self,data):
        if self.is_full():
            print("Queue is full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
        #Remove pass and write the logic to enqueue an element. Enqueue should be done only if queue is not full. Otherwise display appropriate message.
    
    def display(self):
        for ele in self.__elements:
            print(ele)
        #Remove pass and write the logic to display all the queue element(s).
                                                  
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



queue1=Queue(5)
#Enqueue all the required element(s).
queue1.enqueue("Tom")
queue1.enqueue("Dick")
queue1.enqueue("Hary")
queue1.enqueue("Jack")
queue1.enqueue("Maria")
#Display all the elements in the queue.
queue1.display()
                                              