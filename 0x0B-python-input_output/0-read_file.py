#!/usr/bin/python3

def read_file(filename=""):
    with open('my_file_0.txt', "r", encoding="UTF-8") as f:
        print(f.read(), end="")
