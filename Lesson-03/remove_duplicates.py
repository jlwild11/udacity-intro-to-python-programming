def remove_duplicates(a_list):
    new_list = []
    
    for item in a_list:
        if item not in new_list:
            new_list.append(item)
    
    return new_list


list1 = ["USA", "Brazil", "Mexico", "Canada"]
list2 = ["USA", "Brazil", "Mexico", "Canada", "Mexico", "Canada"]

print(remove_duplicates(list1))
print("next list")
print(remove_duplicates(list2))