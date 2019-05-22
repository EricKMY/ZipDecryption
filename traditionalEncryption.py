# -*-coding:utf-8-*-

import zipfile

with zipfile.ZipFile('test.zip') as testZip:
    passwordDict = open('passwordDict.txt', 'r')
    password = passwordDict.readline()

    while password: 
        try:
            with testZip.open('test.txt',  pwd=bytes(password.replace('\n', ''), 'utf-8')) as testFile:
                print('correct password: ' + password)
                print(testFile.read())                 
                break

        except RuntimeError as e:
            print(e)
            print('password: ' + password)

        password = passwordDict.readline()

    passwordDict.close()