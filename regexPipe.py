import re


regexPattern = re.compile(r"Bat(man|car|copter)(sexy)*|Cat(wo)?man")
# (?) means match none or one
# (*) means match none or more
# (+) means match one or more
# 
matchObj = regexPattern.search("I want to be Batcarsexysexysexy but not Catwoman")
matchObj2 = regexPattern.search("Idk why but i want to be Catwoman and not Batman")
print(f"found: {matchObj.group()}")
print(f"second found: {matchObj2.group()}")