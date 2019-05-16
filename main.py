# -*-coding:utf-8-*-
import zipfile, os

def main():
    
    filePath = 'test.zip'
    password = '123'

    with zipfile.ZipFile(filePath) as testZip:
        try:
            with testZip.open('test.txt',  pwd=bytes(password, 'utf-8')) as testFile:
                print('password: ' + password)
                print(testFile.read())
        except RuntimeError:
            print('wrong password')

print(main())