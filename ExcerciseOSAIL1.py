def find_decreasing_start(list1,start,end):
    #Remove pass and write your logic here
    prev=0
    for ind in range(start,end+1):
        if list1[prev]>list1[ind]:
            return ind
        else:
            prev=ind
    return 0
            
        

#Use different values for list1 and test your program
list1=[1,4,7,8,9,5,4]
start=0
end=len(list1)-1
result=find_decreasing_start(list1,start,end)
print("The index position at which the increasing array starts decreasing is:",result)