class Node:
    def __init__(self, data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data
    
    def get_next(self):
        return self.__next
    
    def set_data(self, data):
        self.__data=data

    def set_next(self, next):
        self.__next=next

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self, data):
        new_node=Node(data)
        if self.__head==None:
            self.__head=new_node
            self.__tail=new_node
        else:
            new_node=Node(data)
            self.__tail.set_next(new_node)
            self.__tail=new_node

    def display(self):
        linkedList=self.__str__()
        print(linkedList)

    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg
    
l=LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.display()