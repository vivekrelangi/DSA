import sys
sys.setrecursionlimit(10000)
def code1(num):
    if(num<=2):
        return 1
    else:
        return (code1(num-1)+code1(num-2))
print(code1(49))