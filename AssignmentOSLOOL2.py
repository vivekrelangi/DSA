#Code I have written
# #lex_auth_0127667335697694723476

def merge_sort(num_list):
    # Remove pass and write the logic here to return the sorted list
    low = 0
    high = len(num_list)-1
    if(low == high):
        # print('num_list in if',num_list)
        return num_list
    else:
        mid = len(num_list)//2
        left_list = num_list[0:mid]
        right_list = num_list[mid:high+1]
        # print('divided lists',left_list,right_list)
        returned_left_list = merge_sort(left_list)
        returned_right_list = merge_sort(right_list)
        # print('returned lists',returned_left_list,returned_right_list)
        sorted_list = merge(returned_left_list,returned_right_list)
        # print('sorted list in else',sorted_list)
        return sorted_list


def merge(left_list,right_list):
    # Remove pass and write the logic to merge the elements in the left_list and right_list and return the sorted list
    i = 0
    j = 0
    sorted_list = []
    while(i< len(left_list) and j < len(right_list)):
        # print('sl:',sorted_list,i,j)
        if(left_list[i]<=right_list[j]):
            sorted_list.append(left_list[i])
            # print('while if ',sorted_list)
            i+=1
        else:
            sorted_list.append(right_list[j])
            # print('while else')
            j+=1
    while (i<len(left_list)):
        # print('i',i)
        sorted_list.append(left_list[i])
        # print('while while if i',sorted_list)
        i+=1
    while (j<len(right_list)):
        # print('j',j)
        sorted_list.append(right_list[j])
        # print('while while if j', sorted_list)
        j+=1
    return sorted_list

#Implement Item class here
class Item:
    # __item_name = None
    # __author_name = None
    # __published_year = None
    def __init__(self, item_name, author_name, published_year):
        self.__item_name = item_name
        self.__author_name = author_name
        self.__published_year = published_year
    
    def get_item_name(self):
        return self.__item_name
    
    def get_author_name(self):
        return self.__author_name
    
    def get_published_year(self):
        return self.__published_year
    
    def __str__(self):
        return ('Name: '+self.__item_name+'------Author: '+self.__author_name+'------Published Year: '+str(self.__published_year))

#Implement Library class here
class Library:
    # __item_list = None
    def __init__(self, item_list):
        self.__item_list = item_list

    def get_item_list(self):
        return self.__item_list
    
    def sort_item_list_by_author(self, new_item_list):
        # alpha_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
        # for item in new_item_list:
        #     a_name = item.get_author_name()
        #     if a_name[0] not in ['[@_!#$%^&*()<>?/\|}{~:] ']:
        #         a
        author_name_list=[]
        for item in new_item_list:
            a_name = item.get_author_name()
            if a_name[0] not in ['[@_!#$%^&*()<>?/\\|}{~:] ']:
                author_name_list.append(a_name)
            else:
                author_name_list.append(a_name[1:len(a_name)])
        sorted_list = []
        for author in merge_sort(author_name_list):
            for item in new_item_list:
                if item.get_author_name() == author:
                    sorted_list.append(item)
        return sorted_list

    def add_new_items(self, new_item_list):
        self.__item_list.extend(new_item_list)
        self.__item_list = self.sort_item_list_by_author(self.__item_list)

    def sort_items_by_published_year(self):
        # self.__item_list.sort(item.get_published_year)
        # published_years = []
        # for item in self.__item_list:
        #     published_years.append(item.get_published_year())
        # sorted_published_years = merge_sort(published_years)
        # sorted_item_list =[]
        # for sorted_p_year in sorted_published_years:
        #     for item in self.__item_list:
        #         if item.get_published_year() == sorted_p_year and item not in sorted_item_list:
        #             sorted_item_list.append(item)
        # counts_of_sorted_list = []
        # for spy in sorted_published_years:
        #     counts_of_sorted_list.append(sorted_published_years.count(spy))
        # for i in range(len(sorted_published_years)):
        #     if counts_of_sorted_list[i] > 1:
        yearanditemdict = dict()
        for item in self.__item_list:
            p_year = item.get_published_year()
            if p_year in yearanditemdict.keys():
                yearanditemdict[p_year].append(item)
            else:
                yearanditemdict[p_year] = [item]
        sorted_list_by_year_and_then_author = []
        for k,v in yearanditemdict.items():
            if len(v) > 1:
                yearanditemdict[k] = self.sort_item_list_by_author(v)
                sorted_list_by_year_and_then_author.extend(yearanditemdict[k])
            else:
                sorted_list_by_year_and_then_author.extend(yearanditemdict[k])
        keys_list = list(yearanditemdict.keys())
        # print(list(keys_list))
        sorted_keys_of_dict = merge_sort(keys_list) 
        final_list = []
        for s_key in sorted_keys_of_dict:
            final_list.extend(yearanditemdict[s_key])
        self.__item_list = final_list
        

                


