# -*-coding:utf-8-*-
import zipfile, os

def main():
    
    file = "test.zip"
    pwd = bytes(123)
    with zipfile.ZipFile('test.zip') as testZip:
        with testZip.open('test.txt', pwd=bytes('123', 'utf-8')) as testFile:
            print(testFile.read())

print(main())