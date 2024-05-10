strs = ["flower","flow","flight"]
prefix = strs[0]
def loop(strs):
    for item in strs:
        if prefix in item[1:]:
            continue
        else:
            return False
    print("......")
    return True
def longestCommonPrefix(strs,prefix):
    for x in strs[0]:
        if loop(strs):
            break
        else:
            prefix = prefix[:-1]
        print(prefix)
    return prefix

prefix = longestCommonPrefix(strs,prefix)
print(str(prefix)+"....")