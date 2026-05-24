def frequency(word):
    word = word.replace(" ","").lower() 

    counts = {}

    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
        
    return counts

def checkAnagrams(word1, word2):
    if frequency(word1) == frequency(word2):
        return True 
    else:
        return False
    
word1 = input("Enter the first word: ")
word2 = input("Enter second word: ")

print(checkAnagrams(word1,word2))