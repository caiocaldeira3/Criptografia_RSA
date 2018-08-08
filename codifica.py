def codifica(a):
    result = 0
    i = 0
    for letter in a:
        result += 256**i * ord(letter)
        i += 1
    return result

a = input()
b = codifica(a)
print(b)
