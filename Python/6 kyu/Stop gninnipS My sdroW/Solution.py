def spin_words(sentence):
    words = sentence.split()
    newWords = []
    
    #Parse sentence into individual words.
    for word in words:
        #If word is of length 5 or greater, reverse the word.
        if(len(word)>4):
            newWord = word[-1:]
            for word_i in range(1,len(word)):
                newWord += word[len(word)-word_i-1:len(word)-word_i]
            word = newWord
            #Place reversed words in new array for return.
            newWords.append(word)
        else:
            #Place nonreversed words in array for return.
            newWords.append(word)
    #Join array of newWords into a string using a space delimeter.
    return " ".join(newWords)
