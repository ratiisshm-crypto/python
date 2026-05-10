def reverse(s):

    n = len(s)

    li = list(s)

    for i in range(n//2):

        li[i], li[n-i-1] = li[n-i-1], li[i]

        return "".join(li)
    
inp = input("Enter String: ")

print(reverse(inp))
