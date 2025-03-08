import sys
sys.setrecursionlimit(10000)
def code3(num):
    global memo
    if(num<=2):
        return 1
    if(memo.get(num)!=None):
            return memo[num]
    for n in range(2,num+1):
        val=code3(n-1)+code3(n-2)
        memo.update({n:val})
    return memo[num]
memo={}
print(code3(10001))