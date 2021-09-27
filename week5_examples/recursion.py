lst = ["diet coke", "rugby", "hiking", "pizza", "fajitas", "football", "basketball", "animals", "people"]

for item in lst:
    print(item)
    
    
print("--------")


def print_items(lst, idx):
    # base case
    if idx >= len(lst):
        return
    
    # print item / recursive
    print(idx, lst[idx])
    if idx == 0:
        idx = 2
    else:
        idx *= 2
        
    print_items(lst, idx)
    
    # return
    
print_items(lst, 0)