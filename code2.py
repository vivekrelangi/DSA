import sys
sys.setrecursionlimit(10000)
def code2(num):
    global memo
    if(num<=2):
        return 1
    if(memo.get(num)!=None):
        return memo[num]
    else:
        val=code2(num-1)+code2(num-2)
        memo.update({num:val})
        return memo[num]
memo={}
print(code2(10000))