#lex_auth_0127667391112806403379

def find_matches(country_name):
    #Remove pass and write your logic here
    res=[]
    for match in match_list:
        if match.startswith(country_name):
            res.append(match)
    return res

def max_wins():
    #Remove pass and write your logic here
    """code that I written"""
    dres={}
    dres1={}
    cntryratios={}
    countries = []
    for match in match_list:
        splitedMatch = match.split(':')
        if (splitedMatch[0] not in countries):
            countries.append(splitedMatch[0])
    for country in countries:
        matches = find_matches(country)
        cntryratios[country]={}
        for match in matches:
            splitedMatch = match.split(':')
            if(splitedMatch[1] not in dres.keys()):
                dres[splitedMatch[1]] = []
                dres1[splitedMatch[1]] = 0
            # cntryratios[splitedMatch[0]].append({splitedMatch[1]:(int(splitedMatch[3])/int(splitedMatch[2]))})
            # cntryratios[splitedMatch[0]][splitedMatch[1]] = int(splitedMatch[3])/int(splitedMatch[2])
            cntryratios[splitedMatch[0]][splitedMatch[1]] = int(splitedMatch[3])
    for championship in dres1.keys():
        for cntry in countries: 
                if(championship in cntryratios[cntry].keys()):
                    # print(cntryratios[cntry][championship] , cntryratios[cntry])
                    # print(dres1[championship],cntryratios[cntry][championship])
                    if(dres1[championship] <= cntryratios[cntry][championship]):
                        dres1[championship] = cntryratios[cntry][championship] 
    # print(dres1)
    for championship in dres.keys():
        for cntry in countries:
            if(championship in cntryratios[cntry].keys()):
                if(dres1[championship] == cntryratios[cntry][championship]):
                    dres[championship].append(cntry)
    return dres
    """copied"""
    # match_dict = dict()
    # for match in match_list:
    #     temp = match.split(':')
    #     champ_name = temp[1]
    #     team_name = temp[0]
    #     matches_won = int(temp[3])
    #     if champ_name in match_dict:
    #         max_matches_won = match_dict[champ_name][-1]
    #         if max_matches_won < matches_won:
    #             match_dict[champ_name] = [team_name,matches_won]
    #         if max_matches_won == matches_won:
    #             match_dict[champ_name].insert(-2,team_name)
    #     else:
    #         match_dict[champ_name] = [team_name,matches_won]
    # for champ_name in match_dict:
    #     match_dict[champ_name].pop()
    # return match_dict
            
            

    # print(cntryratios,dres)
        # if(splitedMatch[1] not in dres.keys()):
        #     dres[splitedMatch[1]] 
    # for championship in list(set(match_dict["championship_name"])):
    #     dres[championship]=[]
    # print(dres)
    # cdict={}
    # for c in list(set(match_dict["country_name"])):
    #     cdict[c]=find_matches(c)
    # print(cdict)   

def find_winner(country1,country2):
    #Remove pass and write your logic here
    c1 = 0
    c2 = 0
    for match in match_list:
        splitedMatch = match.split(':')
        if(splitedMatch[0]==country1):
            c1 += int(splitedMatch[3])
        elif(splitedMatch[0]==country2):
            c2 += int(splitedMatch[3])
    if(c1>c2):
        return country1
    elif(c2>c1):
        return country2
    else:
        return "Tie"
    

#Consider match_list to be a global variable
# match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]
match_list = ['AUS:T20:5:3', 'IND:CHAM:5:3', 'AUS:WOR:2:0', 'CAN:CHAM:5:1', 'ENG:WOR:2:0', 'IND:T20:6:4', 'PAK:T20:4:3', 'IND:WOR:5:3', 'AUS:CHAM:1:0', 'PAK:CHAM:5:1', 'SA:CHAM:5:2', 'SA:T20:5:0', 'PAK:WOR:2:0']
# match_dict={"country_name":[],"championship_name":[],"total_number_of_matches_played":[],"number_of_matches_won":[]}
# for match in match_list:
#     slist=match.split(":")
#     match_dict["country_name"].append(slist[0])
#     match_dict["championship_name"].append(slist[1])
#     match_dict["total_number_of_matches_played"].append(slist[2])
#     match_dict["number_of_matches_won"].append(slist[3])
#Pass different values to each function and test your program
# print("The match status list details are:")
# print(match_list)
# print(match_dict)
print(max_wins())

# print(find_matches('IND'))
# print(max_wins())
# print(find_winner('AUS','IND'))

#Plan
"""save countries in a list
then, get matches of the coutries
then, for every champipionship of a country save ratio of wins and loses in a the cntryratios dict where key is country and value is another dictionary which
has key as championship names and value is their ratio
then, while setting cntryratios set dres with championship names"""