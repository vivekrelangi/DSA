class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node
    
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
    #         add(data)
    # 1. Create a new node with the data
    # 2. If the linked list is empty (head node is not referring to any other node), 
    #    make the head node and the tail node refer to the new node
    # 3. Otherwise,
    #    a. Make the tail node’s link refer to new node
    #    b. Call the new node as tail node
        new_node=Node(data)
        if self.__head==None:
            self.__head=new_node
            self.__tail=new_node
        else:
            new_node=Node(data)
            self.__tail.set_next(new_node)
            self.__tail=new_node
        #Remove pass and copy the code you had written to add an element.
    
    def display(self):
    #     display()
    # 1. Call the head node as temp
    # 2. While temp is not None,
    #    a. Display temp’s data
    #    b. Make the next node as temp
        temp=self.__head
        #elements=[]
        while(temp is not None):
            #elements.append(temp.get_data())
            print(temp.get_data())
            temp=temp.get_next()
        #elements=" ".join(elements)
        #elements="Elements in linked list are, "+elements
        #return elements
        #Remove pass and copy the code you had written to display the element(s).
    
    def find_node(self,data):
        #   find_node()
        # 1. Call the head node as temp
        # 2. While temp is not None
        #       a. if temp's data is equal data that is to be found return temp(current node)
        #       b. Make the next node as temp
        # 3. Return None if data is not found
        temp=self.__head
        while(temp is not None):
            if temp.get_data() == data:
                return temp
            temp=temp.get_next()
        return None
        #Remove pass and write the logic to find the node and return the node if found or return None.

    def insert(self,data,data_before):
        #         insert(data,data_before)
        # 1. Create a new node with the given data
        # 2. If the data_before is None,
        #     a. Make the new node's link refer to head node 
        #     b. Call the new node as head node
        #     c. If the new node's link is None, make it the tail node
        # 3. Else
        #     a. Find the node with data_before, once found consider it as node_before
        #     b. Make the new node’s link refer to node_before’s link.
        #     c. Make the node_before’s link refer to new node
        #     d. If new node’s link is None, make it the tail node
        # 4. If node with data_before is not found, display appropriate error message
        new_node=Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head=new_node
            if new_node.get_next() is None:
                self.__tail=new_node
        else:
            node_before=self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail=new_node
            else:
                print("The node after which you want place the data is not found ")

        #Remove pass and write the logic to insert an element.

    def delete(self,data):
        #         delete(data):
        # 1. Find the node with the given data. If found,
        #    a. If the node to be deleted is head node, make the next node as head node
        #       1. If it is also the tail node, make the tail node as None
        #    b. Otherwise,
        #       1. Traverse till the node before the node to be deleted, call it temp
        #       2. Make temp’s link refer to node’s link.
        #       3. If the node to be deleted is the tail node, call the temp as tail node
        #       4. Make the node's link as None
        # 2. If the node to be deleted is not found, display appropriate error message
        node=self.find_node(data)
        if node is not None:
            if node is self.__head:
                self.__head=node.get_next()
                if node is self.__tail:
                    self.__tail=None
            else:
                temp=self.__head
                while(temp.get_next() is not node):
                    temp=temp.get_next()
                temp.set_next(node.get_next())
                if node is self.__tail:
                    self.__tail=temp
                node.set_next(None)
        else:
            print("Node to be deleted is not found")

        #Remove pass and write the logic to delete an element.    

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


list1=LinkedList()
#Add all the required element(s)
#Search for the required node
list1.add("Sugar")
list1.add("Teabags")
list1.add("Milk")
list1.add("Biscuits")
list1.display()
print("------------------------------------------------------------------")
list1.insert("Salt",None)
# for i in ["Milk","Salt","Biscuits","Apple Juice","Pomegranate","Watermelon"]:
#     node=list1.find_node(i)
#     if(node!=None):
#         print(i," found")
#     else:
#         print(i," not found") 
list1.display()
print("------------------------------------------------------------------")
list1.delete("Teabags")
list1.display()


