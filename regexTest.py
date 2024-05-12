from cgitb import text
import re

#parentheses make the output text divide to groups we can call seperatly
phoneRegexPattern = re.compile(r"(\d{3})-(\d{3}-\d{4})") 
phoneRegexPattern2 = re.compile(r"(\(\d{3}\)) (\d{3}-\d{4})")
# (\d{3,6}) will find the longest string of numbers within 3-6
# (\d{3,6}?) will find the shortest string or numberswithin the 3-6 character range 
matchedObjects = phoneRegexPattern.search("BRBRBWMj415-555-4242fefe")
matchedObjects2 = phoneRegexPattern2.search("BRBRBWMj(415) 555-4242fefe")
areaCode, phoneNumber = matchedObjects.groups()
areaCode2, phoneNumber2 = matchedObjects2.groups()
#if we out 1 inside it returns the first parentheses content same goes for 2
print(f"Phone number found: {matchedObjects.group(0)}.")
print(f"Phone number: {phoneNumber}\nArea code: {areaCode}")
print(f"Area code: {areaCode2} Phone number: {phoneNumber2}")


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
 # has groups
objtes = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
for i in objtes:
    print("-".join(i))