text = bytearray(b'41!ce1337')
array = bytearray(b'oI!&}IusoKs ?Ytr'[::-1])

for i in range(len(array)):
    array[i] ^= text[i % len(text)]

foo = array[::-1]
print(foo.decode())
# Deadbeef
# \xDE\xAD\xBE\xEF
# bytearray(b'something)


str= '\0R\u009c\u007f\u0016ndC\u0005î\u0093MíÃ×\u007f\u0093\u0090\u007fS}­\u0093)ÿÃ\f0\u0093g/\u0003\u0093+Ã¶\0Rt\u007f\u0016\u0087dC\aî\u0093píÃ8\u007f\u0093\u0093\u007fSz­\u0093ÇÿÃÓ0\u0093\u0086/\u0003q'
res=[]
for i in range (len(str)):
    res.append(hex(ord(str[i])))
    
print(res)
a = "".join(ele for ele in res)
print(a)

print(str.encode())

 
