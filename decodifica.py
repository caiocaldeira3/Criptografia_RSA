def decodifica(b):
    str = ''
    while b != 0:
        str = "%s%s" %(str, chr(b%256))
        b //= 256
    return str

b = int(input())
c = decodifica(b)
print(c)
