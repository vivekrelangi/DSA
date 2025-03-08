#lex_auth_0127667363860725763513

def arrange_tickets(tickets_list):
    #Remove pass and write your logic here
    # group1 = []
    # group2 = []
    # for i in range(1,11):
    #     group1.append('T'+str(i))
    # for j in range(11,21):
    #     group2.append('T'+str(j))
    # for ticket in 
    totaltickets = []
    for i in range(1,21):
        if 'T'+str(i) in tickets_list:
            totaltickets.append('T'+str(i))
        else:
            totaltickets.append('V')
    # for t in tickets_list:
    # #     if 
    # print(totaltickets)
    group1 = totaltickets[0:10]
    group2 = totaltickets[10:20]
    # group2 = group2[::-1]
    # filtered = []
    # for t in group2:
    #     if t != 'V':
    #         filtered.append(t)
    group2 = list(filter(lambda x: x != 'V', group2))
    group2=group2[::-1]
    # print('f',list(f))
    # print(group1,group2)

    for tind in range(len(group1)):
        # for t1ind in range(len(group2)):
        #     if group1[tind] == 'V':
        #         group1[tind] = group2
        if group1[tind] == 'V':
            group1[tind] = group2.pop()
            print('g',group1[tind])
    # print(group1)
    return group1

tickets_list = ['T5', 'T17', 'T10', 'T2', 'T9', 'T15', 'T17', 'T19', 'T16', 'T1', 'T12', 'T13']
print("Ticket ids of all the available students :")
print(tickets_list)
result=arrange_tickets(tickets_list)
print()
print("Ticket ids of the ten students in Group-1:")
print(result)