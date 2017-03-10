def is_valid_IP(strng):
    stringArray = strng.split(".")

    if(len(stringArray) != 4):
        return False

    for num in stringArray:
        if num[0] == "0":
            return False
        if not num.isdigit():
            return False
        if int(num) > 255:
            return False

    return True
