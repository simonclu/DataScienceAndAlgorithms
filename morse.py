"""
Morse code key:
A: . ...
B: ... . . .
C: ... . ... .
D: ... . .
E: .
F: . . ... .
G: ... ... .
H: . . . .
I: . .
J: . ... ... ...
K: ... . ...
L: . ... . .
M: ... ...
N: ... .
O: ... ... ...
P: . ... ... .
Q: ... ... . ...
R: . ... .
S: . . .
T: ...
U: . . ...
V: . . . ...
W: . ... ...
X: ... . . ...
Y: ... . ... ...
Z: ... ... . .
0: ... ... ... ... ...
1: . ... ... ... ...
2: . . ... ... ...
3: . . . ... ...
4: . . . . ...
5: . . . . .
6: ... . . . .
7: ... ... . . .
8: ... ... ... . .
9: ... ... ... ... .
Signal gap: 1
Letter gap: 3
Word gap: 7
"""
dictionary1 = {
    "A":". ...",
    "B":"... . . .",
    "C":"... . ... .",
    "D":"... . .",
    "E":".",
    "F":". . ... .",
    "G":"... ... .",
    "H":". . . .",
    "I":". .",
    "J":". ... ... ...",
    "K":"... . ...",
    "L":". ... . .",
    "M":"... ...",
    "N":"... .",
    "O":"... ... ...",
    "P":". ... ... .",
    "Q":"... ... . ...",
    "R":". ... .",
    "S":". . .",
    "T":"...",
    "U":". . ...",
    "V":". . . ...",
    "W":". ... ...",
    "X":"... . . ...",
    "Y":"... . ... ...",
    "Z":"... ... . .",
    "0":"... ... ... ... ...",
    "1":". ... ... ... ...",
    "2":". . ... ... ...",
    "3":". . . ... ...",
    "4":". . . . ...",
    "5":". . . . .",
    "6":"... . . . .",
    "7":"... ... . . .",
    "8":"... ... ... . .",
    "9":"... ... ... ... ."}
dictionary2 = dict(zip(dictionary1.values(), dictionary1.keys()))
def encode(string):
    out = ""
    string = string.upper()
    words = string.split(" ")
    for word in words:
        for char in word:
            if char in "QWERTYUIOPASDFGHJKLZXCVBNM1234567890":
                out += dictionary1[char]
            else:
                out += char
            out += "   "
        out += "    "
    return out
def decode(string):
    out = ""
    words = string.split("       ")
    for word in words:
        chars = word.split("   ")
        for char in chars:
            out += dictionary2[char]
        out += " "
    return out