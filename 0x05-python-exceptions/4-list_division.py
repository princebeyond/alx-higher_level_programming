#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lists = []
    for i in range(list_length):
        try:
            if isinstance(my_list_1[i], (int, float)) and
            isinstance(my_list_2[i], (int, float)):
                div = my_list_1[i] / my_list_2[i]
                lists.append(div)
            else:
                print("wrong type")
                lists.append(0)
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            None
    return lists
