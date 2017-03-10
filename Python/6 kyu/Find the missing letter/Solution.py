def find_missing_letter(chars):
    start = 0

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if(chars[0].istitle()):
        alphaString = " ".join(alphabet)
        alphaString = alphaString.upper()
        alphabet = alphaString.split(" ")

    for letter in range(0, len(alphabet)):
        if(alphabet[letter] == chars[0]):
            start = letter
    for char in chars:
        if(char == alphabet[start]):
            start += 1
        else:
            return alphabet[start]
