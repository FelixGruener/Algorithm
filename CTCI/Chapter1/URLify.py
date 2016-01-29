#Q1.3 URLify change all the spaces in a string with "%20"

# two pass, 
# one pass collapse all the consecutive multiple spaces into a single space
# second pass replace all the space with "%20"

def trimLeadingSpaces(str):
    if str.startswith("  "):
        return trimLeadingSpaces(str[1:])
    return str

def URLify(str):
    str = trimLeadingSpaces(str)
    if str.startswith(" "):
        return "%20" + URLify(str[1:])
    for i in range(len(str)):
        if str[i] == " ":
            return str[:i] + URLify(str[i:])
    return str  
        
        
testString = "   abc  dedf   degaf"
testString2 = "ab   dsdad  asdd asdwf"
print URLify(testString)
print URLify(testString2)