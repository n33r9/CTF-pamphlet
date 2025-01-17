
key = 'oI!&}IusoKs ?Ytr'
rev_key = key[::-1]
print(rev_key)
print(len(key))
text1 = "41!ce1337"
res = []
for i in range(len(key)):
    res.append(ord(rev_key[i]) ^ ord(text1[i % len(text1)]))

# res= [70, 69, 120, 92, 69, 66, 120, 92, 68, 65, 120, 92, 69, 68, 120, 92]
for x in res[::-1]:
    print((chr(x)), end='')

# question1: \xDE\xAD\xBE\xEF


print('\n')


def rol(v, s):
    b = s % 8
    return (v << b) | (v >> (8-b))


text2 = "c4t3rp1114rz_s3cr3t1y_ru13_7h3_w0r1d"

encodedStr = "\0R\u009c\u007f\u0016ndC\u0005î\u0093MíÃ×\u007f\u0093\u0090\u007fS}­\u0093)ÿÃ\f0\u0093g/\u0003\u0093+Ã¶\0Rt\u007f\u0016\u0087dC\aî\u0093píÃ8\u007f\u0093\u0093\u007fSz­\u0093ÇÿÃÓ0\u0093\u0086/\u0003q"

# decodedstr = encodedStr.encode().decode()
# print(decodedstr)
a = []
for x in encodedStr[::-1]:
    # print(ord(x))
    a.append(ord(x))
print(len(a))
print(a)

list_result = []
for i in range(0, len(a), 1):
    # for item in listITEM:
    kytuthuI = []
    for item in range(47, 122):
        b = item
        b = rol(b, 114)
        b &= 0xff
        b += 222
        b &= 0xff
        b = b ^ ord(text2[i % len(text2)])
        b -= 127
        b &= 0xff
        b = rol(b, 6)
        b &= 0xff
        if(b == a[i]):
            kytuthuI.append(chr(item))

    list_result.append(kytuthuI)

print(list_result)
print("Len:", len(list_result))

soTruongHop = 1
for i in range(0, len(list_result)):
    soTruongHop *= len(list_result[i])

print("Sotruonghop", soTruongHop)


# \x4\xL\x1\xC\x3\x1\xS\xN\x0\xT\x4\xS\xL\x3\x3\xP\xS\x4\xV\x3\xH\x3\xR
