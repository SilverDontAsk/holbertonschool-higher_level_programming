#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:  # this part gives n1 and n2 the list values
            n1 = my_list_1[i] if i < len(my_list_1) else None
            n2 = my_list_2[i] if i < len(my_list_2) else None
# this part checks if the values are divisible or not
            if n1 is None or n2 is None:
                raise IndexError("out of range")
            if not isinstance(n1, (int, float)):
                raise TypeError("wrong type")
            if not isinstance(n2, (int, float)):
                raise TypeError("wrong type")
            if n2 == 0:
                raise ZeroDivisionError("division by 0")
            div_result = n1 / n2
            result.append(div_result)
        except IndexError:   # error handling part
            result.append(0)
            print("out of range")
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except (TypeError, ValueError):
            result.append(0)
            print("wrong type")
        finally:  # this part is empty cause all the processes are done
            pass
    return result
