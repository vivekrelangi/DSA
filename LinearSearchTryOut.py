#DSA-Tryout

import random

def find_it(num,element_list):
    #Remove pass and write the logic to search num in element_list using linear search algorithm
    #Return the total number of guesses made
    guesses=0
    for e in element_list:
        guesses+=1
        if num == e:
            print("Element Found")
            break
        else:
            print("Not Found")
    return guesses

#Initializes a list with values 1 to n in random order and returns it
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1,n+1):
        list_of_elements.append(i)
    mid=n//2
    for j in range(0,n):
        index1=random.randrange(0,mid)
        index2=random.randrange(mid,n)
        num1=list_of_elements[index1]
        list_of_elements[index1]=list_of_elements[index2]
        list_of_elements[index2]=num1
    return list_of_elements

def play(n):
    # Step 1: Invoke initialize_list_of_elements() by passing n
    # Step 2: Generate a random number from the list of elements. The number should be between 1 and n (both inclusive)
    # Step 3: Invoke find_it() by passing the number generated at Step 2 and list generated at Step 1 and display the return value
    # Remove pass and write the code to implement the above three steps.
    listE=initialize_list_of_elements(n)
    randnum=random.randrange(1,n,1)
    print(find_it(randnum, listE))

#Pass different values to play() and observe the output
play(400)