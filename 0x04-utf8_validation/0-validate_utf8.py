#!/usr/bin/python3
"""UTF-8 Encoding Module"""


def validUTF8(data):
    """validate if data is utf-8 encoded"""
    for c in data:
        try:
            bytes([c]).decode('utf-8')
        except:
            return False
    return True
