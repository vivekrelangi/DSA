def pattern_search(text, pattern):
    #Remove pass and write your logic here
    substrs=[]
    lp=len(pattern)
    lt=len(text)
    for i in range(lt):
        end=i+lp
        if end <= lt:
            if text[i:end] == pattern:
                substrs.append(text[i:end])
                print(end)
    if substrs == []:
        return 0
    else:
        return len(substrs)

#Use different values for text and pattern and test your program
text = "MESMERIZING MESSAGE"
pattern = "MES"
result=pattern_search(text, pattern)
print("The given text:",text)
print("Pattern:",pattern)
print("No. of occurrences of the pattern :",result)