#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        i = 0
        new_list = []
        while i < list_length:
            try:
                new_list.append(my_list_1[i] / my_list_2[i])
                i += 1
            except ZeroDivisionError:
                new_list.append(0)
                i += 1
                print("division by 0")
            except (ValueError, TypeError):
                new_list.append(0)
                i += 1
                print("wrong type")
    except IndexError:
        new_list.append(0)
        print("out of range")
    finally:
        return (new_list)
