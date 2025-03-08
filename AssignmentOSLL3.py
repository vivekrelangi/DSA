#lex_auth_0127667344787537923521

"""The manager of an airport wants to generate various reports.

Details of the flights and passengers are stored as mentioned below:

1. Flight details are stored as a list of strings. Suppose "AI890:BAN:MUM:1400" is a string in the flight details list, it should be interpreted as follows: AI890 is the flight name , BAN is the source, MUM is the destination and 1400 is the departure time (24 hour format).

2. Passenger details are stored in a dictionary where key is the PNR number of the passenger and value is a list containing passenger details. 

   Suppose "LW101":["Amanda","AI678","C7",25] is an element in the dictionary, it should be interpreted as follows:

  LW101 is the PNR number of the passenger and  ["Amanda","AI678","C7",25] is the list in which the index 0, 1, 2 and  3  represents the passenger name, flight name, seat number and the baggage weight respectively.

Assume that we are considering only those flights which are departing between 0700hrs and 2000hrs.

Write a python program to perform the below mentioned functionalities.

find_flights(flight_time): This method accepts time in 24 hour format and returns the list of flights which are waiting to takeoff within another two hours starting from the given time (both inclusive).

sort_flight_list(flight_list): This method takes the flight details list as the input and returns the flight details list sorted based on the increasing order of their departure time.

get_passenger_details(flight_detail): This method takes a flight’s detail as input and returns the list of PNR numbers of the passengers who are waiting to board the given flight.

security_check(passenger_pnr_list): This method takes the list of PNR numbers of the passengers boarding a specific flight as the input and returns the list of PNR numbers of the passengers whose baggage has been cleared.
The baggage will be cleared if the baggage weight is between 0-25kg (both inclusive)

sort_passengers(passenger_pnr_list): This method takes the list of PNR numbers of the passengers whose baggage has been cleared as the input and returns the list of PNR numbers sorted based on the increasing order of their seat numbers. ( order of seats: A→J )

boarding(passenger_pnr_list): The passengers who have to board a flight should stand in a queue. This method takes the list of PNR numbers of the passengers sorted based on seat numbers as the input and returns the queue of PNR numbers of the passengers. The queue should be of the same size as that of the list. The first passenger in the list should be the first person to stand in the queue.

seating(passenger_queue):The flight has only one door which is at the back side. The passengers who board the flight are expected to occupy seats from the front. So the passenger who board last will be able to come out first from the flight. This method takes the queue of PNR numbers of the passengers as the input and returns the stack ( max size of the stack should be same as the size of the queue) which contains the PNR numbers of the passengers representing the seating.

"""

"""*********************Queue*****************************"""
class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

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


    def get_max_size(self):
        return self.__max_size

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

"""****************************Merge Sort**********************************"""
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


#Global variables
flight_details=["AI890:BAN:MUM:1400","AI678:BAN:LON:1200","AI345:BAN:CAN:1410","AF780:BAN:AGF:1340","AI001:BAN:AUS:1500","AI404:BAN:NY:1220"]

passenger_details_dict=\
{"LW101":["Amanda","AI678","C7",25],"LW103":["John","AI345","A2",10],"LW107":["Alex","AI678","G5",12],\
"TW700":["Hary","AF780","D2",26],"LW167":["Kate","AI001","G3",25],"LT890":["Wade","AI404","G3",25],\
"TW677":["Preet","AF780","D3",25],"LA106":["Henry","AI001","B5",25.5],"LA104":["Ajay","AI001","A7",23],\
"LW202":["Amy","AI345","C3",24.5],"LT673":["Susan","AI404","J8",5],"TW709":["Tris","AF780","H5",22.5],\
"LA188":["Cameron","AI890","H4",22],"LA902":["Scofield","AI678","G4",23],"TW767":["Pom","AF780","H4",2],\
"LW787":["Burrows","AI890","B4",29],"LW898":["Sara","AI678","E4",14],"LW104":["Williams","AI890","C4",10] }

def find_flights(flight_time):
    #Remove pass and write your logic here
    retfls = []
    for f in flight_details:
        fls = f.split(":")
        if int(fls[3])/100 >= flight_time/100 and int(fls[3])/100 <= (flight_time/100)+2:
            retfls.append(f)
    return retfls


def sort_flight_list(flight_list):
    #Remove pass and write your logic here
    d = dict()
    for f in flight_list:
        fls = f.split(":")
        if int(fls[3]) not in d.keys():
            d[int(fls[3])] =  [f]
        else:
            d[int(fls[3])].append(f)
    flight_times = merge_sort(list(d.keys()))
    sorted_list = []
    for f_time in flight_times:
        sorted_list.extend(d[f_time])
    return sorted_list

def get_passenger_details(flight_detail):
    #Remove pass and write your logic here
    pnrs = []
    f = flight_detail.split(":")
    for k,v in passenger_details_dict.items():
        if passenger_details_dict[k][1] == f[0]:
            pnrs.append(k)
    return pnrs

def security_check(passenger_pnr_list):
    #Remove pass and write your logic here
    retpnrs = []
    for pnr in passenger_pnr_list:
        if passenger_details_dict[pnr][3] <=25 and passenger_details_dict[pnr][3] >= 0:
            retpnrs.append(pnr)
    return retpnrs

def sort_passengers(passenger_pnr_list):
    #Remove pass and write your logic here
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    sortedpnrs = []
    for letter in letters:
        # templist = []
        for pnr in passenger_pnr_list:
            for n in range(0,10):
                if passenger_details_dict[pnr][2][0] == letter and int(passenger_details_dict[pnr][2][1]) == n:
                    # templist.append(pnr)
                    # print('pnr:', pnr)
                    sortedpnrs.append(pnr)
    return sortedpnrs
    


def boarding(passenger_pnr_list):
    #Remove pass and write your logic here
    passenger_q = Queue(len(passenger_pnr_list))
    for pnr in passenger_pnr_list:
        passenger_q.enqueue(pnr)
    return passenger_q

def seating(passenger_queue):
    #Remove pass and write your logic here
    passenger_stack = Stack(passenger_queue.get_max_size())
    while passenger_queue.is_empty() != True:
        passenger_stack.push(passenger_queue.dequeue())
    return passenger_stack

print("The flight details :")
print(flight_details)
print()
print("The passenger details at the airport:")
print(passenger_details_dict)
print()
time=1130
print("Details of the flight between the timings",time,"and",time+200,"are:")
flight_list=find_flights(time)
flight_list=sort_flight_list(flight_list)
print(flight_list)
print()
print("Details of the passengers boarding the flights between the timings ",time,"and",(time+200),"are:")
print()
for i in range(0,len(flight_list)):
    flight_data=flight_list[i].split(':')
    flight_name=flight_data[0]

    passenger_pnr_list=get_passenger_details(flight_list[i])
    print("PNR details of the passengers boarding the flight",flight_name,":")
    print(passenger_pnr_list)

    print()
    updated_passenger_pnr_list=security_check(passenger_pnr_list)
    print("PNR details of the passengers of flight",flight_name," whose baggage has been cleared:")
    print(updated_passenger_pnr_list)

    sorted_passenger_pnr_list=sort_passengers(updated_passenger_pnr_list)
    print("PNR details of the passengers of flight",flight_name," sorted based on seating number:")
    print(sorted_passenger_pnr_list)

    print()
    print("The PNR details of the passengers at the queue",flight_name,":")
    passenger_queue=boarding(updated_passenger_pnr_list)
    passenger_queue.display()

    print()
    seating_stack=seating(passenger_queue)
    print("The PNR details of the passengers in the flight",flight_name,":")
    seating_stack.display()