#Finds most optimal partner, Proposal problem uses gale-shapley algorithm


import sys

input_val = open("input_a1.txt")

dict_blue = dict()
dict_pink = dict()

def find_partner(dict_match, val):
    for k,v in dict_match.items():
        print(k,v)
        if k == val:
            return k
        


while True:

    read_proposer = input_val.readline().strip("\n")

    if read_proposer == "0":
        break

    for i in range(int(read_proposer)): #Blue
        
        val = input_val.readline().strip("\n")
        new_list = [int(i) for i in val.split()]
        dict_blue[i+1] = ["$"] + new_list
        
    for i in range(int(read_proposer)): #Pink
        
        val = input_val.readline().strip("\n")
        new_list = [int(i) for i in val.split()]
        dict_pink[i+1] = ["$"] + new_list


free_blue = []
free_pink = []
for i in range(len(dict_blue)+1):
    if len(free_blue) == 0:
        free_blue.append("$")
        free_pink.append("$")
    else:
        free_blue.append(True)
        free_pink.append(True)


dict_match = dict()

while True in free_blue:
    for male in dict_blue:
        print(male, "male", iter)
        if free_blue[male]:
            pref = dict_blue[male][1]
            if free_pink[pref]:
               dict_match[male] = pref
               free_blue[male] = False
               free_pink[pref] = False
               val = dict_blue[male].pop(1)
            else:
                current_engage = find_partner(dict_match, pref)
                engagement_index = dict_pink[pref].index(current_engage) # Both of these can be a function
                new_engagement = dict_pink[pref].index(male) #

                print("current_engage",current_engage,"engagement_index", engagement_index)
                if new_engagement < engagement_index:
                    pass
                break

            # else:
            #     current_engage = dict_match[pref]
            #     engagement_index = dict_pink[pref].index(current_engage)
            #     new_engagement = dict_pink[pref].index(male) # 2:1
                
            #     print(current_engage,"current_engage")


            #     if new_engagement < engagement_index:
            #         dict_match[male] = pref
            #         free_blue[male] = False
            #         free_blue[pref] = True
            #         dict_match[pref] = None
            #         print(pref, "pref")
            #         dict_pink[pref].remove(current_engage)
            #     else:
            #         pass





                print(new_engagement, "new_engagement")
                print(engagement_index)
    break 
print(dict_match, "dict_match")
print(free_blue, "free_blue")
print(dict_blue, "dict_blue")
print(dict_pink, "dict_pink")



    
# length = len(dict_blue)
# #while False in free_blue:
# for k,v in dict_blue.items():
#     if free_blue[k]:
#         first = v[0]
#         print(first)
#         print(free_pink, 'free')
#         if free_pink[first]:
#             dict_match[first] = int(k)
#             free_pink[first] = False
#             free_blue[k] = False
                
#         else:
#             find_engage = dict_match[first] #finds who the engagement is
#             print(find_engage, "find")
#             engagement_index = dict_pink[first].index(find_engage) #-1 because lists are fucked I need to fix it
#             print(engagement_index, "engagement_index")
#             current_index = 1            
                

# print(dict_match)
                    
        
            
            
        
    
