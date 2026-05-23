def changeTheCase(s):
    result = ""
    for i in s:

        if i.islower():
            result = result + i.upper()

        if i.isupper():
            result = result + i.lower()
    return result

inp = input("Enter String:")
print("String after change lower case to upper and vice versa--")
print(changeTheCase(inp))