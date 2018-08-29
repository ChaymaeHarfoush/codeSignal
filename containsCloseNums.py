def containsCloseNums(nums, k):
    dct={}#key:number, value:index contains the last occurance index of a number
    if not nums or k==0:
        return False

    for index,num in enumerate(nums):
        try:
            if index-dct[num] <= k:
                return True
        except:
            pass
        dct[num]=index

    return False
