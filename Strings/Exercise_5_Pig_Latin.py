def Pig_latin():
    word = input("English word to translate into Pig Latin: ")
    if word[0] in ["a", "e", "i", "o", "u"]:
        return word+"way"
    return f'{word[1:]}{word[0]}ay'



print(Pig_latin())
