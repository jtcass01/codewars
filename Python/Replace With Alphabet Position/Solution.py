def alphabet_position(text):
    text = text.lower()
    result = ""

    for letter in text:
        if(letter.isalpha()):
            result += str(ord(letter)-96) + " "
    return result[:-1]
