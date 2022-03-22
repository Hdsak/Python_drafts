def Pig_latin_sentence(sentence):
    temp = []
    for tmp in sentence.split():
        if tmp[0] in 'aeiou':
            temp.append(f'{tmp}way')
        else:
            temp.append(f'{tmp[1:]}{tmp[0]}ay')
    return ' '.join(temp)

print(Pig_latin_sentence("This is a test message"))
