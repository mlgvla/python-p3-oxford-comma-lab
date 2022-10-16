def oxford_comma(items):
    last_element = items[-1]
    modified_list = items[0:-1]

    if len(items) == 1:
        return "".join(items)
    elif len(items) == 2:
        return ", ".join(modified_list) + " and " + last_element
    else:
        return ", ".join(modified_list) + ", and " + last_element
