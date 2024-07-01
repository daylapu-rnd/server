import random
import string


def GenerateAlfNumStr(length, type_="all"):
    """Creating an alphanumeric, numeric, or alphanumeric string"""
    if type_ == "all":
        letters_and_digits = string.ascii_letters + string.digits
        rand_string = ''.join(random.sample(letters_and_digits, length))
        return rand_string
    elif type_ == "int":
        letters_and_digits = string.digits
        rand_string = ''.join(random.sample(letters_and_digits, length))
        return rand_string
    elif type_ == "str":
        letters_and_digits = string.ascii_letters
        rand_string = ''.join(random.sample(letters_and_digits, length))
        return rand_string
    else:
        return False


def creatDictFromLists(lis):
    resDict = {}
    try:
        for i in range(len(lis)):
            resDict[i] = lis[i]
        return resDict
    except Exception as e:
        return []


def string_to_list(user_ids_str):
    """Converts a string of user IDs to a list"""
    if not isinstance(user_ids_str, str):
        raise ValueError("Input should be a string")
    if user_ids_str:
        return user_ids_str.split(',')
    return []


def list_to_string(user_id_list):
    """Converts a list of user IDs to a string"""
    if not isinstance(user_id_list, list):
        raise ValueError("Input should be a list")
    if not all(isinstance(item, str) for item in user_id_list):
        raise ValueError("All items in the list should be strings")
    return ','.join(user_id_list)




