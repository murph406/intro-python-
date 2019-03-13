def returnKeys(enter_dict):
    list_keys = []
    for item in enter_dict:
        list_keys.append(item)
    return list_keys

def returnDivisibleValues(user_dict, num):
    user_list = []
    for key in user_dict:
        value = user_dict[key]
        if type(value) == int:
            if value % num == 0:
                user_list.append(value)
    return user_list

def returnEven(seq):
    num_elements = 0
    for item in seq:
        num_elements += 1
    if num_elements % 2 == 0:
        return True
    else:
        return False

def swapKeyValue(enter_dict):
    swapped_dict= {}
    for key in enter_dict:
        old_key = key
        old_value = enter_dict[key]
        new_value = old_key
        new_key = old_value
        swapped_dict[new_key] = new_value
    return swapped_dict


