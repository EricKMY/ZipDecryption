# -*-coding:utf-8-*-
import zipfile, os

def main():
    
    filePath = 'test.zip'
    passwordDict = ['100', '111', '5559','151514','555','123']

    with zipfile.ZipFile(filePath) as testZip:
        for password in passwordDict: 
            try:
                with testZip.open('test.txt',  pwd=bytes(password, 'utf-8')) as testFile:
                    print('password: ' + password)
                    print(testFile.read())
                    break
            except RuntimeError:
                print('wrong password: ' + password)

print(main())