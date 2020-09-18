# Tuples as container
directions = (
    'north',
    'south',
    'east',
    'west',
    'down',
    'up',
    'left',
    'right',
    'back'
)


verbs = (
    'go',
    'stop',
    'kill',
    'eat'
)

stop = (
    'the',
    'in',
    'of',
    'from',
    'at',
    'it'
)

nouns = (
    'door',
    'bear',
    'princess',
    'cabinet'
)

numbers = range(-9999999, 9999999)

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

#Auto test
def scan(inputwords):
    words = inputwords.split()
    word_list = []

    for i in words:
        if i in directions:
            word_list.append(('direction', i))
            #print(word_list)

        elif i in verbs:
            word_list.append(('verb', i))
            #print(word_list)

        elif i in stop:
            word_list.append(('stop', i))
            #print(word_list)

        elif i in nouns:
            word_list.append(('noun', i))
            #print(word_list)

        elif convert_number(i) in numbers:
            word_list.append(('number', convert_number(i)))

        else:
            word_list.append(('error', i))

    return word_list
