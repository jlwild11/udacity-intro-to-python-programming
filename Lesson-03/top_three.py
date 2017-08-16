def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
    sorted_list = sorted(input_list, reverse = True)
    return sorted_list[:3]


list = [1,2]

print(top_three(list))
