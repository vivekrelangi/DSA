#lex_auth_0127667392950599683407
# def find_maximum_activities(activity_list,start_time_list, finish_time_list):
#     #Remove pass and write your logic here
#     diffs = dict()
#     for indx,val in enumerate(start_time_list):
#         diffs[activity_list[indx]] = abs(val-finish_time_list[indx])
def find_maximum_activities(activity_list,start_time_list, finish_time_list):
    #Remove pass and write your logic here
    length = len(activity_list)
    performed_activities = []
    # activities= sorted([[activity_list[index],start_time_list[index],finish_time_list[index]] for index in range(length)],key = lambda x:x[2])
    activities = []
    for index in range(length):
       activities.append([activity_list[index], start_time_list[index], finish_time_list[index]])
    activities = sorted(activities,key=lambda x:x[2])
    print('log: ',activities,performed_activities)
    end_time = -1
    for activity in activities:
        if activity[1] > end_time:
          performed_activities.append(activity[0])
          end_time = activity[2]
    return performed_activities 
    
    
        
    

#Pass different values to the function and test your program
activity_list=[1,2,3,4,5,6]
start_time_list=[5, 4, 8, 2, 3, 1]
finish_time_list= [13, 6, 16, 7, 5, 4]
print("Activities:",activity_list)
print("Start time of the activities:",start_time_list)
print("Finishing time of the activities:", finish_time_list)

result=find_maximum_activities(activity_list,start_time_list, finish_time_list)
print("The maximum set of activities that can be completed:",result)