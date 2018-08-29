def areFollowingPatterns(strings, patterns):
    HT={}
    for i in range(len(strings)):
        if strings[i] not in HT:
            if patterns[i] in HT.values():
                return False
            HT[strings[i]]=patterns[i]
        else:
            if HT[strings[i]]!= patterns[i]:
                return False
    return True
"I have found someone called(KOTTENATOR) making a good solution :"
def areFollowingPatterns(strings, patterns):
    return len(set(strings)) == len(set(patterns)) == len(set(zip(strings, patterns)))
"""
Assum that:
strings=[1,2,4,7,4]
patterns=[2,3,4,8,8]
here len(set(strings)) = len(set(patterns)) =4
but index 2 and 4 in string not following the value of the patterns in the same index
thar's why he have used zip
zip(strings, patterns): returns object of tuples having:
(1,2),(2,3),(4,4),(7,8),(4,8)
where the lenght of it's set=5
"""
