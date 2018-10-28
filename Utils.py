def filter_char(str_raw, char_dest):
    list_str = list(str_raw)
    str_filtered = ''
    tmp = []
    length = len(list_str)
    if length <= 1:
        str_filtered = str_raw
        return str_filtered
    for i in range(length - 1):
        if list_str[i] != list_str[i + 1] or list_str[i] != char_dest:
            tmp.append(list_str[i])
    tmp.append(list_str[-1])
    str_filtered = ''.join(tmp)
    return str_filtered
# def log(str_content):

