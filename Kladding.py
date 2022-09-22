en_til_hundre = list(range(1,101,2))
primtall = [2, 3, 5, 7]
for num in en_til_hundre:
    if num % 2 != 1:
        if num in en_til_hundre and num not in primtall:
            en_til_hundre.remove(num)
    elif num % 3 == 0:
        if num in en_til_hundre and num not in primtall:
            en_til_hundre.remove(num)
    elif num % 5 == 0:
        if num in en_til_hundre and num not in primtall:
            en_til_hundre.remove(num)
    elif num % 7 == 0:
        if num in en_til_hundre and num not in primtall:
            en_til_hundre.remove(num)


print(en_til_hundre)

def procedure_GCD(a,b):
    x = a
    y = b
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

