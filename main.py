import os, sys

def encode(text):
    arr = []
    for i in text:
        if i == " ": arr.append("*")
        elif i.isupper(): arr.append(f"{(int(hex(ord(i)), 16) - int('0x40', 16))*'+'}@")
        elif i.islower(): arr.append(f"{(int(hex(ord(i)), 16) - int('0x60', 16))*'+'}#")
        elif i.isdigit:
            var = "+"*int(i) + "&!"
            arr.append(var)
    arr.append(".;")
    return ''.join(arr)

def decode(text):
    value = 0
    arr = []
    for i in text:
        if i == "+": value += 1
        elif i == "-": value -= 1
        elif i == ".":
            print(''.join(arr))
            arr = []
        elif i == "#":
            arr.append(chr(0x60+value))
            value = 0
        elif i == "@":
            arr.append(chr(0x40+value))
            value = 0
        elif i == ";": quit()
        elif i == "*": arr.append(" ")
        elif i == "!": value = 0
        elif i == "&": arr.append(str(value))
    return

if __name__ == "__main__":
    if sys.argv[1] == "encode": print(encode(sys.argv[2]))
    elif sys.argv[1] == "decode": decode(sys.argv[2])
    else: print(f"Invalid arguments\nUsage: {sys.argv[0]} <encode/decode> <string>")