#!/usr/bin/python3
"""UTF-8 Encoding Module"""
import codecs

def validUTF8(data):
    """validate if data is utf-8 encoded"""
    try:
        filtered_data = [byte for byte in data if 0 <= byte <= 255]
        codecs.decode(bytes(filtered_data), 'utf-8')
        return True
    except UnicodeDecodeError:
        return False
