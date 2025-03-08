# Given a nested array of arbitrary depth, write a function that flattens it into a single-level array.
# example: 
# nestedArray = [1, [2, 3], [2, [4, [5]]], 5];
# Output: [1, 2, 3, 2, 4, 5, 5]
"""take input as """
def flatten(na):
    res=[]
    for i in na:
        if type(i) is int:
            res.append(i)
            # print(i,type(i))
        elif type(i) is list:
            # res.append(flatten(i))
            # print(i,type(i))
            temp=flatten(i)
            # print(temp)
            for i in temp:
                res.append(i)
    return list(set(res))

nestedArray = [1, [2, 3], [2, [4, [5]]], 5]
f=flatten(nestedArray)
print(f)
#you could have said that 