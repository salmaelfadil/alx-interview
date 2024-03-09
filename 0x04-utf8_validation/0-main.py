#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))
print ("should be true")
print("######")

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))
print ("should be true")
print("######")

data = [229, 65, 127, 256]
print(validUTF8(data))
print ("should be false")
print("######")

data =[467, 133, 108]
print(validUTF8(data))
print ("should be false")
print("######")

data = [240, 188, 128, 167]
print(validUTF8(data))
print ("should be true")
print("######")

data = [235, 140]
print(validUTF8(data))
print ("should be false")
print("######")

data = [345, 467]
print(validUTF8(data))
print ("should be false")
print("######")

data =  [250, 145, 145, 145, 145]
print(validUTF8(data))
print ("should be true")
print("######")

data = [0, 0, 0, 0, 0, 0]
print(validUTF8(data))
print ("should be true")
print("######")

data = []
print(validUTF8(data))
print ("should be true")
print("######")
