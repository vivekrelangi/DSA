

"""def merge_list(list1, list2):
    merged_data=""
    #write your logic here
    list2=list2[::-1]
    for i in range(len(list1)):
        if list1[i] == None and list2[i] == None:
            continue
        elif list1[i] == None:
            merged_data+=list2[i]
            if i != len(list1)-1:
                merged_data+=" "
        elif list2[i] == None:
            merged_data += list1[i]
            if i != len(list1)-1:
                merged_data+=" "
        else:
            merged_data+=list1[i]
            merged_data+=list2[i]
            if i != len(list1)-1:
                merged_data+=" "
    resultant_data = merged_data
    return resultant_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data,"end")"""
"""class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))

class Service:
    def __init__(self, car_list):
        self.__car_list=car_list

    def get_car_list(self):
        return self.__car_list
    
    def find_cars_by_year(self, year):
        ret=[]
        for car in self.__car_list:
            if car.get_year() == year:
                ret.append(car.get_model())
        if ret == []:
            return
        else:
            return ret

    def add_cars(self, new_car_list):
        self.__car_list+=new_car_list
        years={}
        # temp=[]
        # count=0
        for car in self.__car_list:
            years[car.get_year()]=[]
            #count+=1
        for year in years.keys():
            for car in self.__car_list:
                if car.get_year() == year:
                    years[year].append(car)
        #sorted(years.values())
        self.__car_list=[]
        for year in sorted(years.keys()):
            for car in years[year]:
                self.__car_list.append(car)
        return self.__car_list
    
    def remove_cars_from_karnataka(self):
        temp=[]
        for car in self.__car_list:
            if car.get_registration_number().startswith("KA"):
                pass
            else:
                temp.append(car)
        self.__car_list=temp
        return self.__car_list

#Implement Service class here

car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4,car5]
#Create object of Service class, invoke the methods and test your program
s=Service(car_list)
car6=Car("Tata", 2024,"AP39 5555")
car7=Car("Mahindra", 2023,"AP39 7777")
new_list=[car6, car7]
added=s.add_cars(new_list)
y=[]
for car in added:
    y.append(car.get_year())
print(y)
afterremove=s.remove_cars_from_karnataka()
reg=[]
for car in afterremove:
    reg.append(car.get_registration_number())
print(reg)"""
"""def check_double(list1,list2):
    new_list=[]
    #write your logic here
    for i in list1:
        if i*2 in list2:
            new_list.append(i)
    return new_list

#Provide different values for the variables and test your program
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
print(check_double(list1, list2))"""
class Player:
    def __init__(self,name,experience):
        self.__name=name
        self.__experience=experience

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def __str__(self):
        return(self.__name+" "+(str)(self.__experience))

#Implement Game class here
class Game:
    def __init__(self, players_list):
        self.__players_list=players_list

    def sort_players_based_on_experience(self):
        d={}
        for player in self.__players_list:
            d[player.get_experience()]=[]
        for key in d.keys():
            for player in self.__players_list:
                if key == player.get_experience():
                    d[key].append(player)
        temp=[]
        for key in sorted(d.keys())[::-1]:
            for player in d[key]:
                temp.append(player)
        self.__players_list=temp
        return self.__players_list
    
    def shift_player_to_new_position(self, old_index_position, new_index_position):
        p=self.__players_list.pop(old_index_position)
        self.__players_list.insert(new_index_position, p)
        return self.__players_list
    
    def display_player_details(self):
        self.shift_player_to_new_position(0,3)
        details=[]
        for player in self.__players_list:
            details.append([player.get_name(),player.get_experience()])
        print(details)

player1=Player("Dhoni",15)
player2=Player("Virat",10)
player3=Player("Rohit",12)
player4=Player("Raina",11)
player5=Player("Jadeja",13)
player6=Player("Ishant",9)
player7=Player("Shikhar",8)
player8=Player("Axar",7.5)
player9=Player("Ashwin",6)
player10=Player("Stuart",7)
player11=Player("Bhuvneshwar",5)
#Add different values to the list and test the program
players_list=[player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11]
#Create object of Game class, invoke the methods and test your program
g=Game(players_list)
sortedplayers=g.sort_players_based_on_experience()
exp=[]
for player in sortedplayers:
    exp.append(player.get_experience())
print(exp)
# shifted=g.shift_player_to_new_position(0,3)
# l=[]
# for player in shifted:
#     l.append(player.get_experience())
# print(l)
g.display_player_details()