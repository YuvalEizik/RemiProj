''' todo
add restriction to table permutation: is valid serial 
make sure copying all objects when adding them
after adding card to table check for each one if it has any matches
'''
from abc import ABC, abstractmethod
import copy

class card:    
    def __init__(self,number,color,is_joker):
        self.number=number
        self.color=color
        self.is_joker=is_joker      
    
class table:
    def __init__(self,groups):
        self.groups=groups

class group(ABC):
    def __init__(self,cards):
        self.cards=cards

    @abstractmethod
    def is_valid(self):
        return

class run(group):#same number    
    def is_valid(self,cards):
        super().is_valid()      
        return all_numbers_are_the_same(cards) and all_colors_are_different(cards)

def all_numbers_are_the_same(cards):
    for i in range(len(cards)-1):
        if cards[i].number!=cards[i+1].number:
            return False
    return True

def all_colors_are_different(cards):
    for i in range(len(cards)-1):
        if cards[i].color==cards[i+1]:
            return False
    return True

class meld(group):
    def is_valid(self,cards):
        super().is_valid()
        return cards_going_up(cards) and all_colors_are_the_same(cards)

def cards_going_up(cards):
    numbers=get_cards_numbers(cards)
    numbers.sort()
    for i in range(len(numbers)-1):
        if numbers[i]+1!=numbers[i+1]:
            return False
    return True

def get_cards_numbers(cards):    
    return [card.number for card in cards]

def all_colors_are_the_same(cards):
    for i in range(len(cards)-1):
        if cards[i].color!=cards[i+1].color:
            return False
    return True

def get_your_cards_input():
    your_cards_input=input('enter your cards: <number1>:<color1>,<number2>:<color2> (<j>,<j2> if joker) (1:black,2:blue,3:red,4:yellow)')
    return get_list_of_cards_by_input(your_cards_input)

def get_list_of_cards_by_input(cards):
    output_cards=[]
    cards_splited_list=cards.split(',')
    for card in cards_splited_list:
        if card=='j':
            new_card=card(0,0,True)
        else:
            number_and_color_is_joker_splited_list=card.split(':')
            new_card=card(number_and_color_is_joker_splited_list[0],number_and_color_is_joker_splited_list[1],False)
        output_cards.append(new_card)      
            
    return output_cards

def get_table_cards_input():
    table_cards_input=input('enter table cards: <number1>:<color1>,<number2>:<color2> (<j>,<j2> if joker) (1:black,2:blue,3:red,4:yellow)')
    return get_list_of_cards_by_input(table_cards_input)

def get_cards_permutations(your_cards):    
    l=len(your_cards)
    if l==0:
        return []
    permutations=[]
    for i in range(1,l+1):    
        get_cards_permutation_helper(your_cards,permutations,[],i)
    return permutations

def get_cards_permutation_helper(your_cards,permutations,current_permutation,i):
    if i==len(current_permutation):
       permutations.append(current_permutation)
    for card in your_cards:
        if not card.id in get_ids(current_permutation):            
            newPermutation=copy.deepcopy(current_permutation)
            newPermutation.append(copy.deepcopy(card))
            get_cards_permutation_helper(your_cards,permutations,newPermutation,i)

def get_grouping_permutations(l):#make sure returning only valid groups where each group's len>=3
    if l<3:
        return []
    
    permutations=[]
    get_grouping_permutations_helper(l,[],permutations)

def get_grouping_permutations_helper(l,current_permutation,permutations):
    l_cur=len(current_permutation)
    if l_cur==0:
        rightest_gap=l
    else:
        rightest_cur_element=current_permutation[l_cur-1]
        rightest_gap=l-rightest_cur_element
    

def get_grouped_table_cards_permutations(table_cards_permutations_without_grouping, grouping_permutations):
    grouped_table_cards_permutations=[]
    for grouping_permutation in grouping_permutations:
        for table_cards_permutation_without_grouping in table_cards_permutations_without_grouping:
            grouped_table_cards_permutations.append(get_grouped_table_cards_permutation(table_cards_permutation_without_grouping, grouping_permutation))

def get_grouped_table_cards_permutation(table_cards_permutation_without_grouping, grouping_permutation):#[1,2,3,4,5,6,7,8,9],[3,6]->[[1,2,3],[4,5,6],[7,8,9]]
    l=len(table_cards_permutation_without_grouping)
    grouped_table_cards_permutation=[]
    last_index=0
    for number in grouping_permutation:
        new_group=table_cards_permutation_without_grouping[last_index:number+1]
        grouped_table_cards_permutation.append(new_group)
        last_index=number
    new_group=table_cards_permutation_without_grouping[last_index:l]
    grouped_table_cards_permutation.append(new_group)
    return grouped_table_cards_permutation


your_cards=get_your_cards_input()
table_cards=get_table_cards_input()
  
# print(is_move_valid(your_cards,table_cards))


# def get_ids(cards):
#     return [card.id for card in cards]

# def is_move_valid(your_cards,table_cards):
#     your_cards_permutations=get_cards_permutations(your_cards)
#     table_cards_permutations=get_cards_permutations(table_cards)
#     for your_cards_permutation in your_cards_permutations:
#         for table_cards_permutation in table_cards_permutations:
#             if your_cards_permutation_and_table_cards_permutation_is_valid(your_cards_permutation, table_cards_permutation):
#                 return True    
#     return False   
    

# def your_cards_permutation_and_table_cards_permutation_is_valid(your_cards_permutation, table_cards_permutation):
#     for group in table_cards_permutation:
#         for card in your_cards_permutation:
#             if can_insert_card_to_group(card,group):
#                 return True
#     return False

# def can_insert_card_to_group(card,group):
#     if group_is_a_serial(group):
        
#     else:

# def group_is_a_serial(group):
    
#     if theres_a_joker_in_group(group):
#         group_without_joker=get_group_without_joker(group)         
#         for i in range(len(group_without_joker-1)):
#             if group[i].number==group[i+1]:
#                 return False
#     else:
#         for i in range(len(group)-1):
#             if group[i].number==group[i+1]:
#                 return False

# def theres_a_joker_in_group(group):
#     for card in group:
#         if card.is_joker:
#             return True
#     return False

# def get_group_without_joker(group):
#     new_group=[]
#     for card in group:
#         if not card.is_joker:
#             new_group.append(copy.deepcopy(card))
#     return new_group         

# def get_table_cards_permutations(table_cards):
#     l=len(table_cards)
#     if l==0:
#         return []
#     table_cards_permutations_without_grouping=get_cards_permutations(table_cards)
#     grouping_permutations=get_grouping_permutations(l)
#     return get_grouped_table_cards_permutations(table_cards_permutations_without_grouping, grouping_permutations)

