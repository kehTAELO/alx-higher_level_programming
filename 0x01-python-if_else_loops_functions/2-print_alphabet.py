#!/usr/bin/python3
for letter in range (97, 122):
    if chr(letter) not in ['q', 'e']:
        print(chr(letter), end='')