#Use different values for item and test your program
item1=Item("A Mission In Kashmir","Andrew Whitehead",1995)
item2=Item("A Passage of India","E.M.Forster",2012)
item3=Item("A new deal for Asia","Mahathir Mohammad",1999)
item4=Item("A Voice of Freedom","Nayantara Sehgal",2001)
item5=Item("A pair of blue eyes","Thomas Hardy",1998 )

item_list=[item1,item2,item3,item4,item5]
library=Library(item_list)
print("The current items in the library are:")
for item in library.get_item_list():
    print(item)

item11=Item("Broken Wing","Sarojini Naidu",2012)
item12=Item("Guide","R.K.Narayanan",2001)
item13=Item("Indian Summers","John Mathews",2001)
item14=Item("Innocent in Death","J.D.Robb",2010)
item15=Item("Life of Pi","Yann Martel",2010 )
item16=Item("Sustainability","Johny",2016)
item17=Item("Look Ahead","E.M.Freddy",2012 )

new_item_list=[item11,item12,item13,item14,item15,item16,item17]
print()
print("The new items to be added are:")
for item in new_item_list:
    print(item)

new_item_list_sorted=library.sort_item_list_by_author(new_item_list)
print()
print("The new items after sorting based on the author name are:")
for item in new_item_list_sorted:
    print(item)

library.add_new_items(new_item_list_sorted)
print()
print("The final set of items after adding the new item list are:")
for item in library.get_item_list():
    print(item)

library.sort_items_by_published_year()
print()
print("The items sorted based on the increasing order of their published year:")
for item in library.get_item_list():
    print(item)

#Code Copied
# class Item:
#     def __init__(self,item_name,author_name,published_year):
#         self.__item_name = item_name
#         self.__author_name = author_name
#         self.__published_year = published_year
#     def get_item_name(self): return self.__item_name
#     def get_author_name(self): return self.__author_name
#     def get_published_year(self): return self.__published_year
#     def __str__(self): return ('------'+self.get_item_name()+'---|---'+self.get_author_name()+'---|---'+str(self.get_published_year())+'---|---')

# #Implement Library class here
# class Library:
#     def __init__(self,item_list): self.__item_list = item_list
#     def get_item_list(self): return self.__item_list
#     def sort_item_list_by_author(self,new_item_list):
#         authtobook_dict = dict()
#         for book in new_item_list: authtobook_dict[''.join([letter for letter in book.get_author_name() if letter.isalpha()])] = book
#         sorted_author = sorted(authtobook_dict.keys())
#         return [authtobook_dict[author] for author in sorted_author]
#     def add_new_items(self,new_item_list):
#         self.get_item_list().extend(new_item_list)
#         self.__item_list = self.sort_item_list_by_author(self.get_item_list())
#     def sort_items_by_published_year(self):
#         yeartobook_dict = dict()
#         for book in self.__item_list:
#             year = book.get_published_year()
#             if year in yeartobook_dict: yeartobook_dict[year].append(book)
#             else: yeartobook_dict[year] = [book]
#         sorted_based_on_year = []
#         for year in sorted(yeartobook_dict.keys()):
#             sorted_based_on_year.extend(self.sort_item_list_by_author(yeartobook_dict[year]))
#         self.__item_list = sorted_based_on_year

# #Use different values for item and test your program
# item1=Item("A Mission In Kashmir","Andrew Whitehead",1995)
# item2=Item("A Passage of India","E.M.Forster",2012)
# item3=Item("A new deal for Asia","Mahathir Mohammad",1999)
# item4=Item("A Voice of Freedom","Nayantara Sehgal",2001)
# item5=Item("A pair of blue eyes","Thomas Hardy",1998 )

# item_list=[item1,item2,item3,item4,item5]
# library=Library(item_list)
# print("The current items in the library are:")
# for item in library.get_item_list():
#     print(item)

# item11=Item("Broken Wing","Sarojini Naidu",2012)
# item12=Item("Guide","R.K.Narayanan",2001)
# item13=Item("Indian Summers","John Mathews",2001)
# item14=Item("Innocent in Death","J.D.Robb",2010)
# item15=Item("Life of Pi","Yann Martel",2010 )
# item16=Item("Sustainability","Johny",2016)
# item17=Item("Look Ahead","E.M.Freddy",2012 )

# new_item_list=[item11,item12,item13,item14,item15,item16,item17]
# print()
# print("The new items to be added are:")
# for item in new_item_list:
#     print(item)

# new_item_list_sorted=library.sort_item_list_by_author(new_item_list)
# print()
# print("The new items after sorting based on the author name are:")
# for item in new_item_list_sorted:
#     print(item)

# library.add_new_items(new_item_list_sorted)
# print()
# print("The final set of items after adding the new item list are:")
# for item in library.get_item_list():
#     print(item)

# library.sort_items_by_published_year()
# print()
# print("The items sorted based on the increasing order of their published year:")
# for item in library.get_item_list():
#     print(item)
     