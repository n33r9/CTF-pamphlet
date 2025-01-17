encode={}
encode['n']= "0000"
encode['s']= "0001"
encode['3']= "001"
encode['a']= "010"
encode['u']= "01100"
encode['l']= "01101"
encode['g']= "01110"
encode['o']= "01111"
encode['_']= "100"
encode['m']= "1010"
encode['i']= "1011"
encode['r']= "1100"
encode['T']= "11010"
encode['t']= "11011"
encode['h']= "1110"
encode['f']= "1111"
check="111001100111111111010010000010010110001100010100110101100001001100010011010111001111110010111101111101010"

print(encode)
# print(len(encode['l']))
flag=""
# count=0
start = 0
while start<= len(check):
    for key in encode:
        if (check.find(encode[key]) == 0):
            flag += key;
            start= len(encode[key])
            check=check[start:]
print(flag)



rule 

