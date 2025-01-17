teststr = "corctf{aaaaaaaaaaaaaaaaaaaa}"
print(len(teststr))

# corctf{aaaaaaaaaaaaaaaaaaaa}


def isPrime(n):
    if(n < 2):
        return 0
    i = 2
    while i <= n/2:
        if (n % i == 0):
            return False
        i += 1
    return 1


dest="ujp?_oHy_lxiu_zx_uve"



asciiupp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
asciilow = "abcdefghijklmnopqrstuvwxyz"
# def rot_n(a1, a2):
#     if (asciiupp.find(chr(a1))!= -1):   #65-90
#         return asciiupp[(a2+(a1)-65) % 26]
#     if (asciilow.find(chr(a1))!= -1):   #97-122
#         return asciilow[(a2+(a1)-97) % 26]
#     return a1


def reverse_rot_n(des, V6):
    index1 = asciiupp.find(chr(des))
    if (index1 != -1):  # 65-90
        temp1 = -V6+index1+65
        while(temp1 < 65):
            # temp1 += 26
            index1+=26
            temp1 = -V6+index1+65
        return temp1

    index2 = asciilow.find(chr(des))
    if (index2 != -1):  # 97-122
        temp2 = -V6+index2+97
        while(temp2 < 97):
            # temp2 += 26
            index2+=26
            temp2 = -V6+index2+97
        return temp2
    return des


s1 = []
for i in range(len(dest)):
    v6 = 4*i
    while (isPrime(v6) != 1):
        v6 += 1
    print( v6, end="  ")
    s1.append((reverse_rot_n(ord(dest[i]), v6)))
print("\n")

print(s1)
# print(len(s1))
for x in s1:
    print(chr(x), end="")