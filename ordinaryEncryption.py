# -*- coding:utf-8 -*-  

import os
import subprocess
import zipfile

def brutecrack():

    passwordDict = open('passwordDict.txt', 'r')
    password = passwordDict.readline()

    while password: 
        command = '7z -p' + password + ' t C:/Users/EricKuan/Desktop/OS/ZipDecryption/test.zip'  # t for testing password but not extract
        print(password)
        child = subprocess.call(command)
        print(child)

        if child == 0:
            print("correct password: " + password)
            break

        password = passwordDict.readline()

    passwordDict.close()

if __name__ == '__main__':
	brutecrack()