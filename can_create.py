
def can_create(input_list, input_string):
    """
    :param input_list:  list of strings
    :param input_string: input string
    :return: true if True if input string can be created from the list of strings else false
    """
    can_create = False
    for element in input_list:
        if element in input_string:
            input_string = input_string.replace(element, "", 1)
            if len(input_string) == 0:
                can_create = True
                break
    return can_create


if __name__ == "__main__":

    input_string_list = input("Please enter a list of strings(seperated by a comma): ")
    input_list = list(filter(None, [x.strip() for x in input_string_list.split(',')]))

    print("List of strings = {}".format(input_list))

    input_string = input("Please enter input string : ")
    result = can_create(input_list, input_string)

    print("Result = {}".format(result))
