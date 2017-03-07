def accum(s):
    result = ""

    #loop through string one letter at a time
    for letter in range(0, len(s)):
      #Add each letter to the start of its section as an uppercase
      result += s[letter:letter+1].upper()
      #Add additional lower case letters to each section depending on position
      for letter_i in range(0, letter):
          result += s[letter:letter+1].lower()
      #If not at end of string, add a hyphen between sections
      if(letter < len(s)-1):
          result += "-"
    return result
