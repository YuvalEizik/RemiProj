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
    def is_valid(self):
        super().is_valid()      
        return all_numbers_are_the_same(self.cards) and all_colors_are_different(self.cards)

def all_numbers_are_the_same(cards):
    numbers=get_numbers_without_joker(numbers)
    for i in range(len(numbers)-1):
        if numbers[i].number!=numbers[i+1].number:
            return False
    return True

def all_colors_are_different(cards):
    
    for i in range(len(cards)-1):
        if cards[i].color==cards[i+1]:
            return False
    return True

class meld(group):
    def is_valid(self):
        super().is_valid()
        return cards_going_up(self.cards) and all_colors_are_the_same(self.cards)

def cards_going_up(cards):
    jokers_in_cards=get_jokers_in_cards(cards)
    numbers=get_numbers_without_joker(cards)
    numbers.sort()
    if jokers_in_cards==0:
        for i in range(len(numbers)-1):
            if numbers[i]+1!=numbers[i+1]:
                return False
        return True
    else:
        jokers_left=jokers_in_cards
        for i in range(len(numbers)-1):            
            if numbers[i]+1!=numbers[i+1]:
                jokers_left-=1
                if jokers_left==-1:
                    return False
    return True

def get_jokers_in_cards(cards):
    return len([card for card in cards if card.is_joker])

def all_colors_are_the_same(cards):
    colors=get_colors_without_jokers(cards)    
    for i in range(len(colors)-1):
        if colors[i]!=colors[i+1]:
            return False
    return True

def get_numbers_without_joker(cards):    
    return [card.number for card in cards if card.number!=0]

def get_colors_without_jokers(cards):
    return [card.color for card in cards if card.color!=0]

c1=card(1,1,False)
c2=card(1,2,False)
c3=card(1,3,False)
c4=card(2,1,False)
c5=card(3,1,False)
c6=card(0,0,True)

print(meld([c5,c3,c6]).is_valid())
# print(all_colors_are_the_same([c1,c4,c2]))





# from abc import ABC, abstractmethod
# import copy

# class group(ABC):
#     def __init__(self,input):
#         self.input=input

#     @abstractmethod
#     def is_valid(self):
#         return

# class run(group):#same number    
#     def is_valid(self):
#         super().is_valid()      
#         print(self.input)

# class meld(group):
#     def is_valid(self):
#         super().is_valid()      
#         print(self.input)

# r=meld('2')
# r.is_valid()

# # def get_table_cards_permutations(table_cards):
# #     for number in table_cards:
# #         yield number

# # for table_cards_permutation in get_table_cards_permutations([1,2,3]):
# #         # if your_cards_permutation_and_table_cards_permutation_is_valid(table_cards_permutation,your_cards_permutation):
# #     print(table_cards_permutation)


# # def get_your_cards_permutations(your_cards):
# #     l=len(your_cards)
# #     if l==0:
# #         return []
# #     for i in range(1,l+1):        
# #         for p in get_your_cards_permutation_helper(your_cards,[],i)]:
# #             yield p
# #     # return permutations

# # def get_your_cards_permutation_helper(your_cards,current_permutation,i):
# #     if i==len(current_permutation):
# #        yield current_permutation
# #     for card in your_cards:
# #         if not card.id in [currentCard.id for currentCard in current_permutation]:
# #             newPermutation=[card for card in current_permutation]
# #             newPermutation.append(card)
# #             get_your_cards_permutation_helper(your_cards,newPermutation,i)
    
# # for c in get_your_cards_permutations([1,2,3]):
# #     print(c)

# import copy

# class card:
#     currentId=0
#     def __init__(self,number,color,is_joker):
#         self.number=number
#         self.color=color
#         self.is_joker=is_joker
#         self.id=card.currentId
#         self.increase_id()
    
#     @classmethod 
#     def increase_id(cls):
#         cls.currentId+=1


# def get_your_cards_permutations(your_cards):    
#     l=len(your_cards)
#     if l==0:
#         return []
#     permutations=[]
#     for i in range(1,l+1):    
#         get_your_cards_permutation_helper(your_cards,permutations,[],i)
#     return permutations

# def get_your_cards_permutation_helper(your_cards,permutations,current_permutation,i):
#     if i==len(current_permutation):
#         permutations.append(current_permutation)
#     for card in your_cards:
#         if not card.id in get_ids(current_permutation):
#             # newPermutation=[card for card in current_permutation]
#             # newPermutation.append(card)
#             newPermutation=copy.deepcopy(current_permutation)
#             newPermutation.append(copy.deepcopy(card))
#             get_your_cards_permutation_helper(your_cards,permutations,newPermutation,i)

# def get_ids(cards):
#     return [card.id for card in cards]
    

# c1=card(1,1,False)
# c2=card(2,1,False)
# c3=card(3,1,False)
# cards=[c1,c2,c3]

# # print(get_ids(cards))
# print(get_your_cards_permutations(cards))

# # def get_your_cards_permutations(your_cards):    
# #     l=len(your_cards)
# #     if l==0:
# #         return []
# #     permutations=[]
# #     for i in range(1,l+1):    
# #         get_your_cards_permutation_helper(your_cards,permutations,[],i)
# #     return permutations

# # def get_your_cards_permutation_helper(your_cards,permutations,current_permutation,i):
# #     if i==len(current_permutation):
# #        permutations.append(current_permutation)
# #     for card in your_cards:
# #         if not card in current_permutation:
# #             # newPermutation=[card for card in current_permutation]
# #             # newPermutation.append(card)
# #             newPermutation=copy.deepcopy(current_permutation)
# #             newPermutation.append(copy.deepcopy(card))
# #             get_your_cards_permutation_helper(your_cards,permutations,newPermutation,i)

# # print(get_your_cards_permutations([1,2,3]))

