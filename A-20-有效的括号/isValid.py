def isValid(s):
    brackesDict = {")": "(", "]":"[", "}":"{"}
    if len(s) == 0:
        return True
    if s[0] in brackesDict.keys():
        return False
    bracketArray = []
    for item in s:
        if item in brackesDict.values():
            bracketArray.append(item)
        elif item in brackesDict.keys():
            if len(bracketArray) == 0:
                return False 
            if not brackesDict.get(item) == bracketArray.pop():
                return False
    if not len(bracketArray) == 0:
        return False
    else:
        return True

print(isValid(""))