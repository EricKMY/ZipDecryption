# -*-coding:utf-8-*-

f = open('passwordDict.txt', 'w')

for pwdLen in range(8):
    for i in range(10**(pwdLen+1)):
            f.write(str(i).zfill(pwdLen+1) + '\n') # zfill for fill in zero to fit length ex.123 -> 00123