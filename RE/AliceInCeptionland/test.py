def rol(v, s):
    b = s%8
    return ( ((v<<b)) | ( (v >> (8-b))) )


text = "c4t3rp1114rz_s3cr3t1y_ru13_7h3_w0r1d"

key = "\0R\u009c\u007f\u0016ndC\u0005î\u0093MíÃ×\u007f\u0093\u0090\u007fS}­\u0093)ÿÃ\f0\u0093g/\u0003\u0093+Ã¶\0Rt\u007f\u0016\u0087dC\aî\u0093píÃ8\u007f\u0093\u0093\u007fSz­\u0093ÇÿÃÓ0\u0093\u0086/\u0003q"

arr= []

for i in range(0, len(key)):
    arr.append(ord(key[i]))

arr.reverse()

print(len(arr))

print(arr)


list_result=[]
for i in range(0, len(arr), 1):
    # for item in listITEM:
    kytuthuI = []
    for item in range(47,122):
        b = item
        b = rol(b, 114)
        b&=0xff
        b += 222
        b&=0xff
        b = b ^ ord(text[i%len(text)])
        b -= 127
        b&=0xff
        b = rol(b, 6)
        b&=0xff
        if(b == arr[i]):
            kytuthuI.append(chr(item))
    
    list_result.append(kytuthuI)

print(list_result)
print("Len:", len(list_result))

soTruongHop = 1
for i in range(0, len(list_result)):
    soTruongHop*=len(list_result[i])

print("Sotruonghop", soTruongHop)


# \x4\xL\x1\xC\x3\x1\xS\xN\x0\xT\x4\xS\xL\x3\x3\xP\xS\x4\xV\x3\xH\x3\xR