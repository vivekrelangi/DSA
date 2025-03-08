"""#Do not remove the below import statement
import sys

'''This function provides the capacity, size and space left in the list.
You can invoke it to get the details of the list'''

def list_details(lst):
    #Number of elements that can be stored in the list
    print("Capacity:", (sys.getsizeof(lst)-36)//4)

    #Number of elements in the list
    print("Size:", len(lst))

    #Number of elements that can be accommodated in the space left
    print("Space Left:", ((sys.getsizeof(lst)-36) - len(lst*4))//4)

    #formula changes based on the system architecture
    #(size-36)/4 for 32 bit machines and
    #(size-64)/8 for 64 bit machines

    # 36,64 - size of an empty list based on machine
    # 4,8 - size of a single element in the list based on machine

marias_lst=[]
print("Empty list created!!!")
print("List details:")
list_details(marias_lst)


marias_lst.append("Sugar")
print("Maria's list after adding Sugar:")
print(marias_lst)
print("List details:")
list_details(marias_lst)

marias_lst.append("Tea Bags")
marias_lst.append("Milk")
marias_lst.append("Biscuit")
print("Maria's list after adding items:")
print(marias_lst)
print("List details:")
list_details(marias_lst)
print(type(marias_lst))
"""
"""#Do not remove the below import statement
import sys

'''This function provides the capacity, size and space left in the list.
You can invoke it to get the details of the list'''

def list_details(lst):
    #Number of elements that can be stored in the list
    print("Capacity:", (sys.getsizeof(lst)-36)//4)

    #Number of elements in the list
    print("Size:", len(lst))

    #Number of elements that can be accommodated in the space left
    print("Space Left:", ((sys.getsizeof(lst)-36) - len(lst*4))//4)

    #formula changes based on the system architecture
    #(size-36)/4 for 32 bit machines and
    #(size-64)/8 for 64 bit machines

    # 36,64 - size of an empty list based on machine
    # 4,8 - size of a single element in the list based on machine

marias_lst=[]
print("Empty list created!!!")
print("List details:")
list_details(marias_lst)


marias_lst.append("Sugar")
print("Maria's list after adding Sugar:")
print(marias_lst)
print("List details:")
list_details(marias_lst)


marias_lst.append("Tea Bags")
marias_lst.append("Milk")
marias_lst.append("Biscuit")
print(marias_lst)
print("List details:")
list_details(marias_lst)

marias_lst.insert(1,"Salt")
print(marias_lst)
print("List details:")
list_details(marias_lst)"""
#Do not remove the below import statement
import sys

'''This function provides the capacity, size and space left in the list.
You can invoke it to get the details of the list'''

"""def list_details(lst):
    #Number of elements that can be stored in the list
    print("Capacity:", (sys.getsizeof(lst)-36)//4)

    #Number of elements in the list
    print("Size:", len(lst))

    #Number of elements that can be accommodated in the space left
    print("Space Left:", ((sys.getsizeof(lst)-36) - len(lst*4))//4)

    #formula changes based on the system architecture
    #(size-36)/4 for 32 bit machines and
    #(size-64)/8 for 64 bit machines

    # 36,64 - size of an empty list based on machine
    # 4,8 - size of a single element in the list based on machine

marias_lst=[]
print("Empty list created!!!")
print("List details:")
list_details(marias_lst)


marias_lst.append("Sugar")
print("Maria's list after adding Sugar:")
print(marias_lst)
print("List details:")
list_details(marias_lst)


marias_lst.append("Tea Bags")
marias_lst.append("Milk")
marias_lst.append("Biscuit")
print(marias_lst)
print("List details:")
list_details(marias_lst)

marias_lst.insert(1,"Salt")
print(marias_lst)
print("List details:")
list_details(marias_lst)

marias_lst.pop(2)
print(marias_lst)
print("List details:")
list_details(marias_lst)"""
"""class Employee:
    def __init__(self, name, emp_id, email_id):
        self.__name=name
        self.__emp_id=emp_id
        self.__email_id=email_id

    def get_name(self):
        return self.__name

    def get_emp_id(self):
        return self.__emp_id

    def get_email_id(self):
        return self.__email_id

class OrganizationDirectory:
    def __init__(self,emp_list):
        self.__emp_list=emp_list

    def lookup(self,key_name):
        result_list=[]
        for emp in self.__emp_list:
            if(key_name in emp.get_name()):
                result_list.append(emp)
        self.display(result_list)
        return result_list

    def display(self,result_list):
        print("Search results:")
        for emp in result_list:
            print(emp.get_name()," ", emp.get_emp_id()," ",emp.get_email_id())



emp1=Employee("Kevin",24089, "Kevin_xyz@organization.com")
emp2=Employee("Jack",56789,"Jack_xyz@organization.com")
emp3=Employee("Jackson",67895,"Jackson_xyz@organization.com")
emp4=Employee("Henry Jack",23456,"Jacky_xyz@organization.com")
emp_list=[emp1,emp2,emp3,emp4]

org_dir=OrganizationDirectory(emp_list)
#Search for an employee
org_dir.lookup("Jack")"""
"""def update_mark_list(mark_list, new_element, pos):
    #Write your logic here
    mark_list.insert(pos, new_element)
    return mark_list

def find_mark(mark_list,pos1,pos2):
    '''Remove pass and write your logic here to return a list containing
    the marks at pos1 and pos2 respectively.'''
    ret=[]
    ret.append(mark_list[pos1])
    ret.append(mark_list[pos2])
    return ret

#Provide different values for the variables and test your program
mark_list=[89,78,99,76,77,72,88,99]
new_element=69
pos=2
pos1=5
pos2=8
print(update_mark_list(mark_list, new_element, pos))
print(find_mark(mark_list, pos1, pos2))
print(mark_list)"""
"""class Node:
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

item_node=Node("Sugar")
print(item_node.get_data())"""
"""class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    def get_head(self):
        return self.__head
    def get_tail(self):
        return self.__tail"""
"""class Node:
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
#         pass
#         add(data)
# 1. Create a new node with the data
# 2. If the linked list is empty (head node is not referring to any other node), 
#    make the head node and the tail node refer to the new node
# 3. Otherwise,
#    a. Make the tail node’s link refer to new node
#    b. Call the new node as tail node
        new_node=Node(data)
        if self.__head == None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node


        #Remove pass and write the logic to add an element
    def display(self):
#         pass
#     display()
# 1. Call the head node as temp
# 2. While temp is not None,
#    a. Display temp’s data
#    b. Make the next node as temp
        temp = self.__head
        while temp is not None:
            print("temp.get_data():",temp.get_data())
            temp=temp.get_next()


        #Remove pass and write the logic to display the elements
    
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
list1.add("Sugar")
list1.add("Tea Bags")
list1.add("Milk")
list1.add("Biscuit")
print("Element added successfully")
#print("2nd Element:",list1.get_head().get_next().get_data())
print(list1.display())
#Similarly add all the specified element(s)"""
"""class Node:
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
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node
    
    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()
                                              
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

def count_nodes(biscuit_list):
    count=0
    # Write your logic here
    temp=biscuit_list.get_head()
    if temp is None:
        return count
    while temp.get_next() is not None:
        count+=1
        #print(temp.get_data())
        temp=temp.get_next()
    count+=1
    #print(temp.get_data())
    return count

biscuit_list=LinkedList()
biscuit_list.add("Goodday")
biscuit_list.add("Bourbon")
biscuit_list.add("Hide&Seek")
biscuit_list.add("Nutrichoice")

print(count_nodes(biscuit_list))"""
"""#node of a linked list
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
        self.__next=next_node"""
                                            

                              