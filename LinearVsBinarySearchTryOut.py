#DSA-Tryout

import random
from timeit import default_timer as timer

def find_it_linear(num,element_list):
    #remove pass and copy the code written earlier for linear search
    guesses=0
    for e in element_list:
        guesses+=1
        if num == e:
            print("Element Found")
            return guesses
        # else:
        #     print("Not Found")
    print("Not found")
    return guesses

def find_it_binary(num,element_list):
    #remove pass and copy the code written earlier for binary search
    guesses=0
    if len(element_list)<1 or num>element_list[-1] or num<element_list[0]:
        return guesses
    if num==element_list[len(element_list)//2]:
        guesses+=1
        print("Match found")
        return guesses
    elif num<element_list[len(element_list)//2]:
        guesses+=find_it_binary(num,element_list[:len(element_list)//2])
    elif num>element_list[len(element_list)//2]:
        guesses+=find_it_binary(num,element_list[len(element_list)//2:])
    guesses+=1
    return guesses

#Initializes a list with values 1 to n in ascending order and returns it
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1,n+1):
        list_of_elements.append(i)
    return list_of_elements

def play(n):
    list_of_elements=initialize_list_of_elements(n)
    rand_index=random.randrange(0,len(list_of_elements))
    rand_num=list_of_elements[rand_index]
    print("Number to be guessed:",rand_num)
    start=timer()
    print("No. of guesses made using linear search:",find_it_linear(rand_num,list_of_elements))
    end=timer()
    print("Linear Search:Execution time in seconds:{0:.5f}".format( (end-start)))
    start=timer()
    print("No. of guesses made using binary search:",find_it_binary(rand_num,list_of_elements))
    end=timer()
    print("Binary Search:Execution time in seconds:{0:.5f}".format( (end-start)))

#Pass different values to play() and observe the output
play(100)