directions = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verbs = ('go', 'stop', 'kill', 'eat', 'open')
stop_words = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')

def get_tuple(word):
    test_word = word.lower()

    if test_word in directions:
        return ('direction', word)
    elif test_word in verbs:
        return ('verb', word)
    elif test_word in stop_words:
        return ('stop', word)
    elif test_word in nouns:
        return ('noun', word)
    elif test_word.isdigit():
        return ('number', int(word))
    else:
        return ('stop', word)

def scan(sentence):
    words = sentence.split()
    arr_elements = []
    for word in words:
        arr_elements.append(get_tuple(word))
    return arr_elements
