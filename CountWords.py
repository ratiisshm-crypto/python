def countWords(s):
    count = 0
    s = s.strip()
    for i in range(len(s)):
        if s[i] == " ":
            count+= 1

    return count + 1

inp = input("Enter String: ")
print("Number of words: ", countWords(inp))