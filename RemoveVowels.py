def removeVowels(s):
    result = ""
    li = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(s)):
        if s[i] in li:
            result = result + ""
        else:
            result = result + s[i]
    return result

inp = input("Enter String: ")
print("Result: ", removeVowels(inp))