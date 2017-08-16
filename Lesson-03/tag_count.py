def tag_count(string_list):
    count = 0
    for string in string_list:
        if (string[0] == "<") and (string[-1] == ">"):
            count += 1
    return count
    
    
    
    

# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))