def isAnagram(str1, str2):
    if len(str1) != len(str2):
        return 'not an anagram'
    if sorted(str1) == sorted(str2):
        return 'Its an anagram'

    return 'not an anagram'


s3 = 'decimal'
s4 = 'medical'


# print(isAnagram(s3, s4))
# print(isAnagram('akib', s4))


def isAnagramV2(str1, str2):
    if len(str1) != len(str2):
        return 'not an anagram'

    for w in str1:
        if w not in str2:
            # print(w)
            return 'no an anagram'
    else:
        return 'Anagram!!!'


print(isAnagramV2('love', 'voel'))
print(isAnagramV2('loves', 'voelw'))
