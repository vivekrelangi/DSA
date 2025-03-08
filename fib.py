count = 0
def fibonacci(num):
    global count 
    if(num==0):
        count += 1
        return 0
    elif(num==1):
        return 1
    else:
        return (fibonacci(num-1)+fibonacci(num-2))
                                      
n=6
print(fibonacci(n))
print(count)