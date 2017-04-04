def pig_it(text):
    text = text.split(" ")
    result = []

    for word in text:
        result.append(pig_word(word))
    
    return " ".join(result)
    
def pig_word(word):
    if word.isalpha():
        return word[1:] + word[:1] +  "ay"
    else:
        return word
