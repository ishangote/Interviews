# Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.
# Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
# For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is No.
"""
Questions:
1. What about punctuations? eg; i've v/s ive -> it is punctuation sensetive
2. Can one word of magazine be used twice? -> No

Example:

magazine => 
two times three is not four
note => 
two times two is four

word_count = {
    two : 1
    times : 1
    three : 1
    is : 1
    not : 1
    four : 1
}

"""
from collections import Counter
def ransom_note(magazine, note):
    word_count = Counter(magazine)
    for word in note:
        if word not in word_count: return False
        if word_count[word] == 0: return False
        word_count[word] -= 1
    
    return True